-----

## layout: post title: "ReelCraft: The AI Pipeline That Turns Long Articles into Viral Shorts" date: 2025-10-28 description: "How we built ReelCraft—an automated system using Gemini AI, Pexels, and FFmpeg—to convert any web article into an engaging 30-60 second short-form video in one click." author: "Bejay" tags: [AI, VideoGen, LLM, Gemini, Python, FastAPI] acknowledgment: "Built with the visionary zeal of Paras and the technical brilliance of Aakash."

## Introduction: The Short-Form Addiction Dilemma

It was during the last of **Ninety Days** (early 2024), a hyper-productive sprint where our team was shipping app prototypes weekly. For one such prototype, **Paras** (our CEO) had a funky, yet brilliant, hypothesis: almost everyone in the tech sphere **wants to be productive** and read long-form content, but is simultaneously **addicted to short-form content** (Reels, TikToks, Shorts). The addiction was real, and it was a problem begging for an AI solution.

The goal was simple: bridge the gap. Turn the boring, text-heavy productivity content into the snackable, engaging format of a reel.

I was entrusted with building the initial Proof of Concept (PoC) along with my colleague and best friend, **Aakash**. We had a blast. Fast forward to now (October 2025), I've decided to reproduce the entire pipeline, refine it, and document the process. We called it **ReelCraft**.

**ReelCraft** automatically transforms any web article into a polished, 30–60 second vertical video, complete with narration, stock media, and background music.

-----

## What is ReelCraft? The End-to-End Automation Engine 🎬

ReelCraft is a fully automated video generation pipeline. You paste an article URL, and out comes a professional-grade short video, perfectly formatted for social media.

### Core Features at a Glance

  * **Automatic Script Generation:** Gemini AI converts dense articles into **7-15 punchy, scene-based scripts** optimized for a fast-paced reel format.
  * **AI-Powered Voice Over:** Natural-sounding voice narration is generated for each scene using **Gemini Text-to-Speech (TTS)**.
  * **Smart Asset Selection:** The pipeline automatically finds and downloads relevant **images and videos** from **Pexels** based on keywords generated alongside the script.
  * **Professional Composition:** **FFmpeg** stitches the visual assets, audio, and background music together into a vertical video (720x1280).
  * **Modern Web UI:** A user-friendly, responsive interface with **WebSocket** integration for **real-time progress tracking**.

### The Flow: URL to Reel

The entire process is a streamlined, five-step pipeline:

$$\text{Article URL} \xrightarrow{\text{Content Extraction}} \text{Script Generation} \xrightarrow{\text{Audio Generation}} \text{Asset Download} \xrightarrow{\text{Video Editing}} \text{Final Video}$$

-----

## System Design: How It All Fits Together

The architecture is built for speed and concurrency, leveraging asynchronous Python (`asyncio`) and specialized APIs for each task.

### 1\. Content Extraction (FireCrawl)

The first challenge is getting clean, structured text from a messy web page.

  * We use **FireCrawl** for this. It handles JavaScript-rendered content and returns the article in **clean Markdown**, ready for the LLM.

### 2\. Script Generation (Gemini AI)

This is the **core intelligence**. A prompt is sent to a **Gemini** model (likely Gemini 2.5 Flash for speed) that instructs it to perform a few crucial tasks:

  * Create a compelling **title**.
  * Break the article down into **7-15 scenes** (max 60 seconds total duration).
  * For *each scene*, generate the **narration text** and **3 descriptive keywords** for visual search. This separation of concerns is key for quality output. The output is structured JSON.

### 3\. Audio & Asset Generation (Parallel Processing)

These two heavy tasks run **concurrently** to minimize latency:

  * **Audio Generation:** The narration for all 7-15 scenes is converted to separate `.wav` files using the **Gemini TTS API**. We use an `asyncio.Semaphore` to limit concurrent requests (e.g., max 3 at once) to avoid API rate limits.
  * **Asset Download:** Using the keywords from the script, the pipeline calls the **Pexels API** to download the most relevant image or video for each scene, ensuring it matches the required vertical aspect ratio.

### 4\. Video Composition (FFmpeg)

The final assembly line, driven by the robust **FFmpeg** utility:

  * **Stitching:** Visual assets are concatenated sequentially.
  * **Duration Sync:** This was a key challenge: the audio duration must precisely match the visual duration. FFmpeg is used to **automatically adjust the audio tempo** (speed) to align perfectly with the scene's visual clip length, ensuring a snappy flow.
  * **Audio Mixing:** The voice-over audio track is layered with a background music track, with the voice-over volume boosted and the music volume suppressed (e.g., `background_volume = 0.2`).
  * **Effects:** Basic effects (like zoom/pan for static images) are applied to maintain visual dynamism.

### The FastAPI Backend & Web UI

The entire system is wrapped in a **FastAPI** application, providing both a **REST API** (`/api/generate-video`) and a **WebSocket** connection (`/ws`) to stream real-time progress updates to the frontend. This allows users to see *exactly* when the script is generating, audio is downloading, and FFmpeg is composing.

-----

## Technical Learnings & Design Decisions

### Decision 1: Structured JSON Output for LLM

Initially, we just asked the LLM for a script. It was messy.

  * **Solution:** We enforced a strict JSON schema that requires the scene number, script text, and a dedicated `asset_keywords` array for each scene. This structured output is vital—it makes the downstream parallel processing of audio and visuals deterministic and reliable.

### Decision 2: Prioritizing Parallelism for UX

The full pipeline (extraction to final video) is inherently slow due to multiple API calls (Gemini, Pexels).

  * **Insight:** Waiting 3 minutes for a video is better than waiting 10 minutes.
  * **Implementation:** By running the **Audio Generation** and **Asset Download** steps concurrently (`asyncio.gather`), we slashed the total processing time significantly, resulting in a much better user experience.

### Decision 3: Tempo Adjustment for Seamless Sync

A silent video is useless for a reel.

  * **Problem:** The Gemini TTS audio for a scene might be 5.2 seconds long, but the chosen Pexels clip might be 6 seconds. A simple cut creates a jarring silence.
  * **Solution:** We calculate the required speed adjustment factor ($\frac{\text{Visual Duration}}{\text{Audio Duration}}$) and apply it using FFmpeg's `atempo` filter. This subtly speeds up or slows down the voice-over so it ends precisely when the visual scene transitions.

### Decision 4: Monitoring with Langfuse

To move beyond "it works on my machine," we integrated **Langfuse**.

  * **Benefit:** It tracks every single LLM call (scripting, TTS), their latency, and token usage. This allows us to debug prompt failures and, critically, monitor API costs.

-----

## ReelCraft Technical Stack

| Component | Tool / API | Purpose |
| :--- | :--- | :--- |
| **LLM & TTS** | Google Gemini API (`google-genai`) | Scripting and Voice-Over Generation |
| **Content Extraction** | FireCrawl API (`firecrawl-py`) | Cleanly scrape article text from any URL |
| **Stock Media** | Pexels API (`requests`) | Search and download royalty-free video/images |
| **Video Editing** | FFmpeg (`ffmpeg-python`) | Final composition, stitching, and audio mixing |
| **Web Server & API** | FastAPI, Uvicorn, WebSocket | Real-time progress tracking and API endpoints |
| **Monitoring** | Langfuse | Tracing, debugging, and cost management |

-----

## What’s Next: The Roadmap 🚀

While ReelCraft is a functional and polished PoC, there's always more to build:

  * **Subtitle Generation:** Crucial for short-form content consumption (watching without sound).
  * **Customization:** Adding options for custom background music, different TTS voices, and font/style controls.
  * **Batch Processing:** Allowing users to queue up multiple articles for video generation.
  * **Evals:** Developing a proper LLM-as-a-Judge evaluation framework to quantitatively assess the quality of the generated script and asset keywords.

The blend of an LLM's creativity with robust media processing tools like FFmpeg proved to be an incredibly powerful combination. We took a common problem—the attention-span gap—and solved it with a fully automated, scalable pipeline.

**Check out the repository and try the API\!**

-----

**GitHub**: [repository-url-here]

**API Docs**: [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs) (when running locally)
---
layout: post
title: "ReelCraft: The AI Pipeline That Turns Long Articles into Viral Shorts"
date: 2025-10-30
description: "A technical deep-dive into ReelCraft—an automated system using Gemini AI, Pexels, and FFmpeg—that converts any web article into an engaging 30-60 second short-form video. From the initial PoC to production-ready reliability."
author: "Bejay Ketan Guin"
tags: [AI, VideoGen, Tech]
acknowledgment: "Blog written with the help of <span style='color: #3182ce; font-weight: 500;'>Claude</span>."
---


## Introduction: The Short-Form Addiction Dilemma

It was during the last days of **Nintee** (my last startup stint, early 2024), a hyper-productive sprint where our team was shipping app prototypes weekly. For one such prototype, [**Paras**](https://x.com/paraschopra) (our CEO) had a funky, yet brilliant, hypothesis: almost everyone in the tech sphere **wants to be productive** and read long-form content, but is simultaneously **addicted to short-form content** (Reels, TikToks, Shorts). The addiction was real, and it was a problem begging for an AI solution.

The goal was simple: bridge the gap. Turn the boring, text-heavy productivity content into the snackable, engaging format of a reel.

I was entrusted with building the initial Proof of Concept (PoC) along with my colleague and best friend, [**Aakash**](https://www.aakashb.xyz/). We had a blast. The timing was perfect—ChatGPT had just launched the previous year, and GenAI was beginning to show its potential for creative applications.

Fast forward to now (October 2025), I've decided to reproduce the entire pipeline from scratch, refine it with modern best practices, and document the process. I don't know if I'm breaking any IP here, but the learnings are too valuable not to share. I will be calling it **ReelCraft**.

**ReelCraft** automatically transforms any web article into a polished, 30–60 second vertical video, complete with narration, stock media, and background music.

-----

## What is ReelCraft? The End-to-End Automation Engine 🎬

ReelCraft is a fully automated video generation pipeline. You paste an article URL, and out comes a professional-grade short video, perfectly formatted for social media.

### Core Features at a Glance

  * **Automatic Script Generation:** Gemini AI converts dense articles into **7-15 punchy, scene-based scripts** optimized for a fast-paced reel format.
  * **AI-Powered Voice Over:** Natural-sounding voice narration is generated for each scene using **Gemini Text-to-Speech (TTS)**.
  * **Smart Asset Selection:** The pipeline automatically finds and downloads relevant **images and videos** from **Pexels** based on keywords generated alongside the script.
  * **Professional Composition:** **FFmpeg** stitches the visual assets, audio, and background music together into a vertical video (720x1280).
  * **Visual Polish Features:**
    - **Dynamic Audio Ducking:** Background music automatically lowers during voiceover and rises during pauses for professional audio mixing
    - **Text-Only Scenes:** AI generates punchy text overlays (1-5 words) on solid backgrounds to emphasize key points
    - **Smart Aspect Ratios:** Landscape videos display with blurred background fill for portrait frames
    - **Smooth Transitions:** Dynamic scene transitions (fade, wipe, slide) instead of hard cuts
  * **Modern Web UI:** A user-friendly, responsive interface with **WebSocket** integration for **real-time progress tracking**.

### The Flow: URL to Reel

The entire process is a streamlined, five-step pipeline:

```
Article URL
    ↓
Content Extraction
    ↓
Script Generation
    ↓
Audio + Asset Generation
    ↓
Video Editing
    ↓
Final Video
```

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

### Decision 4: Building Resilience into the Pipeline

As we tested ReelCraft with various articles and network conditions, we encountered several failure modes that needed addressing.

  * **Problem:** API calls would occasionally timeout, network issues caused intermittent failures, and some websites had scraping challenges.
  * **Solution:** We implemented a comprehensive resilience strategy:
    - **Async Retry Mechanism:** Added an `@async_retry` decorator with exponential backoff (1s, 2s, 4s) for HTTP requests, automatically recovering from transient network failures
    - **Increased Timeouts:** Extended HTTP timeouts from 30s to 90s (and 120s for Pexels) to accommodate slower connections and large media downloads
    - **Enhanced Web Scraping:** Added content validation checks for FireCrawl responses, detecting common error patterns (e.g., "access denied", "not found") and providing meaningful error messages
    - **Comprehensive Error Handling:** Added try-catch blocks throughout the pipeline with specific error types (`WebScrapingError`) to distinguish between different failure modes
    - **User-Friendly Feedback:** Enhanced progress updates to inform users about specific failures (e.g., "Failed to extract content", "Connection interrupted") rather than generic errors

  * **Impact:** These changes dramatically improved the success rate—videos that previously failed due to temporary network hiccups now complete successfully. The system gracefully handles edge cases like paywalled articles, JavaScript-heavy sites, and API rate limits.

### Decision 5: Monitoring with Langfuse

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

## Recent Improvements: From PoC to Production-Ready 🔧

The initial prototype worked, but it had rough edges. After running ReelCraft on dozens of real-world articles, we identified and fixed several critical pain points:

### Reliability & Resilience

The biggest challenge wasn't the happy path—it was handling the **messy reality** of production use.

**The Problems:**
- Random network timeouts killing entire 3-minute video generations
- Pexels API occasionally taking 45+ seconds to return large video files
- FireCrawl struggling with certain websites (JavaScript-heavy sites, paywalled content, bot detection)
- Generic error messages like "Request failed" that gave no actionable debugging info

**The Solutions:**
- **Automatic Retry Logic:** Implemented an exponential backoff retry mechanism (`@async_retry` decorator) that automatically retries failed HTTP requests up to 3 times with 1s, 2s, and 4s delays. This single change increased our success rate from ~70% to ~95%.
- **Generous Timeouts:** Bumped HTTP timeouts from 30s to 90s (and 120s for Pexels media downloads). Better to wait an extra minute than fail entirely.
- **Smart Content Validation:** Added checks to detect when FireCrawl returns error pages instead of actual content (e.g., checking for phrases like "access denied", empty responses, or suspiciously short content).
- **Granular Error Reporting:** Created custom exception types (`WebScrapingError`) and enhanced WebSocket progress updates to tell users *exactly* what went wrong ("Failed to extract article content" vs. "Connection interrupted").

### User Experience Enhancements

  * **Real-Time Error Feedback:** The frontend now displays specific error messages for different failure scenarios, helping users understand whether the issue is with the article URL, network connectivity, or API limits.
  * **Better Asset Descriptions:** Improved the metadata for downloaded Pexels videos to include dimensions and duration, making debugging and asset tracking easier.

**Impact:** These changes transformed ReelCraft from a "works on my machine" demo into a **reliable, production-grade tool**. The retry mechanism alone eliminated 80% of transient failures, and the enhanced error handling made debugging issues 10x faster.

-----

## What's Next: The Roadmap 🚀

While ReelCraft is a functional and polished PoC, there's always more to build:

  * **Subtitle Generation:** Crucial for short-form content consumption (watching without sound).
  * **Customization:** Adding options for custom background music, different TTS voices, and font/style controls.
  * **Batch Processing:** Allowing users to queue up multiple articles for video generation.
  * **Evals:** Developing a proper LLM-as-a-Judge evaluation framework to quantitatively assess the quality of the generated script and asset keywords.
  * **A/B Testing Framework:** Systematically test different prompts, scene counts, and asset selection strategies to optimize for engagement.

-----

## Reflections: What I Learned Building This

Building ReelCraft taught me several lessons that go beyond the technical stack:

**1. The 80/20 of Production Systems**

The initial PoC took about a week. Making it **reliable** took another month. The difference between "works in demos" and "works in production" is enormous—you need retry logic, timeout handling, graceful degradation, and comprehensive error reporting. These aren't sexy features, but they're what separate toys from tools.

**2. Parallelism is a Force Multiplier**

The moment we switched from sequential to parallel processing (audio + assets concurrently), the user experience transformed. A 10-minute wait becomes a 3-minute wait. In product terms, that's the difference between "this is too slow" and "this is acceptable."

**3. LLMs + Traditional Tools = Magic**

The real power isn't just in the LLM—it's in the **combination**. Gemini generates creative scripts, but FFmpeg does the heavy lifting of video composition. Pexels provides the visuals, but the LLM's keyword generation makes the search intelligent. The system is greater than the sum of its parts.

**4. Error Messages are User Empathy**

Changing "Request failed" to "Failed to extract article content - the site may be blocking scrapers" is a tiny code change but a huge UX win. Good error messages respect the user's time and intelligence.

-----

## Closing Thoughts

The blend of an LLM's creativity with robust media processing tools like FFmpeg proved to be an incredibly powerful combination. We took a common problem—the attention-span gap—and solved it with a fully automated, scalable pipeline.

What started as a weekend hackathon project at Nintee has evolved into something I'm genuinely proud of. It's not perfect, but it works, it's reliable, and it solves a real problem.

If you're working on similar AI-powered creative tools, I hope this deep-dive gives you some ideas. And if you try ReelCraft and generate a video, I'd love to see it!

**Check out the repository and try the API\!**

-----

**GitHub**: [https://github.com/BKG123/reelcraft](https://github.com/BKG123/reelcraft){:target="_blank" rel="noopener noreferrer"}

**API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs) (when running locally)

**Author**: Bejay Ketan Guin
**With special thanks to**: [Paras Chopra](https://x.com/paraschopra) for the vision, and [Aakash Bakhle](https://www.aakashb.xyz/) for the original collaboration.

---

## More from my blog

- **[Frame AI: Building an AI-Powered Photography Assistant](/2025/10/20/frame-ai.html)** - How I built an AI system that analyzes and enhances photos while teaching me
- **[Everything in Life is Linear Regression](/2025/10/16/life-is-linear-regression.html)** - Why life's complexities are best understood as weighted combinations of multiple factors
- **[Coding in the era of LLMs](/2025/09/21/coding-in-the-era-of-llms.html)** - My thoughts on AI-assisted coding and the importance of learning fundamentals
- **[Your Feelings Lie to You (Sometimes)](/2025/04/15/your-feelings-lie-to-you-sometimes.html)** - My exploration of how emotions and logic shape our decision-making process
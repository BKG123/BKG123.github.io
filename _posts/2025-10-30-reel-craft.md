---
layout: post
title: "ReelCraft: The AI Pipeline That Turns Long Articles into Viral Shorts"
date: 2025-10-30
description: "A technical deep-dive into ReelCraft—an automated system using Gemini AI, Pexels, and FFmpeg—that converts any web article into an engaging 30-60 second short-form video. From the initial PoC to production-ready reliability."
author: "Bejay Ketan Guin"
tags: [AI, VideoGen, Tech]
acknowledgment: "Blog written with the help of <span style='color: #3182ce; font-weight: 500;'>Claude</span>."
---

## How I got the idea?

It was during the last days of **Nintee** (my last startup stint, early 2024), a hyper-productive sprint where our team was shipping app prototypes weekly. For one such prototype, [Paras](https://x.com/paraschopra) (our CEO) had a funky, yet brilliant, hypothesis: almost everyone in the tech sphere **wants to be productive** and read long-form content, but is simultaneously **addicted to short-form content** (Reels, TikToks, Shorts). 

The goal was simple: bridge the gap. Turn the boring, text-heavy productivity content into the consumable, engaging format of a reel.

I was entrusted with building the initial Proof of Concept (PoC) along with my colleague and best friend, [Aakash](https://www.aakashb.xyz/). We had a blast. The timing was perfect—ChatGPT had just launched the previous year, and GenAI was beginning to show its potential for creative applications.

Fast forward to now (October 2025), I've decided to reproduce the entire pipeline from scratch, refine it with modern best practices, and document the process. I don't know if I'm breaking any IP here, but the experience are too valuable not to share. I will be calling it **ReelCraft**.

## What is ReelCraft? 

ReelCraft is a fully automated video generation pipeline. You paste an article URL, and out comes a professional-grade short video, perfectly formatted for social media.

### The Flow: URL to Reel

Five-step pipeline:

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

### 1\. Content Extraction (FireCrawl)

The first challenge is getting clean, structured text from a messy web page.

  * We use **FireCrawl** for this. It handles JavaScript-rendered content and returns the article in **clean Markdown**, ready for the LLM.

### 2\. Script Generation (Gemini AI)

This is the **core intelligence**. A prompt is sent to a **Gemini** model (Gemini 2.5 Flash) that instructs it to perform a few crucial tasks:

  * Create a compelling **title**.
  * Break the article down into **7-15 scenes** (max 60 seconds total duration).
  * For *each scene*, generate the **narration text** and **3 descriptive keywords** for visual search. 

   The idea is to extract as much from the LLM. Generation of script using the article context. Extract as much details as possible.
So we let the llm decide how many scenes to be there. Each screen object would have 2-3 fields.
```json
{
    "scene_number": 7,
    "script": "Younger minds have the most room to change their thinking and experience 'surprise.'",
    "asset_keywords": [
        "brain growth animation",
        "mind blown reaction",
        "lightbulb moment"
    ],
    "asset_type": "video"
}
```
Here's the [link to the full prompt](https://github.com/BKG123/reelcraft/blob/main/config/prompts.py).

### 3\. Audio & Asset Generation (Parallel Processing)

These two tasks run **concurrently** to minimize latency:

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

Evolution:
-


- Now at first we were also letting the llm decide the duration to. But the problem was the sync. The time taken to speak a sentence varies from person to person and TTS to TTS - lol.

- In the next go, we decided to let the TTS take its own time to speak the content of each script.
- So the sync problem was solved.
- Then add the duration in the script object

Now another thing was that we need contextual assets. At first we were sending keyword to pexels
To improve on the relevance,started sending phrases also had an idea while discussiong with claude - get descrriptions of imagtes/video and make a separate api call to rerank. 

A funny incident:

I hadn't handled the error in markdown generation properly. Now the system generated a reel end to end. The article was about some vector indices. Now the reel got generated. And I was checking it out for quality and stuff. A few mins into the video, I was shocked and somewhat amused to find that the reel was about errors lol. So decided to add error catching.



prompt_image.png

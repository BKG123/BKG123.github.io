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

**ReelCraft** automatically transforms any web article into a polished, 30–60 second vertical video, complete with narration, stock media, and background music.


Evolution:
- Extract as much from the LLM. Generation of script using the article context. Extract as much details as possible.
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
- Now at first we were also letting the llm decide the duration to. But the problem was the sync. The time taken to speak a sentence varies from person to person and TTS to TTS - lol.

- In the next go, we decided to let the TTS take its own time to speak the content of each script.
- So the sync problem was solved.
Here's the [link to the full prompt](https://github.com/BKG123/reelcraft/blob/main/config/prompts.py).

prompt_image.png

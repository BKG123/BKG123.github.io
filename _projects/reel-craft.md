---
layout: project
title: "ReelCraft"
date: 2025-10-30
description: "An automated video generation pipeline that converts web articles into engaging 30-60 second vertical videos using Gemini AI, Pexels, and FFmpeg."
tech_stack: "FastAPI · Python · Gemini AI · FFmpeg · Pexels API · FireCrawl"
thumbnail: "/assets/images/2025-10-30-reel-craft/reelcraft-app.png"
links:
  github: "https://github.com/BKG123/reelcraft"
---

ReelCraft is a fully automated video generation pipeline that transforms any web article into a professional-grade short video. Simply paste an article URL, and the system generates a polished 30-60 second vertical video complete with AI narration, stock media, and background music.

## Key Features

- **Automatic Script Generation**: Gemini AI converts articles into 7-15 punchy, scene-based scripts optimized for fast-paced reel format
- **AI-Powered Voice Over**: Natural-sounding narration generated for each scene using Gemini Text-to-Speech
- **Smart Asset Selection**: Automatically finds and downloads relevant images and videos from Pexels based on AI-generated keywords
- **Professional Composition**: FFmpeg stitches visual assets, audio, and background music into vertical video (720x1280)
- **Dynamic Audio Ducking**: Background music automatically adjusts during voiceover for professional audio mixing
- **Real-Time Progress Tracking**: WebSocket integration provides live updates during video generation

## Technical Highlights

- Asynchronous Python architecture with `asyncio` for concurrent audio generation and asset downloads
- Intelligent duration synchronization using FFmpeg's `atempo` filter to match audio precisely with visual transitions
- Content extraction via FireCrawl API handles JavaScript-rendered content and returns clean Markdown
- Modular pipeline design: Content Extraction → Script Generation → Audio + Asset Generation → Video Editing → Final Video
- Background music ducking implementation with silence detection and dynamic volume adjustment

## Sample Output

Here's an example reel generated from Paul Graham's essay "[The Shape of the Essay Field](https://paulgraham.com/field.html)":

<div style="max-width: 400px; margin: 2rem auto;">
  <video controls preload="metadata" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);" playsinline>
    <source src="/assets/images/2025-10-30-reel-craft/sample.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p style="text-align: center; margin-top: 1rem; font-size: 0.9rem; color: #666;">
    A 45-second reel automatically generated from a 3,000+ word essay
  </p>
</div>

---

[Read the full blog post →](/2025/10/30/reel-craft.html)

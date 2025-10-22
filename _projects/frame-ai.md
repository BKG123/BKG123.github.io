---
layout: project
title: "Frame AI"
date: 2025-10-20
description: "An AI-powered photography assistant that analyzes photos and suggests enhancements using vision LLMs and nano-banana image generation."
tech_stack: "FastAPI · Python · Gemini Flash · nano-banana · SQLite"
thumbnail: "/assets/images/2025-10-20-frame-ai/app-1.png"
links:
  demo: "https://frame-ai.bejayketanguin.com/"
  github: "https://github.com/BKG123/frame-ai"
---

Frame AI is an AI-powered photography assistant that bridges the gap between taking photos and knowing how to improve them. It analyzes images using Gemini 2.5 Flash to evaluate photography principles, then generates three distinct enhanced variations using Gemini 2.5 Flash Image (nano-banana).

## Demo

<figure style="margin: 2rem 0;">
  <video width="100%" controls style="border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); border: 1px solid #e5e7eb;">
    <source src="/assets/video/frame-ai.md/frame-ai-demo.webm" type="video/webm">
    Your browser does not support the video tag.
  </video>
  <figcaption style="text-align: center; margin-top: 0.5rem; color: #6b7280; font-size: 0.9rem;">Frame AI in action: analyzing a photo and generating enhanced variations</figcaption>
</figure>

## Results

<div class="image-grid">
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/og_image.png" alt="Original photo" style="border: 1px solid #e5e7eb; border-radius: 4px;">
    <figcaption>Original</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/var1.png" alt="Enhanced variation 1" style="border: 1px solid #e5e7eb; border-radius: 4px;">
    <figcaption>Variation 1: Technical Perfection</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/var2.png" alt="Enhanced variation 2" style="border: 1px solid #e5e7eb; border-radius: 4px;">
    <figcaption>Variation 2: Atmospheric Reinterpretation</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/var3.png" alt="Enhanced variation 3" style="border: 1px solid #e5e7eb; border-radius: 4px;">
    <figcaption>Variation 3: Conceptual Narrative</figcaption>
  </figure>
</div>

## Key Features

- **Intelligent Analysis**: Detailed compositional feedback with numerical scores (exposure, composition, lighting, overall)
- **Three Creative Variations**: Technical perfection, atmospheric reinterpretation, and conceptual narrative
- **Smart Caching**: Content-based hashing (SHA-256) for deduplication and cost optimization

## Technical Highlights

- FastAPI backend with SQLite for persistence and Server-Sent Events for streaming analysis
- Content-based hashing (SHA-256) enables reliable deduplication while remaining privacy-friendly
- Separate LLM call generates editing prompts from analysis before passing to nano-banana—produces more precise edits than passing raw analysis directly
- Parallel image generation using `asyncio.gather` for three simultaneous variations

---

[Read the full blog post →](/2025/10/20/frame-ai.html)

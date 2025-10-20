---
layout: project
title: "Frame AI"
date: 2025-10-20
description: "An AI-powered photography assistant that analyzes photos and suggests enhancements using vision LLMs and nano-banana image generation."
tech_stack: "FastAPI · Python · Gemini Flash · nano-banana · SQLite"
thumbnail: "/assets/images/2025-10-20-frame-ai/app-1.png"
links:
  demo: "#"
  github: "#"
---

Frame AI is an AI-powered photography assistant that helps bridge the gap between taking photos and knowing how to improve them. It analyzes images using vision LLMs to check alignment with photography principles, then generates enhanced variations using Google's nano-banana model.

<div class="image-grid">
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/og_image.png" alt="Original photo">
    <figcaption>Original</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/var1.png" alt="Enhanced variation 1">
    <figcaption>Enhanced Variation 1</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/var2.png" alt="Enhanced variation 2">
    <figcaption>Enhanced Variation 2</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/var3.png" alt="Enhanced variation 3">
    <figcaption>Enhanced Variation 3</figcaption>
  </figure>
</div>

## Key Features

- **Intelligent Analysis**: Evaluates photos against photography best practices (rule of thirds, lighting, composition)
- **AI-Powered Enhancement**: Generates three variations of enhanced images
- **Smart Caching**: Hash-based image caching for performance and cost optimization

## Technical Highlights

The system uses a FastAPI backend with SQLite for data persistence. Image analysis is handled by Gemini Flash models, which provide detailed compositional feedback. A key design decision was generating separate enhancement prompts for nano-banana rather than passing raw analysis—this produces more precise edits since nano-banana excels at following clear instructions.

The architecture implements hash-based caching to avoid redundant LLM calls, significantly reducing API costs for repeat analyses.

## What I Learned

Building Frame AI taught me about LLM prompting nuances, system design for AI-powered applications, and the importance of caching strategies. I also learned when to add features and—just as importantly—when to remove them.

---

[Read the full blog post →](/2025/10/20/frame-ai.html)

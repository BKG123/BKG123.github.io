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

## Overview

Frame AI is an AI-powered photography assistant that bridges the gap between taking photos and knowing how to improve them. It analyzes images using vision LLMs (Gemini Flash) to check alignment with widely accepted photography principles, and enhances images using Google's nano-banana model.

![Frame AI Interface](/assets/images/2025-10-20-frame-ai/app-1.png)

## The Problem

As a mobile photography enthusiast, I often take photos trying to apply principles like rule of thirds, leading lines, and proper lighting. But more often than not, I'm not sure if I'm applying them correctly or how to improve my shots.

## The Solution

Frame AI provides:

1. **Intelligent Analysis**: Evaluates photos against photography best practices
2. **Actionable Feedback**: Clear, bullet-pointed suggestions on what's working and what's not
3. **AI-Powered Enhancement**: Generates three variations of enhanced images using nano-banana

## Technical Architecture

### High-Level Flow

```
User Upload → FastAPI Backend → Image Processing & Caching →
LLM Analysis → Database Storage → Enhancement Trigger →
3 Prompts Generated → 3 Images via nano-banana
```

### Key Components

- **Backend**: FastAPI for fast, async API endpoints
- **Database**: SQLite for lightweight data persistence
- **LLM Integration**: Gemini Flash models for image analysis
- **Image Generation**: nano-banana for AI-powered enhancements
- **Caching**: Hash-based image caching for performance optimization

![System Design](/assets/images/2025-10-20-frame-ai/system-design.png)

## Key Design Decisions

### 1. Separate Instruction Generation

Instead of passing analysis directly to nano-banana, I generate three separate prompts focusing on different aspects of the feedback. This produces more precise, actionable edits since nano-banana excels at following clear instructions rather than reasoning.

### 2. Image Caching Strategy

Implemented hash-based caching using file contents to avoid redundant LLM calls and improve performance. This significantly reduces API costs for repeat analyses.

### 3. Three-Variation Approach

Generate three different enhanced versions to provide variety and let users choose what works best for their vision.

## Example Results

<div class="image-grid" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 2rem 0;">
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/og_image.png" alt="Original photo">
    <figcaption>Original</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/var1.png" alt="Enhanced variation 1">
    <figcaption>Variation 1</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/var2.png" alt="Enhanced variation 2">
    <figcaption>Variation 2</figcaption>
  </figure>
  <figure>
    <img src="/assets/images/2025-10-20-frame-ai/var3.png" alt="Enhanced variation 3">
    <figcaption>Variation 3</figcaption>
  </figure>
</div>

## What I Learned

- **LLM Prompting Nuances**: How to structure prompts for specific, actionable outputs
- **System Design for AI Apps**: Building reliable, cost-effective AI-powered systems
- **Caching Strategies**: When and how caching matters for performance
- **Product Iteration**: Knowing when to add features and when to remove them
- **AI Limitations**: Understanding what AI is good at vs. where it needs help

## Tech Stack Details

- **Backend**: FastAPI (async Python web framework)
- **Database**: SQLite (lightweight, file-based)
- **AI Models**:
  - gemini-2.5-flash (main analysis)
  - gemini-2.5-flash-lite (quick operations)
  - gemini-2.5-flash-image (image understanding)
  - nano-banana (image generation)
- **Deployment**: TBD

## Future Improvements

- Batch processing for multiple images
- User style preferences and learning
- Mobile app integration
- Community sharing features
- Advanced editing controls

## Links

- [Read the full blog post](/2025/10/20/frame-ai.html)
- [Try the demo](#) (Coming soon)
- [View source code](#) (Coming soon)

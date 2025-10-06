---
layout: post
title: "Coding in the era of LLMs"
date: 2025-09-21
description: "My thought dump on AI and coding"
author: "Bejay"
acknowledgment: "Original thoughts, polished with a little help from <span style='color: #3182ce; font-weight: 500;'>Claude</span>."
---

The common people began to have access to "AI" since the launch of chatgpt in 2022 end (30th Nov, 2022 to be precise).
Before that AI was on a sci-fi domain for people. AI was being used for very specific day to day tasks but it was not as significant or head turner as perhaps a Ultron of Avengers fame.

This opened a new avenue. People started recognising the true power of AI. This was also felt in the software engineering career. People started to write code using these LLMs.

I also joined the bandwagon. It definitely felt helpful for certain well defined tasks.
But AI assisted coding was far from perfect. But it steadily started improving. 

The turning point for me was cursor - the AI assisted IDE. I really started growing fond of the tab feature. By then the models had started to improve drastically too. The claude sonnet 3.5 + cursor duo turned out to be really a great duo. The tab feature specifically works for me because it is I who take care of the logic while the tab feature autocompletes it. It makes coding faster.

Then came cursor agent. It could really start building features on its own.

## The Dark Side Nobody Talks About

But here's the thing that worries me as I see more people jumping into this AI-powered coding revolution: **not everyone should be coding with AI the same way.**

There's a dangerous trend emerging, especially among beginners. People who are brand new to programming are treating AI as a magic wand that removes the need to actually learn to code. They're "vibe coding" - throwing prompts at ChatGPT or Cursor and shipping whatever comes out without really understanding what's happening under the hood.

### The Data Tells a Sobering Story

The numbers paint an uncomfortable picture. A 2025 study by METR tracked experienced developers and found something shocking: when using AI tools, developers actually took 19% longer to complete tasks compared to working without AI. Even more troubling? The developers thought they were 20% faster. That's a 39-point gap between perception and reality.

Trust in AI coding tools has been plummeting too. Stack Overflow's 2025 survey shows developer trust in AI output accuracy dropped from 43% in 2024 to just 33% in 2025. The favorability of adding AI tools to workflows fell from 72% to 60% in the same period.

### The Beginner's Trap

For beginners, the risks are even more severe. When you don't have the fundamentals, you can't tell when AI is wrong. And it's wrong more often than you'd think.

Consider these real problems people are facing:

- Up to 30% of packages suggested by AI tools don't even exist - they're hallucinated, creating security vulnerabilities
- 40% of AI-generated database queries are vulnerable to SQL injection attacks
- AI often puts security checks on the client side instead of the server
- Hardcoded API keys and secrets frequently appear in generated code

One experienced developer shared how an AI-generated script locked them out of root access because they asked it to "make it super secure" without reviewing the implementation. These aren't edge cases. They're common patterns.

### You Still Need to Learn the Fundamentals

Here's what the experts are saying: AI coding without a foundation is like letting someone who's never flown a plane sit in the cockpit and take off in automated mode. It sounds crazy when you put it that way, right?

As one senior product manager at Qt Group put it: "If junior developers generate code with AI assistants and deploy the code to digital products without truly understanding it, then they run into the risk of introducing suboptimal code. Whenever junior developers use AI-generated code, they're not really learning how to write and review code themselves."

The most successful approach isn't to avoid AI - that would be career suicide at this point. According to a 2024 developer survey, 76% of developers are using or planning to use AI coding assistants. The market for AI coding tools was valued at $5.5 billion in 2024 and is projected to hit $47.3 billion by 2034.

But you need to **earn the right** to use these tools effectively.

### The Right Way to Learn with AI

Think of AI as a senior developer looking over your shoulder, not as a replacement for your brain. Here's what actually works:

1. **Learn the fundamentals first**. Understand variables, control flow, data structures, functions. Write enough code manually that you can spot when something looks wrong.

2. **Write it yourself, then compare**. Try solving a problem on your own first. Then ask AI how it would do it. See what's different. Learn from the gaps.

3. **Never deploy code you don't understand**. If AI generates something and you can't explain what each part does, you're not ready to use it. Debug it. Break it. Fix it. Make it yours.

4. **Use AI to augment, not replace, learning**. AI is incredible for explaining concepts, suggesting improvements, and catching bugs. But it can't build your mental model of how code works.

The developers who will thrive aren't the ones who can write the best prompts. They're the ones who know enough to recognize when AI is leading them astray.

### Looking Forward

AI coding tools are only going to get better. Models are improving, context windows are expanding (Cursor now offers 1M+ token context windows), and response times are getting faster. We're seeing the emergence of autonomous coding agents that can handle entire features.

But the gap between those who understand what's happening and those who are just prompt-engineering their way through is going to become a chasm. Companies are already learning what happens when their codebases get infiltrated with AI-generated code at scale. We're seeing bigger incidents with slower resolution times because the people trying to fix problems don't understand the code that created them.

## My Take

I love AI coding tools. The cursor + claude combo has genuinely made me more productive. But I was coding since before these tools existed. I had spent years debugging obscure errors, refactoring messy code, and building that intuition for what good code looks like. That foundation is why I can tell when cursor's suggestions are brilliant and when they're subtly broken.

I see people jumping straight to AI without that foundation, and honestly, it makes me a bit nervous for them. Not in a gatekeeping way - I'm genuinely excited about more people getting into coding. But there's a difference between using AI as a productivity booster and using it as a crutch to avoid learning.

When I use the tab feature, I already know what I want to build. The AI just saves me the typing. When I use cursor agent, I review every change it makes because I know what to look for. That's the difference.

Look, I'm not going to tell you how to learn. Maybe you'll figure out your own path that works better. But from where I'm standing, having gone through both worlds - the pre-AI grind and the AI-assisted present - the people who seem to struggle the most are the ones who skipped straight to step two.

The cursor + claude duo is incredible. But it's incredible *because* I know what I'm doing. Without that, it's just a fancy autocomplete that occasionally leads you off a cliff.

That's my experience anyway. Your mileage may vary.
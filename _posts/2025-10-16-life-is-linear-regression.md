---
layout: post
title: "Everything in Life is Linear Regression"
date: 2025-10-16
description: "Food for thought"
author: "Bejay"
acknowledgment: "Original thoughts, polished with a little help from <span style='color: #3182ce; font-weight: 500;'>Claude</span>."
---


When I started learning ML, I was first introduced to Linear Regression. In short, it describes an algorithm where you can model a function using a linear expression:

**y = wx + c**

Largely similar to the equation of a straight line. Here, the value of **y** (dependent variable) changes with **x** (independent variable).

Now, if we extrapolate this to multiple independent variables:

**y = w₁x₁ + w₂x₂ + ... + wₙxₙ + c**

In most use cases of linear regression, this is the case. An outcome or output is dependent on multiple factors.

Suppose you're modeling the house price of a city using linear regression. You'll find that historically, the price of a house depends on multiple factors — area, number of rooms, sq footage, parking (available or not), and so on. The Linear Regression algorithm tries to find those coefficients — w₁, w₂, ... wₙ — and we get a model (or equation) on which, if we feed in new values of x₁...xₙ, we can "predict" or "estimate" the cost of the house in question.

Now, the idea of this blog is not to deep dive into LR. It's because I seem to find a parallel between everything in life and this mathematical concept — not the linear part, but the **combination part** where everything is a combination of multiple things with different scaling factors associated with each of them.

---

### For example:

Suppose you missed a train on a certain day. You become extremely angry and start blaming your mom for apparently "making you late" by asking you to eat breakfast before leaving. But this is **black-and-white thinking** — sure, it might have played a role. But there are other factors here as well to consider. Like the fact that you slept late last night despite knowing you have a train to catch the next day. Also, the traffic at that time was more than usual.

If I were to put it in the equation:

**minutes_late = w₁(breakfast_delay) + w₂(woke_up_late) + w₃(traffic_level) + w₄(distance_to_station) + w₅(train_punctuality) + c**

Where:
- **minutes_late** = how many minutes late you arrived at the station (or how close you were to missing the train)
- **breakfast_delay** = time spent on breakfast (in minutes)
- **woke_up_late** = how late you woke up compared to planned time (in minutes)
- **traffic_level** = traffic congestion factor (could be 1-10 scale, or actual delay in minutes)
- **distance_to_station** = distance you need to travel (in km)
- **train_punctuality** = how early/late the train typically runs (in minutes)
- **c** = baseline constant (accounts for other unmeasured factors)

The weights (w₁, w₂, w₃, etc.) represent how much each factor contributes to the outcome. For instance:
- Maybe **w₂** is large because waking up late has a huge cascading effect
- **w₁** might be small because breakfast only added 5 minutes
- **w₃** could be moderate depending on how unpredictable traffic is

---

The more experiences I have in life, the more I resonate with this. 

Now, I know real linear regression has assumptions about linearity and independence that life often violates. But as a mental model for thinking about multiple factors contributing to outcomes, it works surprisingly well.

This also helps me approach differences in opinions in a calmer and composed manner. Let's say India wins a cricket match — some say it was because of Virat's ton. Some say it's because of Bumrah's fifer. Or some say it was because of Rohit's quickfire 25 off 10 balls.

I say **it's all of that**. Just with different weights.

---

### Another example:

Someone says, "They broke up because he was toxic."

But reality?

**relationship_strain = w₁(miscommunication) + w₂(incompatible goals) + w₃(external stress) + w₄(personality issues) + w₅(past baggage) + c**

We love single-factor explanations because they're simple. But life is **multivariate**, not binary.

---

Ever since I started viewing life through this lens — not the *linear* part of Linear Regression, but the *weighted combination* part — I've become less judgmental, more curious, and surprisingly more forgiving.

Because nothing "just happens."

**Outcome = Σ (all factors × their weights) + some randomness**

And most of us are just bad at estimating the weights.
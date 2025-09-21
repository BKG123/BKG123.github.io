---
layout: default
title: Blog
---

# 📝 Blog

Thoughts, experiments, and lessons from the journey.

<div class="blog-grid">
    {% for post in site.posts %}
    <div class="blog-card">
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p>{{ post.description | default: post.excerpt | strip_html | truncatewords: 25 }}</p>
        <small>Posted: {{ post.date | date: "%B %Y" }}</small>
    </div>
    {% endfor %}

    {% if site.posts.size == 0 %}
    <div class="blog-card">
        <h3>Welcome to the blog!</h3>
        <p>Posts will appear here as they're published.</p>
        <small>Stay tuned...</small>
    </div>
    {% endif %}
</div>
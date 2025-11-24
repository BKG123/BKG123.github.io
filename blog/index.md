---
layout: default
title: Blog
---

<div class="page-hero">
  <h1>Blog</h1>
  <p class="page-subtitle">Thoughts, experiments, and lessons from the journey of building intelligent systems.</p>
</div>

<div class="blog-grid-modern">
    {% for post in site.posts %}
    <article class="blog-card-modern">
        <div class="blog-card-header">
            <span class="blog-date">{{ post.date | date: "%b %d, %Y" }}</span>
            {% if post.tags and post.tags.size > 0 %}
                <span class="blog-tag">{{ post.tags[0] }}</span>
            {% endif %}
        </div>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p>{{ post.description | default: post.excerpt | strip_html | truncatewords: 25 }}</p>
        <a href="{{ post.url | relative_url }}" class="read-more">Read more →</a>
    </article>
    {% endfor %}

    {% if site.posts.size == 0 %}
    <article class="blog-card-modern">
        <h3>Welcome to the blog!</h3>
        <p>Posts will appear here as they're published.</p>
        <span class="read-more">Stay tuned...</span>
    </article>
    {% endif %}
</div>
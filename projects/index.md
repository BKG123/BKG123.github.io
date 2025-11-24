---
layout: default
title: "Projects"
---

<div class="projects-section">
  <div class="page-hero">
    <h1>Projects</h1>
    <p class="page-subtitle">A collection of things I've built while learning and experimenting with AI, backend systems, and innovative solutions.</p>
  </div>

  <div class="projects-grid">
    {% assign sorted_projects = site.projects | sort: 'date' | reverse %}
    {% for project in sorted_projects %}
    <div class="project-card">
      {% if project.thumbnail %}
      <div class="project-thumbnail">
        <img src="{{ project.thumbnail | relative_url }}" alt="{{ project.title }}">
      </div>
      {% endif %}

      <div class="project-card-content">
        <h2 class="project-card-title">
          <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
        </h2>

        {% if project.description %}
        <p class="project-card-description">{{ project.description }}</p>
        {% endif %}

        {% if project.tech_stack %}
        <div class="project-card-tech">
          {{ project.tech_stack }}
        </div>
        {% endif %}

        <div class="project-card-links">
          {% if project.links.demo %}
          <a href="{{ project.links.demo }}" target="_blank" class="project-card-link">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6M15 3h6v6M10 14L21 3"/>
            </svg>
            Demo
          </a>
          {% endif %}
          {% if project.links.github %}
          <a href="{{ project.links.github }}" target="_blank" class="project-card-link">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0C5.374 0 0 5.373 0 12 0 17.302 3.438 21.8 8.207 23.387c.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
            </svg>
            GitHub
          </a>
          {% endif %}
          <a href="{{ project.url | relative_url }}" class="project-card-link">
            Read More →
          </a>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
</div>

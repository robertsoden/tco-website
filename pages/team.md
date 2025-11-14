---
layout: default
title: Team
permalink: /team/
---

<section class="page-header">
    <div class="container">
        <h1>Our Team</h1>
    </div>
</section>

<section class="team-section">
    <div class="container">
        <h2>FACULTY</h2>
        <div class="team-grid">
            {% assign faculty = site.team | where: "category", "faculty" | sort: "order" %}
            {% for member in faculty %}
            <div class="team-member-card">
                {% if member.image %}
                <div class="member-image">
                    <img src="{{ member.image | relative_url }}" alt="{{ member.name }}">
                </div>
                {% endif %}
                <div class="member-info">
                    <h3>{{ member.name }}</h3>
                    {% if member.title %}
                    <p class="member-title">{{ member.title }}</p>
                    {% endif %}
                    <div class="member-bio">
                        {{ member.bio | truncatewords: 50 }}
                    </div>
                    <a href="{{ member.url | relative_url }}" class="read-more">Read More →</a>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <h2>GRADUATE STUDENTS & POST-DOCS</h2>
        <div class="team-grid">
            {% assign grads = site.team | where: "category", "graduate" | sort: "order" %}
            {% for member in grads %}
            <div class="team-member-card">
                {% if member.image %}
                <div class="member-image">
                    <img src="{{ member.image | relative_url }}" alt="{{ member.name }}">
                </div>
                {% endif %}
                <div class="member-info">
                    <h3>{{ member.name }}</h3>
                    {% if member.title %}
                    <p class="member-title">{{ member.title }}</p>
                    {% endif %}
                    <div class="member-bio">
                        {{ member.bio | truncatewords: 50 }}
                    </div>
                    <a href="{{ member.url | relative_url }}" class="read-more">Read More →</a>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <h2>RESEARCH ASSISTANTS</h2>
        <div class="team-grid">
            {% assign ras = site.team | where: "category", "research-assistant" | sort: "order" %}
            {% for member in ras %}
            <div class="team-member-card">
                {% if member.image %}
                <div class="member-image">
                    <img src="{{ member.image | relative_url }}" alt="{{ member.name }}">
                </div>
                {% endif %}
                <div class="member-info">
                    <h3>{{ member.name }}</h3>
                    {% if member.title %}
                    <p class="member-title">{{ member.title }}</p>
                    {% endif %}
                    <div class="member-bio">
                        {{ member.bio | truncatewords: 50 }}
                    </div>
                    <a href="{{ member.url | relative_url }}" class="read-more">Read More →</a>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <h2>ALUMNI</h2>
        <div class="team-grid">
            {% assign alumni = site.team | where: "category", "alumni" | sort: "order" %}
            {% for member in alumni %}
            <div class="team-member-card">
                {% if member.image %}
                <div class="member-image">
                    <img src="{{ member.image | relative_url }}" alt="{{ member.name }}">
                </div>
                {% endif %}
                <div class="member-info">
                    <h3>{{ member.name }}</h3>
                    {% if member.title %}
                    <p class="member-title">{{ member.title }}</p>
                    {% endif %}
                    <div class="member-bio">
                        {{ member.bio | truncatewords: 50 }}
                    </div>
                    <a href="{{ member.url | relative_url }}" class="read-more">Read More →</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>

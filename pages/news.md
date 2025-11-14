---
layout: page-with-sidebar
title: News & Updates
permalink: /news/
---

<section class="news-list">
    <div class="container">
        {% for post in site.posts %}
        <article class="news-article">
            <div class="article-meta">
                <time datetime="{{ post.date | date_to_xmlschema }}">
                    {{ post.date | date: "%B %d, %Y" }}
                </time>
            </div>

            <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>

            {% if post.image %}
            <div class="article-image">
                <a href="{{ post.url | relative_url }}">
                    <img src="{{ post.image | relative_url }}" alt="{{ post.title }}">
                </a>
            </div>
            {% endif %}

            <div class="article-excerpt">
                {{ post.excerpt }}
            </div>

            <a href="{{ post.url | relative_url }}" class="read-more">Read More →</a>
        </article>
        {% endfor %}
    </div>
</section>

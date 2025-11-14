---
layout: page
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

            ## <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            <div class="article-excerpt">
                {{ post.excerpt }}

            <a href="{{ post.url | relative_url }}" class="read-more">Read More →</a>
        </article>
        {% endfor %}

</section>

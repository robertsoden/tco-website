---
layout: page
title: Publications
permalink: /publications/
---

{% assign pubs = site.posts | where_exp: "p", "p.categories contains 'publication'" %}
{% assign by_year = pubs | group_by_exp: "p", "p.date | date: '%Y'" %}
{% for group in by_year %}
## {{ group.name }}

<ul class="publications-year">
{% for pub in group.items %}
  <li>
    {% assign suffix = " (" | append: group.name | append: ")" %}<a class="pub-title" href="{{ pub.url | relative_url }}">{{ pub.title | replace: suffix, "" }}</a>
    {% if pub.authors %}<span class="pub-authors">{{ pub.authors }}</span>{% endif %}
    {% if pub.venue %}<span class="pub-venue">{{ pub.venue }}</span>{% endif %}
    {% if pub.doi %}<a class="pub-doi" href="https://doi.org/{{ pub.doi }}">doi:{{ pub.doi }}</a>{% endif %}
  </li>
{% endfor %}
</ul>
{% endfor %}

---
layout: page
permalink: /call/
title: Call for Papers
nav: true
nav_order: 2
---

{% if site.data.workshop.backgrounds.light != "" or site.data.workshop.backgrounds.dark != "" %}

<style>
body {
  background-size: cover;
  background-position: right center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  {% if site.data.workshop.backgrounds.light != "" %}
  background-image: url("{{ site.data.workshop.backgrounds.light | relative_url }}");
  {% endif %}
}
{% if site.data.workshop.backgrounds.dark != "" %}
html[data-theme="dark"] {
  --global-bg-color: #000;
}
{% endif %}
html[data-theme="dark"] body {
  {% if site.data.workshop.backgrounds.dark != "" %}
  background-image: linear-gradient(rgba(0, 0, 0, 0.18), rgba(0, 0, 0, 0.18)), url("{{ site.data.workshop.backgrounds.dark | relative_url }}");
  {% else %}
  background-image: none;
  {% endif %}
}
{% if site.data.workshop.backgrounds.dark != "" %}
@media (max-width: 767px) {
  html[data-theme="dark"] body {
    background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("{{ site.data.workshop.backgrounds.dark | relative_url }}");
  }
}
{% endif %}
</style>

{% endif %}

{% if site.data.workshop.submission.released %}

We invite submissions to **{{ site.data.workshop.title }}**, a {{ site.data.workshop.status | downcase }} at {{ site.data.workshop.conference }}. We seek work on visually and physically intelligent foundation models, spanning perception, reasoning, generation, world modeling, planning, and robotic action.

### Important Dates

| Milestone                 | Date                                             |
| ------------------------- | ------------------------------------------------ |
| Paper submission deadline | {{ site.data.workshop.submission.deadline }}     |
| Acceptance notification   | {{ site.data.workshop.submission.notification }} |

All deadlines are **Anywhere on Earth (AoE, UTC−12)**. Workshop date and venue will be announced.

### Submission Guidelines

We welcome submissions of **up to {{ site.data.workshop.submission.pages }} pages, single column, excluding references**, including **tiny papers of one or two pages** presenting early-stage ideas, concise results, follow-up experiments, or reanalyses. We strongly encourage ongoing and novel work and open research questions that can contribute to discussion of emerging challenges.

Submissions must be **primarily human-authored**, reflecting original thought and analysis. AI assistance is permitted, but AI-generated papers are not allowed under ICLR's tiny/short-paper rules.

Shorter versions of recently published work are also welcome. Papers containing new or ongoing research will be prioritized for contributed talks. Work presented at the workshop may subsequently be submitted to another venue.

{% if site.data.workshop.submission.url != "" %}
[Submit through OpenReview]({{ site.data.workshop.submission.url }}).
{% else %}
The OpenReview submission portal and paper template will be announced here.
{% endif %}

### Review and Presentation

Each paper will be reviewed by **{{ site.data.workshop.submission.reviewers }} experienced reviewers**, with acceptance decisions made by the workshop program committee. All accepted papers will be presented as posters, and **{{ site.data.workshop.submission.contributed_talks }} papers** will be selected for contributed talks.

Authors will also give **one-minute lightning pitches** before the poster session. Authors will have the option to share accepted papers, posters, and short presentation videos on the workshop website.

### Topics

<ul>
{% for topic in site.data.topics %}
  <li><strong>{{ topic.name }}.</strong> {{ topic.description }}</li>
{% endfor %}
</ul>

### Contact

For questions about submissions, contact [{{ site.data.workshop.contact }}](mailto:{{ site.data.workshop.contact }}).

{% else %}

**Not released yet.**

The call for papers, submission guidelines, and deadlines will be announced here once the workshop is confirmed.

{% endif %}

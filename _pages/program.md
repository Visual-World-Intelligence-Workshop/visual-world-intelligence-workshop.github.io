---
layout: page
permalink: /program/
title: Program
nav: true
nav_order: 3
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

### Planned Schedule

We plan a **full day workshop** with invited and contributed talks, Q&A sessions, poster lightning pitches, a poster session, and a panel discussion. The workshop date, venue, and keynote assignments will be announced.

<table>
  <thead>
    <tr><th scope="col">Time</th><th scope="col">Session</th></tr>
  </thead>
  <tbody>
    {% for item in site.data.schedule %}
    <tr><td>{{ item.time }}</td><td>{{ item.session }}</td></tr>
    {% endfor %}
  </tbody>
</table>

Times are local to the workshop venue.

### Planned Speakers

<ul>
{% for speaker in site.data.speakers %}
  <li><a href="{{ speaker.url }}" target="_blank" rel="noopener noreferrer">{{ speaker.name }}</a>: {{ speaker.affiliation }}</li>
{% endfor %}
</ul>

### Planned Panelists

The panel brings together academic and industrial leaders to discuss the scientific and engineering path toward visual world intelligence. Audience questions will help guide the discussion.

<ul>
{% for panelist in site.data.panelists %}
  <li><a href="{{ panelist.url }}" target="_blank" rel="noopener noreferrer">{{ panelist.name }}</a>: {{ panelist.affiliation }}</li>
{% endfor %}
</ul>

### Posters and Participation

All accepted papers will be presented during the poster session, with four selected for contributed talks. Authors will give one-minute lightning pitches to introduce their work. Poster sessions will provide time for discussion and engagement without overlapping lunch.

The workshop will be held in person. Authors may share accepted papers, posters, and short presentation videos on the workshop website to support access beyond the event.

We anticipate **100–300 participants** and approximately **40 posters**.

### Workshop Outcomes

We plan to release a community report covering recurring themes from talk Q&As, posters, and the panel, together with open challenges and future research directions. Accepted authors may share papers, posters, and short presentation videos on this website to support access beyond the workshop day.

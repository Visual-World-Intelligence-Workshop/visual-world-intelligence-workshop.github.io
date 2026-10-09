---
layout: about
title: Home
permalink: /
subtitle: "Beyond Understanding and Generation"
selected_papers: false
social: false
announcements:
  enabled: false
  scrollable: true
  limit: 5
latest_posts:
  enabled: false
  scrollable: true
  limit: 3
---

<style>
.people-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin: 1rem 0 2rem;
  max-width: 712px;
}
.people-grid:not(.panelists-grid) {
  justify-content: center;
  margin-left: auto;
  margin-right: auto;
}
.people-grid.panelists-grid {
  max-width: 896px;
}
.person-card {
  width: 160px;
  text-align: center;
}
.person-card img,
.person-placeholder {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  display: block;
  margin: 0 auto;
  background: #e0e0e0;
}
.person-card .person-name {
  font-weight: 600;
  font-size: 0.9rem;
  margin-top: 0.5rem;
  display: block;
}
.person-card .person-affiliation {
  font-size: 0.8rem;
  color: #888;
  display: block;
}
.post-header {
  display: block;
  container-type: inline-size;
  margin-bottom: 1rem;
}
.post-header > .post-title,
.post-header > .desc {
  margin: 0;
  white-space: nowrap;
  overflow-wrap: normal;
  font-size: clamp(12px, 4.2cqi, 40px);
  font-weight: 300;
  letter-spacing: -0.02em;
}
.post-header > .post-title {
  font-weight: 400;
}
</style>

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

<p class="desc">{{ site.data.workshop.status }} at {{ site.data.workshop.conference }} &bull; Date and venue to be announced</p>

### Abstract

{{ site.data.workshop.abstract }}

### About the Workshop

{% for paragraph in site.data.workshop.overview %}

<p>{{ paragraph }}</p>
{% endfor %}

##### Topics

More specifically, the workshop will cover the following topics:

<ul>
{% for topic in site.data.topics %}
  <li><strong>{{ topic.name }}.</strong> {{ topic.description }}</li>
{% endfor %}
</ul>

---

### Planned Speakers

<div class="people-grid">
{% for speaker in site.data.speakers %}
<div class="person-card">
  {% if speaker.img and speaker.img != "" %}
  <img src="{{ speaker.img | relative_url }}" alt="{{ speaker.name }}" loading="lazy" decoding="async" width="100" height="100">
  {% else %}
  <div class="person-placeholder" aria-hidden="true"></div>
  {% endif %}
  <span class="person-name">{% if speaker.url and speaker.url != "" %}<a href="{{ speaker.url }}" target="_blank" rel="noopener noreferrer">{{ speaker.name }}</a>{% else %}{{ speaker.name }}{% endif %}</span>
  {% if speaker.affiliation and speaker.affiliation != "" %}<span class="person-affiliation">{{ speaker.affiliation }}</span>{% endif %}
</div>
{% endfor %}
</div>

---

### Planned Panelists

<div class="people-grid panelists-grid">
{% for panelist in site.data.panelists %}
<div class="person-card">
  {% if panelist.img and panelist.img != "" %}
  <img src="{{ panelist.img | relative_url }}" alt="{{ panelist.name }}" loading="lazy" decoding="async" width="100" height="100">
  {% else %}
  <div class="person-placeholder" aria-hidden="true"></div>
  {% endif %}
  <span class="person-name">{% if panelist.url and panelist.url != "" %}<a href="{{ panelist.url }}" target="_blank" rel="noopener noreferrer">{{ panelist.name }}</a>{% else %}{{ panelist.name }}{% endif %}</span>
  {% if panelist.affiliation and panelist.affiliation != "" %}<span class="person-affiliation">{{ panelist.affiliation }}</span>{% endif %}
</div>
{% endfor %}
</div>

---

### Organizers

Our organizing team brings together academic and industrial researchers at different career stages, with experience organizing workshops at CVPR, ICCV, ECCV, NeurIPS, ICLR, and FAccT. Their research spans multimodal foundation models, generative models, latent world models, perception, and benchmarking.

<div class="people-grid">
{% for organizer in site.data.organizers %}
<div class="person-card">
  {% if organizer.img and organizer.img != "" %}
  <img src="{{ organizer.img | relative_url }}" alt="{{ organizer.name }}" loading="lazy" decoding="async" width="100" height="100">
  {% else %}
  <div class="person-placeholder" aria-hidden="true"></div>
  {% endif %}
  <span class="person-name">{% if organizer.url and organizer.url != "" %}<a href="{{ organizer.url }}" target="_blank" rel="noopener noreferrer">{{ organizer.name }}</a>{% else %}{{ organizer.name }}{% endif %}</span>
  {% if organizer.affiliation and organizer.affiliation != "" %}<span class="person-affiliation">{{ organizer.affiliation }}</span>{% endif %}
</div>
{% endfor %}
</div>

---

### Participation

We plan a full day of invited and contributed talks, a panel, poster lightning pitches, and a poster session. Partial hybrid participation is planned, with details to be announced. We welcome ongoing research, early ideas, and open questions.

{% if site.data.workshop.submission.released %}

- **Paper submission deadline:** {{ site.data.workshop.submission.deadline }}.
- **Acceptance notification:** {{ site.data.workshop.submission.notification }}.

{% endif %}

Read the [Call for Papers]({{ '/call/' | relative_url }}) and [planned program]({{ '/program/' | relative_url }}).

### An Inclusive Community

We are committed to an inclusive and welcoming environment for participants from all backgrounds. The organizers, speakers, and panelists span academic institutions, industrial labs, and startups, with a range of nationalities, gender identities, expertise, and career stages. Their expertise includes visual reasoning, generative and latent world models, and robotics. We aim to support broad participation, diverse discussion, and collaborations across the visual intelligence community.

Contact the organizing team at [{{ site.data.workshop.contact }}](mailto:{{ site.data.workshop.contact }}).

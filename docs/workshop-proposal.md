# Visual World Intelligence: Beyond Understanding and Generation

Proposed workshop at ICLR 2027. The abstract, topic overview, six research tracks, biographies, submission guidelines, and tentative schedule are maintained in `_data/`. The public website shows the abstract, topics, planned participants, and program. Biographies are retained for proposal reference, and the call for papers remains unreleased.

## Invited speakers and panelists

The expertise of the invited speakers spans world modeling, robotics, perception, visual generation, and foundation models. Sherry Yang, Yuki Asano, Lucas Beyer, and Olga Russakovsky are all confirmed in the updated proposal. The public website continues to label all speakers and panelists as planned.

The panelists span perception and multimodal foundation models, world models, and robotics. Georgia Gkioxari, Akshara Rai, Terrance DeVries, Bill Peebles, and Jenny Seidenschwarz are confirmed. Full biographies and supplied OpenReview identifiers are preserved in `_data/speakers.yml` and `_data/panelists.yml`.

Bill Peebles's biography uses the approved wording: “Bill Peebles is a former research scientist at OpenAI, where he headed Sora, OpenAI's video generation and world simulation effort.”

## Organizers

The organizing team comprises academic and industrial researchers at different stages of their careers: Tim Rädsch, Adriana Romero-Soriano, Carsten Lüth, Zhang Xiaofeng, Michal Drozdzal, Ye Zhu, Nicolas Ballas, and Felix Friedrich. The team has experience organizing workshops and other events at CVPR, ICCV, ECCV, NeurIPS, ICLR, and FAccT, and a research record across multimodal foundation models, generative models, latent world models, perception, and benchmarking. Affiliations, email addresses, supplied OpenReview identifiers, and full biographies are preserved in `_data/organizers.yml`.

## Diversity commitment

The organizing committee has been intentionally curated to bring together a global and inclusive set of perspectives, supporting and promoting diversity and inclusion. Our team is composed of academic and industrial researchers representing a broad spectrum of backgrounds and career stages, including senior researchers, early-career scientists, and Ph.D. students. Our team also represents researchers with different backgrounds, nationalities, and gender identities. The organizing team has extensive experience organizing workshops and other events at top conferences such as ICLR, NeurIPS, and CVPR. Beyond its organizing experience, team members have a proven track record of research publications spanning all workshop tracks, including vision and multimodal generative models, latent world models, unified architectures, and benchmarking.

Our speaker and panelist lineup reflects a similar commitment to diversity across background, seniority, affiliations, nationality, gender identity, and expertise. The invited speakers bring diverse, international perspectives and include leaders from academic and industrial research labs. This diversity ensures a wide range of viewpoints on the field's technical and conceptual challenges. We have prioritized balanced gender representation and a mix of seniority levels, ranging from foundational pioneers to rising stars in visual reasoning, generative and latent world models, and robotics, and including academia, large industrial labs, and startups. Our ongoing efforts focus on ensuring an inclusive environment that welcomes participants from all backgrounds and encourages vibrant, diverse discussion.

We anticipate that diversity among organizers, speakers, and panelists will provide rich representation of different perspectives, creating an inclusive and welcoming environment for all participants.

## Related workshops

Visual intelligence research has largely advanced along two closely related but often separately organized directions: visual understanding and visual generation. On the understanding side, workshops such as [OpenSUN3D: Workshop on Open-World 3D Scene Understanding and Representations](https://opensun3d.github.io/) (ECCV 2026) and the [Workshop on 3D Scene Understanding for Vision, Graphics, and Robotics](https://scene-understanding.com/) (CVPR 2026) focus on visual perception, spatial representations, and scene understanding. On the generation side, workshops such as the [4th Workshop on Generative Models for Computer Vision](https://generative-vision.github.io/workshop-CVPR-26/) (CVPR 2026) and [Visual Generative Modeling: What's After Diffusion?](https://vgm-cvpr.github.io/) (CVPR 2025) explore advances in generative architectures and visual synthesis. While these directions increasingly interact, our proposed workshop takes a broader, complementary perspective. We aim to explore how understanding and generation can jointly enable visual world intelligence: models that build grounded, temporally coherent representations of the world, predict how it evolves, and use these predictions to support reasoning, planning, and interaction.

Recent workshops have increasingly explored visual intelligence, multimodal reasoning, and world models from complementary perspectives. The [ICLR 2025](https://sites.google.com/view/worldmodel-iclr2025/) and [ICLR 2026](https://sites.google.com/view/iclr-2026-workshop-world-model/home) World Models: Understanding, Modelling and Scaling workshops focused on learning, scaling, and applying world models, while the ICLR 2026 workshop on [Multimodal Intelligence: Next Token Prediction and Beyond](https://mmintelligence.github.io/) explored different modeling paradigms for multimodal foundation models. NeurIPS 2025 also featured several reasoning workshops, including [Foundations of Reasoning in Language Models](https://reasoning-workshop.github.io/), [Efficient Reasoning](https://efficient-reasoning.github.io/), and [Multimodal Algorithmic Reasoning](https://marworkshop.github.io/neurips25/), which primarily emphasized reasoning in language and multimodal models rather than reasoning through vision-first generative and predictive models. At CVPR 2026, [Visual General Intelligence](https://cvpr2026-vgi-workshop.limitlab.xyz/) explored the role of vision in the path toward general intelligence. More closely related, the ECCV 2026 workshops [UniWorld](https://uniworld-ai.github.io/) and [MUCG](https://mllm-mucg.github.io/ECCV2026/) explored unified visual representations and architectures integrating perception, reasoning, generation, and interaction, as well as synergistic learning between understanding and generation. Other workshops, including [Reliable and Interactable World Models](https://riwm-2025.github.io/RIWM-2025/) (ICCV 2025), [World Models in the Loop](https://eccv26woop.github.io/) (ECCV 2026), and [World Models in Physical AI](https://www.worldmodels-physicalai.com/) (NeurIPS 2026), emphasize physical consistency, interactivity, evaluation, and downstream decision making.

While visual understanding and generation have achieved impressive progress, success in these individual tasks does not necessarily imply that a model has acquired generalizable knowledge of the physical world. Such knowledge should support reasoning about physical dynamics and facilitate transferring learned capabilities to unfamiliar situations. Building on previous community efforts, our workshop focuses on a distinct scientific question: Does integrating different visual capabilities lead to genuinely generalizable visual world intelligence, or merely combine task-specific competencies within a single architecture?

We aim to critically examine when and why joint learning across perception, reasoning, generation, and action produces transferable capabilities. Does jointly learning visual understanding and generation enable new capabilities beyond those achieved independently? Is a unified architecture necessary, or can modular systems achieve comparable generalization? What evidence would allow us to recognize the emergence of general visual world intelligence? What benchmarks can distinguish transferable knowledge of the visual world from task-specific performance or distributional shortcuts?

By bringing together researchers across visual understanding, generative modeling, world models, and embodied intelligence, we aim to establish a common scientific agenda for defining, developing, and evaluating visual world intelligence beyond individual task performance.

## Format, logistics, and outcomes

This proposal is for a full-day workshop with a standard venue setting: a room with presentation equipment and seating for participants. The workshop plans for paper submissions and requires a poster area for approximately 40 posters.

The workshop will include invited and contributed talks, a panel, and a poster session. Talks will be followed by Q&A sessions, and poster sessions will ensure sufficient time for participant engagement while avoiding overlap with lunch. Before the poster session, authors will deliver one-minute lightning pitches to highlight their work's key contributions.

The panel will bring together industrial and academic leaders to discuss the scientific and engineering considerations of the path toward visual intelligence. Audience questions will guide the discussion.

The workshop will be held in person. Authors will have the option to share contributed content, including PDFs of accepted work, posters, and short presentation videos, on the website maintained by the co-organizers. This will provide access to workshop materials for those who cannot attend and facilitate dissemination beyond the workshop day.

We plan to release a report identifying recurring themes from talk Q&As, poster presentations, and the panel, together with key open challenges and future research directions. The report will sustain broader community engagement, build collaborations, and extend the workshop's impact beyond the event.

Anticipated audience size: **100–300 people**.

The planned schedule is maintained in `_data/schedule.yml`. Poster lightning pitches run from 11:45 to 12:30, allowing approximately 40 one-minute presentations and five minutes for transitions.

## Paper submission

We will comply with ICLR 2027's workshop requirements. We will adhere to ICLR 2027's participation limits: each organizer will be listed on no more than two workshop proposals and will disclose any other proposals they are helping organize; each speaker or panelist will be listed in no more than two distinct workshop proposals. By 26 February 2027, 11:59 pm AoE, we will notify contributors, make accepted papers publicly available on OpenReview, and import them into iclr.cc. Organizers will recuse themselves from reviewing and deciding on conflicted submissions, including those from the same organization; an unconflicted committee member will oversee these decisions. Organizers will not give workshop talks, except brief introductory remarks, and may moderate the panel.

We will set up an OpenReview platform for paper submission. Each paper will be reviewed by two to three experienced reviewers, and the workshop program committee will make acceptance decisions. All accepted papers will be presented during the poster session, and four will be selected for contributed talks.

We welcome submissions of up to four pages (single column), excluding references, including tiny papers of one or two pages presenting early-stage ideas, concise results, follow-up experiments, or reanalyses. We strongly encourage ongoing and novel work to promote discussion of emerging challenges and open research questions. Work presented at the workshop may also be submitted to another venue afterwards. Shorter versions of recently published work are welcome, while papers containing new or ongoing research will be prioritized for contributed talks.

Submissions must be primarily human-authored, reflecting original thought and analysis. AI assistance is permitted, but AI-generated papers are not allowed under ICLR's tiny/short-paper rules.

- Paper submission deadline: **1 February 2027, 11:59 pm AoE**.
- Acceptance notification: **26 February 2027, 11:59 pm AoE**.

## Advertising and audience outreach

To drive attendance, we will adopt a plan across the website, social media, and our networks.

- **Website:** We have published a preliminary workshop website at [https://visual-world-intelligence-workshop.github.io/](https://visual-world-intelligence-workshop.github.io/) with an overview, planned program, and speaker, panelist, and organizer profiles. Announcements, program highlights, and submission guidelines will be added as they become available.
- **Social media:** Create dedicated accounts and coordinate posts with topic teasers, announcements, countdowns, and submission links.
- **Networks:** Share the event on relevant mailing lists, including [ELLIS](https://ellis.eu), [WiML](https://www.wiml.org/), Machine Learning News, and [heidelberg.ai](http://heidelberg.ai) (3,000 members), as well as community groups and Slack channels.
- **Collaborators:** Partner with speakers, collaborators, and related institutions to share posts ahead of the event.

This document describes planned outreach; no messages have been sent or accounts created.

## Nominated reviewer

**Dr. Jakob Verbeek** — OpenReview: [~Jakob_Verbeek1](https://openreview.net/profile?id=~Jakob_Verbeek1).

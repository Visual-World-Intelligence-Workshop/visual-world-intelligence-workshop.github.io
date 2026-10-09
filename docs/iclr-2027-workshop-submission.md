# Visual World Intelligence: Beyond Understanding and Generation

**ICLR 2027 Workshop Proposal**

## Abstract

As large language models continue to demonstrate increasing capabilities across a broad variety of domains, current foundation models still lack comparable visual world intelligence, limiting their capacity to support the planning and forecasting abilities required to unlock the next revolution in physical AI. With this workshop, we aim to bring together diverse perspectives across academia and industry to discuss the path towards building visually and physically intelligent foundation models. These paths span video reasoning, omnimodal models, interleaved image-and-language generation, latent world models, or alternative paradigms.

## Topic

Visual world intelligence is an integrated faculty that allows us to perceive the world, reason about what we see, imagine potential futures, and use these representations to guide our actions. These capabilities are not isolated from one another; they are interconnected components that took millions of years to evolve into a single unity.

Recent foundation models have driven massive progress in areas like text and coding, demonstrating impressive capabilities and generalizability across tasks and domains. Yet visual foundation models tackle problems separately, and performance in visual world intelligence still lags far behind. For example, state-of-the-art video generation models generate compelling content that often violates the rules that govern the physical world. Vision-language models reason about visual content but struggle with fine-grained spatial geometry and scene dynamics. Robotics systems often rely on task-specific representations that fail to generalize across domains. To move beyond these fragmented paradigms, we must re-evaluate how visual world intelligence is built. What representations are required to generate physically grounded videos, reason over complex spatial dynamics, and enable transferable robotic control simultaneously? And can solving these challenges result in an analogous breakthrough to that of large language models for the visual world?

This workshop aims to address a fundamental question: Can a unified visual world intelligence emerge directly from visual data, and how can we detect its arrival? Can unified systems that jointly perceive scenes, generate plausible futures, reason, and control robotic actions exhibit general capabilities that transcend those obtained by current task-specific visual foundation models? Do these systems capture a unified visual representation that unlocks new levels of generalization? Or is the future of visual world intelligence fundamentally modular, requiring orchestration across specialized components?

A major difference in achieving visual and text intelligence lies in the nature of the data, making the LLM analogy non-trivial. Unlike language, which has an abstract structure established in a discrete symbolic system, the physical world, and our visual perception of it, is continuous and governed by dynamic, causal, and spatial constraints. We currently lack the conceptual frameworks to define unified visual world intelligence and the evaluation tools to measure it.

This workshop brings together researchers across perception, generative systems, latent world modeling, spatial reasoning, and physical AI to stress-test existing paradigms, identify fundamental challenges, and build the path toward true visual world intelligence in silico.

More specifically, the workshop will cover the following topics:

**Visual Reasoning.** Do current systems reason about the visual world or exploit distributional shortcuts? Can a system that reasons well in language transfer that capacity to visual inference? What would purely visual reasoning look like in the absence of language scaffolding?

**Evaluation and Benchmarking.** Existing benchmarks were designed for single-task models. What tasks, metrics, and protocols are needed to evaluate whether a system's visual capabilities are genuinely unified, i.e., mutually consistent and grounded, rather than separately capable? What would a "visual Turing test" for emergence look like?

**Video Generative Models.** Generative models as a probe for understanding: if a model can generate physically plausible, temporally coherent video, does that imply an internal world model? What failure modes reveal the absence of genuine understanding beneath surface-level generation quality?

**Latent World Models.** World models that operate over learned representations, e.g., JEPA-style approaches, have already demonstrated physics understanding and the ability to solve tasks through planning. Yet these approaches remain prone to representation collapse, and while several losses have been proposed to prevent it, no consensus has emerged. How latent world models behave at scale also remains an open question.

**Unified Multimodal Architectures.** Joint models over perception, language, and generation: which architectural choices are necessary conditions for enabling emergence of widely applicable visual intelligence? What does the gap between current unified models and human visual cognition reveal?

**Visual Perception and Cognition for Robotics.** Vision-Language-Action models provide a unique testbed: physical grounding exposes failures that purely perceptual or generative evaluations miss. Does embodiment accelerate or constrain the path toward unified visual intelligence?

## Invited Speakers and Panelists

### Invited Speakers

The expertise of the speakers spans important areas covered by the workshop proposal, namely world modeling, robotics, perception, visual generation, and foundation models. Detailed biographies of all speakers are provided below.

#### Prof. Sherry Yang

OpenReview: [~Sherry_Yang1](https://openreview.net/profile?id=~Sherry_Yang1). **Confirmed.**

Sherry Yang is an Assistant Professor at NYU Courant and a Staff Research Scientist at Google DeepMind. Her research is in machine learning with a focus on reinforcement learning and generative modeling. Recently, she is interested in problems at the intersection of foundation models and decision making, such as learning world models and agents, and their applications in robotics and AI for science. Prior to this, she was a postdoctoral researcher at Stanford working with Percy Liang. Sherry obtained her Ph.D. from UC Berkeley advised by Pieter Abbeel, and her B.S. and M.Eng. from MIT.

#### Prof. Yuki Asano

OpenReview: [~Yuki_M_Asano1](https://openreview.net/profile?id=~Yuki_M_Asano1). **Confirmed.**

Yuki Asano is the head of the Fundamental AI (FunAI) Lab and full Professor at the University of Technology Nuremberg. Prior to this, he led the QUVA lab at the University of Amsterdam, where he closely collaborated with Qualcomm AI Research. Prof. Asano completed his Ph.D. at the Visual Geometry Group (VGG) at the University of Oxford, where he worked with Andrea Vedaldi and Christian Rupprecht.

#### Dr. Lucas Beyer

OpenReview: [~Lucas_Beyer1](https://openreview.net/profile?id=~Lucas_Beyer1). **Confirmed.**

Lucas grew up in Belgium wanting to make video games and their AI. He went on to study mechanical engineering at RWTH Aachen in Germany, where he also did a Ph.D. in robotic perception and computer vision. He later joined Google Brain in Zürich, which became part of Google DeepMind, and then helped start OpenAI's Zürich office. He is now at Meta in Zürich, where he continues to research multimodal AI.

#### Prof. Olga Russakovsky

OpenReview: [~Olga_Russakovsky1](https://openreview.net/profile?id=~Olga_Russakovsky1). **Confirmed.**

Olga Russakovsky is an Associate Professor in the Computer Science Department at Princeton University. Her research is in computer vision, closely integrated with the fields of machine learning, human-computer interaction, and fairness, accountability and transparency. She has been awarded the PAMI Young Researcher Award, the NSF CAREER award, AnitaB.org's Emerging Leader Abie Award in honor of Denice Denton, the CRA-WP Anita Borg Early Career Award, the MIT Technology Review's 35-under-35 Innovator award, the PAMI Everingham Prize, and the Foreign Policy Magazine's 100 Leading Global Thinkers award. In addition to her research, she co-founded and continues to serve on the Board of Directors of the AI4ALL nonprofit dedicated to increasing diversity and inclusion in Artificial Intelligence (AI). She completed her Ph.D. at Stanford University and her postdoctoral fellowship at Carnegie Mellon University. She served as program chair for ECCV 2024.

### Panelists

The expertise of the proposed panelists spans topics covered in this workshop, from perception and multimodal foundation models to world models and robotics. Detailed biographies of all panelists are provided below.

#### Prof. Georgia Gkioxari

OpenReview: [~Georgia_Gkioxari1](https://openreview.net/profile?id=~Georgia_Gkioxari1). **Confirmed.**

Georgia Gkioxari is an Assistant Professor in the Computing & Mathematical Sciences department at Caltech. Previously, she was a research scientist at Meta's FAIR team. She completed her Ph.D. at UC Berkeley with Jitendra Malik and her undergraduate studies at NTUA, Greece, where she worked with Petros Maragos. Georgia is a Packard Fellow (2025), the recipient of the PAMI Young Researcher Award (2021), a Google Faculty Award (2024), the Okawa Research Award (2024), and the Amazon Research Award (2024). Her teammates and she received the PAMI Mark Everingham Award (2021) for the Detectron Library Suite. She was named one of 30 influential women advancing AI in 2019 by ReWork and was nominated for the Women in AI Awards in 2020 by VentureBeat.

#### Dr. Akshara Rai

OpenReview: [~Akshara_Rai1](https://openreview.net/profile?id=~Akshara_Rai1). **Confirmed.**

Akshara Rai is a co-founder and Chief Scientist at Versor, tackling some of the fundamental challenges in robotics through real2sim2real. Previously, she was a research scientist at Meta AI, working at the intersection of machine learning and control for robotics. Her research aims at teaching robots to perform complex, novel tasks in very few trials, by utilizing simulators, physics-based models, or demonstration data. Before joining Meta AI, she finished her Ph.D. at the Robotics Institute, Carnegie Mellon University in 2018, working with Prof. Christopher G. Atkeson on utilizing simulations to learn locomotion on bipedal robots.

#### Dr. Terrance DeVries

OpenReview: [~Terrance_DeVries1](https://openreview.net/profile?id=~Terrance_DeVries1). **Confirmed.**

Terrance DeVries is a founding research scientist at Luma AI, where he works on advancing the capabilities of visual AI and bringing new technologies into practical use. He has contributed to some of the earliest applications of NeRF-based 3D capture, mobile neural rendering, 3D asset generation, and diffusion transformer-based video generation. His recent work includes developing HDR video generation for Luma AI's Ray3 model and exploring foundation models for robotics and spatial intelligence. He received his Ph.D. from the University of Guelph, where he was advised by Prof. Graham Taylor.

#### Dr. Bill Peebles

OpenReview: [~William_Peebles1](https://openreview.net/profile?id=~William_Peebles1). **Confirmed.**

Bill Peebles is a former research scientist at OpenAI, where he headed Sora, OpenAI's video generation and world simulation effort. Previously, he completed his Ph.D. at Berkeley AI Research advised by Alyosha Efros. Before that, he did his undergraduate studies at MIT, where he was advised by Antonio Torralba. He has interned at FAIR, Adobe Research, and NVIDIA. During his Ph.D., he was supported by the National Science Foundation's Graduate Research Fellowship Program.

#### Dr. Jenny Seidenschwarz

OpenReview: [~Jenny_Seidenschwarz1](https://openreview.net/profile?id=~Jenny_Seidenschwarz1). **Confirmed.**

Jenny Seidenschwarz is a Research Scientist at Odyssey, where she specializes in dynamic generative world modeling for physical AI. Her research focuses on action-conditioned, multimodal world modeling as well as multi-agent reinforcement learning. Recently, she is interested in in-the-loop training of agents with world models and enhancing the world models' underlying reasoning capabilities. Prior to her current role, she completed her Ph.D. at TUM advised by Dr. Laura Leal-Taixé, with research visits at CMU with Prof. Deva Ramanan and at NVIDIA.

## Organizers

The organizing team is composed of academic and industrial researchers at different stages of their careers. The organizing team has extensive experience in organizing workshops and other events at top-tier conferences such as CVPR, ICCV, ECCV, NeurIPS, ICLR, and FAccT. Beyond its organizing experience, team members also have a proven track record of research on topics related to multimodal foundation models, generative models, latent world models, perception, and benchmarking. Below is a detailed background description of all team members.

### Tim Rädsch

**OpenReview:** [~Tim_Rädsch1](https://openreview.net/profile?id=~Tim_R%C3%A4dsch1)

**Affiliation:** Technical University of Munich, Anates Labs

**Email:** [tim.raedsch@tum.de](mailto:tim.raedsch@tum.de)

**Short Bio:** Tim Rädsch is a postdoctoral-level researcher at the Technical University of Munich and co-founder of Anates Labs. His work focuses on data-centric AI, visual intelligence, machine learning evaluation, and trustworthy computer vision systems. He previously led a 25-person data engineering team at understandAI, co-organized the community-wide ASAM OpenLABEL standard and the KiTS23 challenge, and now works on scalable evaluation and physical reasoning for generative video and multimodal foundation models. His research has appeared at Nature Machine Intelligence, Nature Methods, CVPR, ECCV, FAccT, and NeurIPS.

### Adriana Romero-Soriano

**OpenReview:** [~Adriana_Romero-Soriano1](https://openreview.net/profile?id=~Adriana_Romero-Soriano1)

**Affiliation:** Meta FAIR, McGill University, Mila – Québec AI Institute

**Email:** [adriana.romero-soriano@mila.quebec](mailto:adriana.romero-soriano@mila.quebec)

**Short Bio:** Adriana Romero-Soriano is a Research Scientist at Meta FAIR, an Adjunct Professor at McGill University, a core industrial member of Mila, and the recipient of a Canada CIFAR AI Chair. Adriana's research sits at the intersection of computer vision, generative modeling, and representation learning. Her work appears regularly in top-tier venues (NeurIPS, ICLR, ICML, CVPR, ICCV) and has gathered over 60k citations. Her contributions earned her recognition as an influential woman advancing AI in 2019 by ReWork. Adriana is also an active member of the AI community: she has co-organized numerous workshops at top-tier conferences, including the ReGenAI workshop at CVPR (2024–2025) and sessions on the Science and Engineering of Deep Learning and Graph Representation Learning at NeurIPS and ICLR (2019, 2021). Adriana earned her Ph.D. from the University of Barcelona under the supervision of Dr. Carlo Gatta, followed by a postdoctoral fellowship at Mila with Prof. Yoshua Bengio.

### Carsten Lüth

**OpenReview:** [~Carsten_T.\_Lüth1](https://openreview.net/profile?id=~Carsten_T._L%C3%BCth1)

**Affiliation:** Anates Labs

**Email:** [carsten@anates.ai](mailto:carsten@anates.ai)

**Short Bio:** Carsten Lüth is a machine learning researcher specializing in evaluation methodology and empirical rigor for deep learning systems. He is currently focusing on evaluating generative video and world models. During his Ph.D., he identified and addressed systematic evaluation flaws across active learning, uncertainty estimation, and selective classification for vision tasks. More concretely, he built the largest empirical active learning benchmark for 3D biomedical image segmentation (150k GPU hours). He has published 10 papers at top venues, including two ICLR Orals, one NeurIPS Spotlight, one MICCAI STAR Award, and one CVPR Highlight as last author, with 800+ personal citations. He acted as a core maintainer of nnU-Net (8k+ GitHub stars) and was a leading organizer of heidelberg.ai (3,000+ members), one of the largest AI communities in Germany, hosting regular events with speakers including creators of AlphaFold, Stable Diffusion, and leading European LLMs.

### Zhang Xiaofeng

**OpenReview:** [~Zhang_Xiaofeng1](https://openreview.net/profile?id=~Zhang_Xiaofeng1)

**Affiliation:** Mila, Université de Montréal

**Email:** [xiaofeng.zhang@mila.quebec](mailto:xiaofeng.zhang@mila.quebec)

**Short Bio:** Zhang Xiaofeng is a Ph.D. student at Université de Montréal and Mila, advised by Aaron Courville, and recently completed a visiting research position at Meta FAIR. His research focuses on generative modeling and representation learning, with a particular interest in how generative models can better represent and learn the structure of real visual data. More broadly, his research aims to advance visual intelligence by grounding generative models in the statistical structure, diversity, and physical regularities of the visual world. His work has appeared at ICLR, NeurIPS, CVPR, and EMNLP. He is also an organizer of the World Modeling Workshop and co-organizes the Mila World Models Reading Group.

### Michal Drozdzal

**OpenReview:** [~Michal_Drozdzal1](https://openreview.net/profile?id=~Michal_Drozdzal1)

**Affiliation:** Meta

**Email:** [mdrozdzal@meta.com](mailto:mdrozdzal@meta.com)

**Short Bio:** Michal Drozdzal is a Research Scientist at the Fundamental AI Research lab at Meta. Michal's research sits at the intersection of vision generative models and representation learning. His work has appeared in top-tier venues such as ICLR, NeurIPS, ICML, CVPR, and ICCV and has been cited more than 14k times. Michal is an active member of the AI community; he regularly serves as Area Chair and reviewer for top-tier venues. Michal co-organized the ReGenAI workshop at CVPR (2024–2025) and served as a senior Program Chair for the 2024 Montreal AI Symposium. Michal earned his Ph.D. from the University of Barcelona under the supervision of Prof. Petia Radeva.

### Ye Zhu

**OpenReview:** [~Ye_Zhu3](https://openreview.net/profile?id=~Ye_Zhu3)

**Affiliation:** CNRS, École Polytechnique, Institut Polytechnique de Paris

**Email:** [ye.zhu@polytechnique.edu](mailto:ye.zhu@polytechnique.edu)

**Short Bio:** Ye Zhu is an Assistant Professor and Principal Investigator at the Department of Computer Science and the Laboratoire d'Informatique (LIX) at École Polytechnique. Her research focuses on generative models and computer vision, with applications to multimodal learning and physical systems, as well as on sampling and control techniques for fine-grained generation. Her work has appeared at major machine learning and computer vision venues, including NeurIPS, ICML, ICLR, CVPR, ECCV, and ICCV, and she has served as an Area Chair for major conferences in these fields. She is also an ELLIS member and Hi!Paris Chair. Before joining École Polytechnique in 2025, she was a postdoctoral researcher at Princeton University. She co-organizes workshops at top-tier conferences, including the ReGenAI workshop (CVPR 2024–2025) and CV4Science workshop (CVPR 2025–2026).

### Nicolas Ballas

**OpenReview:** [~Nicolas_Ballas1](https://openreview.net/profile?id=~Nicolas_Ballas1)

**Affiliation:** AMI Labs

**Email:** [nicolas.ballas@amilabs.xyz](mailto:nicolas.ballas@amilabs.xyz)

**Short Bio:** Nicolas Ballas is a researcher at AMI Labs, where he works on end-to-end world models. He spent the previous decade at Meta FAIR, where he was a core contributor to the JEPA research, including I-JEPA, V-JEPA, and V-JEPA 2, a family of self-supervised models that learn to predict in latent space and have demonstrated physical understanding and planning from video alone. His broader work spans self-supervised representation learning, video understanding, and the scaling of predictive architectures.

### Felix Friedrich

**OpenReview:** [~Felix_Friedrich1](https://openreview.net/profile?id=~Felix_Friedrich1)

**Affiliation:** Black Forest Labs

**Email:** [felix@blackforestlabs.ai](mailto:felix@blackforestlabs.ai)

**Short Bio:** Felix Friedrich is a Researcher at Black Forest Labs in Freiburg, Germany, where he conducts fundamental research on generative multimodal models, with a focus on RL post-training, robotics, and AI safety. His work centers on both advancing these systems and ensuring their responsible deployment. Previously, he was a postdoctoral researcher at Meta FAIR in Montreal, working on RL post-training for generative models and V-JEPA as a physics reward model.

## Diversity Commitment: Speakers, Panelists, and Organizers

The organizing committee has been intentionally curated to bring together a global and inclusive set of perspectives, supporting and promoting diversity and inclusion. Our team is composed of academic and industrial researchers representing a broad spectrum of backgrounds and career stages, including senior researchers, early-career scientists, and Ph.D. students. Our team also represents researchers with different backgrounds, nationalities, and gender identities. The organizing team has extensive experience in organizing workshops and other events at top-tier conferences such as ICLR, NeurIPS, and CVPR. Beyond its organizing experience, team members also have a proven track record of research publications on topics spanning all tracks of the proposed workshop, including vision and multimodal generative models, latent world models, unified architectures, and benchmarking.

Our speaker and panelist lineup reflects a similar commitment to diversity across background, seniority, affiliations, nationality, gender identity, and expertise. The invited speakers bring diverse, international perspectives and include leaders from both academic and industrial research labs. This diversity ensures a wide range of viewpoints on the technical and conceptual challenges of the field. We have prioritized balanced gender representation and a mix of seniority levels, ranging from foundational pioneers to rising stars in visual reasoning, generative and latent world models, and robotics, and including academia, large industrial labs, and startups. Our ongoing efforts continue to focus on ensuring an inclusive environment that welcomes participants from all backgrounds and encourages vibrant, diverse discussion.

We anticipate that diversity among organizers, speakers, and panelists will provide rich representation of different perspectives, creating an inclusive and welcoming environment for all participants.

## Related Workshops

Visual intelligence research has largely advanced along two closely related but often separately organized directions: visual understanding and visual generation. On the understanding side, workshops such as OpenSUN3D: Workshop on Open-World 3D Scene Understanding and Representations (ECCV 2026) and the Workshop on 3D Scene Understanding for Vision, Graphics, and Robotics (CVPR 2026) focus on visual perception, spatial representations, and scene understanding. On the generation side, workshops such as the 4th Workshop on Generative Models for Computer Vision (CVPR 2026) and Visual Generative Modeling: What's After Diffusion? (CVPR 2025) explore advances in generative architectures and visual synthesis. While these directions are increasingly interacting, our proposed workshop takes a broader, complementary perspective. Rather than treating understanding and generation as ends in themselves, we aim to explore how they can jointly enable visual world intelligence: models that build grounded, temporally coherent representations of the world, predict how it evolves, and use these predictions to support reasoning, planning, and interaction.

Building on these developments, recent workshops have increasingly explored visual intelligence, multimodal reasoning, and world models from complementary perspectives. The ICLR 2025 and ICLR 2026 World Models: Understanding, Modelling and Scaling workshops focused on learning, scaling, and applying world models, while the ICLR 2026 workshop on Multimodal Intelligence: Next Token Prediction and Beyond explored different modeling paradigms for multimodal foundation models. NeurIPS 2025 also featured several reasoning workshops (e.g., Foundations of Reasoning in Language Models, Efficient Reasoning, and Multimodal Algorithmic Reasoning), which primarily emphasized reasoning in language and multimodal models rather than reasoning through vision-first generative and predictive models. At CVPR 2026, Visual General Intelligence explored the role of vision in the path toward general intelligence. More closely related, the ECCV 2026 workshops UniWorld and MUCG explored unified visual representations and architectures that integrate perception, reasoning, generation, and interaction, as well as synergistic learning between understanding and generation. Other workshops, including Reliable and Interactable World Models (ICCV 2025), World Models in the Loop (ECCV 2026), and the planned World Models in Physical AI workshop (NeurIPS 2026), emphasize physical consistency, interactivity, evaluation, and downstream decision making.

While visual understanding and generation have achieved impressive progress, success in these individual tasks does not necessarily imply that a model has acquired generalizable knowledge of the physical world. Such knowledge should support reasoning about physical dynamics and facilitate transferring learned capabilities to unfamiliar situations. Building on previous efforts of the community, our workshop focuses on a distinct scientific question: Does integrating different visual capabilities lead to genuinely generalizable visual world intelligence, or merely combine task-specific competencies within a single architecture?

Rather than assuming that unified models are necessarily superior, we aim to critically examine when and why joint learning across perception, reasoning, generation, and action produces transferable capabilities. Does jointly learning visual understanding and generation enable new capabilities beyond those achieved independently? Is a unified architecture necessary, or can modular systems achieve comparable generalization? Crucially, what evidence would allow us to recognize the emergence of general visual world intelligence? What benchmarks can distinguish transferable knowledge of the visual world from task-specific performance or distributional shortcuts?

By bringing together researchers across visual understanding, generative modeling, world models, and embodied intelligence, we aim to establish a common scientific agenda for defining, developing, and evaluating visual world intelligence beyond individual task performance.

## Format, Logistics, and Outcomes

This proposal is for a full-day workshop with a standard venue setting, i.e., a room with presentation equipment and seats for participants. The workshop plans for paper submissions and would require a poster area for approximately 40 posters.

The workshop will include invited and contributed talks, a panel, and a poster session. To generate discussion, talks will be followed by Q&A sessions, and poster sessions will ensure sufficient time for participant engagement while avoiding overlap with lunchtime. Moreover, prior to the poster session, authors will deliver one-minute lightning pitches to highlight the key contributions of their work.

We envision the panel discussion bringing together industrial and academic leaders to discuss the scientific and engineering considerations of the path towards visual intelligence. The panel will encourage additional engagement with participants by allowing questions from the audience to guide the discussion.

The workshop will be held in person. Authors will have the option to share contributed content, including PDFs of accepted work, posters, and short presentation videos, on the workshop website, which will be maintained by the co-organizers. This will provide access to workshop materials for those who cannot attend and facilitate dissemination beyond the workshop day.

We plan to release a report on the event, which will identify emerging recurring themes from the discussion sessions (talk Q&As, poster presentations, and panel). The purpose of this report is to highlight the main discussion points and identify key open challenges and future research directions in the field. The report's goal will be to sustain broader community engagement, build collaborations, and extend the impact of the workshop beyond this event.

**Anticipated audience size:** 100–300 people.

### Planned Schedule

A planned schedule is presented below. Times are local to the workshop venue. The 45-minute lightning-pitch session accommodates approximately 40 one-minute pitches, with five minutes available for transitions.

| Time        | Session                  |
| ----------- | ------------------------ |
| 09:00–09:15 | Opening remarks          |
| 09:15–09:45 | Keynote 1                |
| 09:45–10:00 | Contributed talk 1       |
| 10:00–10:45 | Coffee break             |
| 10:45–11:15 | Keynote 2                |
| 11:15–11:30 | Contributed talk 2       |
| 11:30–11:45 | Contributed talk 3       |
| 11:45–12:30 | Poster lightning pitches |
| 12:30–13:30 | Lunch break              |
| 13:30–14:00 | Keynote 3                |
| 14:00–15:00 | Poster session           |
| 15:00–15:30 | Coffee break             |
| 15:30–16:00 | Keynote 4                |
| 16:00–16:15 | Contributed talk 4       |
| 16:15–17:00 | Panel                    |
| 17:00–17:10 | Closing remarks          |

## Paper Submission

We will comply with ICLR 2027's workshop requirements. We will adhere to ICLR 2027's participation limits: each organizer will be listed on no more than two workshop proposals and will disclose any other proposals they are helping organize; each speaker or panelist will be listed in no more than two distinct workshop proposals. By 26 February 2027, 11:59 pm AoE, we will notify contributors, make accepted papers publicly available on OpenReview, and import them into iclr.cc. Organizers will recuse themselves from reviewing and deciding on conflicted submissions, including those from the same organization; an unconflicted committee member will oversee these decisions. Organizers will not give workshop talks, except brief introductory remarks, and may moderate the panel.

We will set up an OpenReview platform to enable paper submission. Each paper will be reviewed by two to three experienced reviewers, and the acceptance decision will be made by the workshop program committee. All accepted papers will be presented during the poster session, and four will be selected for contributed talks.

We welcome submissions of up to four pages (single column), excluding references, including tiny papers of one or two pages presenting early-stage ideas, concise results, follow-up experiments, or reanalyses. We strongly encourage the submission of ongoing and novel work to promote discussion of emerging challenges and open research questions, and to ensure the workshop remains primarily for forward-looking research discussions. Works presented at the workshop may also be submitted to a different venue afterwards. Although submitted work may also include shorter versions of recently published work, papers containing new or ongoing research will be prioritized for contributed talks.

Submissions must be primarily human-authored, reflecting original thought and analysis. AI assistance is permitted, but AI-generated papers are not allowed under ICLR's tiny/short-paper rules.

### Paper Review Timeline

- **Paper submission deadline:** 1 February 2027, 11:59 pm AoE.
- **Acceptance notification:** 26 February 2027, 11:59 pm AoE.

## Plan to Attract an Audience: Advertising and Outreach

To attract an audience and drive attendance, we will adopt a multi-channel advertising plan across our website, social media, and networks.

**Website:** We have published a preliminary workshop website at [https://visual-world-intelligence-workshop.github.io/](https://visual-world-intelligence-workshop.github.io/) with an overview, planned program, and speaker, panelist, and organizer profiles. Announcements, program highlights, and paper submission guidelines will be added as they become available.

**Social media:** We will create dedicated social media accounts and coordinate posts with topic teasers, important announcements, countdowns, and submission links.

**Networks:** We will post about the event on relevant mailing lists (e.g., ELLIS, WiML, Machine Learning News, and heidelberg.ai, with 3,000 members), relevant community groups, and Slack channels to increase awareness and engagement. We will partner with collaborators, speakers, and related institutions to share posts ahead of the event.

## Nominated Reviewer

**Dr. Jakob Verbeek**

**OpenReview:** [~Jakob_Verbeek1](https://openreview.net/profile?id=~Jakob_Verbeek1)

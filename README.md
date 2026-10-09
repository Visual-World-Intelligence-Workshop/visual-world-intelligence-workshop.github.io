# Visual World Intelligence

**Beyond Understanding and Generation — proposed ICLR 2027 workshop**

This site adapts the [Visual Intelligence Workshop website](https://github.com/Visual-Intelligence-Workshop/visual-intelligence-workshop.github.io), retaining its al-folio theme, typography, layout, circular profile cards, and light/dark modes. The original MIT license is retained in `LICENSE`.

## Content

- `_data/workshop.yml`: workshop title, abstract, overview, conference, status, submission dates, contact, and background images.
- `_data/topics.yml`: the six research topics, shared by the home page and call for papers.
- `_data/speakers.yml`, `_data/panelists.yml`, `_data/organizers.yml`: affiliations, biographies, profiles, planned participation status, and portraits.
- `_data/schedule.yml`: planned full-day program.
- `_pages/about.md`: home page.
- `_pages/call.md`: “Not released yet” until `submission.released` is set to `true` in `_data/workshop.yml`; the planned guidelines and dates are retained for publication.
- `_pages/program.md`: schedule, participation, and planned outcomes.
- `docs/workshop-proposal.md`: proposal material, including related workshops, diversity, outreach, and nominated reviewer.

The revised morning schedule has no gaps, with poster lightning pitches from 11:45 to 12:30. Each pitch is one minute, allowing approximately 40 presentations and five minutes for transitions. All speakers and panelists are presented as planned. Biographies are retained in the data files for reference and are not displayed on the website. No workshop acceptance, venue, date, paper template, or OpenReview submission URL has been assumed.

## Background images and portraits

Upload your images into `assets/img/`, then set `backgrounds.light` and `backgrounds.dark` in `_data/workshop.yml` to their relative paths, for example `assets/img/background-light.jpg` and `assets/img/background-dark.jpg`. The existing light/dark switch selects the corresponding background. The dark background uses the supplied aperture-of-light artwork, resized to 2560 pixels wide and compressed as a JPEG. The light background is awaiting an image. Select dark mode with the theme toggle to see the artwork. On smaller screens, the background is dimmed to keep text readable.

For each person, set `img` in their data file to a portrait path. Portrait files are compressed 300 × 300 JPEGs, displayed in the original 100 × 100 circles and loaded lazily. Portraits are available for all 17 speakers, panelists, and organizers. The previous workshop's affiliation logo montage is not displayed because it represents the old organizing team.

## Local development

An initial static preview is available at `_site/index.html`; open it in a browser. It was rendered from the current content using Liquid and Kramdown with the original published theme's CSS and JavaScript. It includes the call for papers and program. This preview is generated output, is ignored by Git, and is replaced by the next Jekyll build.

Use **Ruby 3.3 or later**, Bundler **4.0.6**, Node.js, and ImageMagick for responsive image generation. Then:

```sh
bundle config set --local path vendor/bundle
bundle install
npm ci
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000/`. Jekyll rebuilds content changes automatically; restart after editing `_config.yml`.

## Publishing

The prepared organization name is `visual-world-intelligence-workshop`, with a public repository named `visual-world-intelligence-workshop.github.io`. Its website URL is `https://visual-world-intelligence-workshop.github.io/`. If a different organization name is chosen, update `url` in `_config.yml` and use the matching `<organization>.github.io` repository name. Keep `baseurl` empty for an organization site.

Create the free organization at <https://github.com/organizations/new>, then create the public repository and upload the source to `main`. In **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**. The `.github/workflows/deploy.yml` workflow builds Jekyll and publishes through the official Pages actions on each push to `main`. Pull requests build the site without publishing it. No separate `gh-pages` branch or hosting token is required.

For the created organization `Visual-World-Intelligence-Workshop`, run `bash bin/publish-github-pages` in your own terminal. It uses the prepared `output/github-pages-source.zip`, creates the public repository, uploads `main`, and enables Pages. GitHub may ask you to grant the `workflow` scope for uploading the Actions configuration. The script uses a temporary checkout because this managed workspace prevents creating `.git` locally.

The inherited template workflows are preserved under `docs/workflow-archive/`; they are inactive in this workshop repository. Jekyll excludes that archive, development files, and the template's plugin catalog page from the published website.

Add the workshop's OpenReview URL in `_data/workshop.yml` when available, and update the status, date, and venue when confirmed. No changes have been published to the old workshop's repository.

## Source import

The managed workspace prevents creating `.git`. The original production source was therefore downloaded using GitHub's source archive, at commit `97eb2e3525866653fe90764e1e0030b7c4ebcfe0`. This workspace contains the site files, without Git history. The archive's protected `.agents` and `.codex` paths could not be copied; their source remains in the original repository.

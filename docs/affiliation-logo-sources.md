# Organizer logo montage

Website image: `assets/img/organizer-logos-2027.svg` (1550 × 495). A PNG export is available alongside it. The white background preserves contrast. Ten logos are arranged in three rows, preserving their source proportions.

- Anates Labs: existing local artwork, `logo-anates-labs-inverted-on-white.png`.
- Mila, Meta, McGill, TUM: existing downloaded logo files. Meta’s missing viewBox was supplied from its original 948 × 191 dimensions.
- AMI Labs: original symbol and outlined “Advanced Machine Intelligence” wordmark extracted from the final frame of the official website animation at https://amilabs.xyz. No replacement text was typeset.
- Black Forest Labs: navigation SVG from https://bfl.ai.
- Université de Montréal: embedded SVG from the official website stylesheet at https://www.umontreal.ca/.
- École Polytechnique: official blue header SVG from https://www.polytechnique.edu/, including its Institut Polytechnique de Paris affiliation.
- CNRS: https://www.cnrs.fr/sites/default/files/logo/logo.svg.

Individual source assets are retained in `assets/img/affiliation-logos/`. The montage SVG embeds its images and can be uploaded as one file. Rebuild with `python3 bin/build-organizer-logos.py`. The PNG was rendered using GIMP’s librsvg and visually inspected. The cropped montage is included beneath the organizers on the home page; publication requires syncing the website repository.

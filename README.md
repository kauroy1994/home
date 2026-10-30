# Dr. Kaushik Roy — faculty website

The source for [kauroy1994.github.io/home](https://kauroy1994.github.io/home/), an independent faculty and MIND Lab website for Dr. Kaushik Roy, Assistant Professor of Computer Science, The University of Alabama.

## Site architecture

This site retains the original GitHub Pages/Jekyll structure and adds a dedicated, accessible layout:

- `_layouts/faculty.html`: common page shell, metadata, main navigation and footer
- `assets/css/faculty.css`: responsive UA-inspired design, no external build dependencies
- `_data/navigation.yml`: primary navigation
- `_pages/about.md`: landing page
- `_pages/research.md`, `publications.md`, `lab.md`, `people.md`, `teaching.html`, `news.md`, `opportunities.md`, `cv.md`, `contact.md`: faculty-site sections

The original academic-pages archive and content remain in the repository for historical reference.

## Site maintenance

Edit a page in `_pages/`, commit to `master`, and let GitHub Pages build the site. The `_config.yml` uses `url: https://kauroy1994.github.io` and `baseurl: /home`; use Jekyll's `relative_url` filter for internal links and images to keep subpath deployment working.

If using a local Ruby/Jekyll environment: `bundle install` then `bundle exec jekyll serve`; visit `http://127.0.0.1:4000/home/`.

### Suggested content update workflow
1. Verify new paper metadata against publisher DOI, proceedings, or arXiv before publishing.
2. Add the entry to `_pages/publications.md` and a short dated item to `_pages/news.md`.
3. Update the People page only when names, roles, and preferred publication permissions are confirmed.
4. Replace the CV note with a valid PDF link after a current approved CV is uploaded.
5. Review the footer's editorial update date.

## Verified source references (October 29, 2026)

- [UA Fall 2025 faculty announcement](https://cs.ua.edu/faculty-staff/our-new-fall-2025-faculty/)
- [UA Engineering faculty directory](https://eng.ua.edu/eng-directory/dr-kaushik-roy/)
- [Official UA brand color guidance](https://brand.ua.edu/colors/) — Crimson Flame #9E1B32, Capstone Gray #828A8F, Victory White
- [Official UA web brand guidance](https://brand.ua.edu/web/)
- [Scholar Commons dissertation](https://scholarcommons.sc.edu/etd/8563/)
- [ACM Transactions on Computing for Healthcare 2026](https://doi.org/10.1145/3805697)
- [AAAI 2026 demonstration paper](https://doi.org/10.1609/aaai.v40i48.42348)
- [NeSy 2026 sepsis work](https://arxiv.org/abs/2608.13617)
- [PMLR NeSy 2025](https://proceedings.mlr.press/v284/chattopadhyay25a.html)
- [IEEE Intelligent Systems 2025](https://doi.org/10.1109/MIS.2025.3561487)
- [UA 2026 SCoE CORE equipment news](https://autmn.ua.edu/news.html)

This site uses the University's published color palette for affiliation-appropriate visual continuity, but does not reproduce regulated UA wordmarks or present itself as an official institutional website.

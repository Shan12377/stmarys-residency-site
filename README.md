# St. Mary's Virtual Residency (private)

- `src/` is the source: wiki pages, index, log, What's New (`src/whats_new.md`), and tool pages. Edit here.
- `bash build.sh` builds the site into `public/`.
- Cloudflare Pages serves `public/` from `main` (build command none, output `public`), behind Cloudflare Access.
- Rules: see `src/CLAUDE.md`. No patient information, no names of colleagues, no St. Mary's internal documents, no copied commercial reference content.
- Monthly update: a scheduled task opens a pull request with source checks and a new What's New entry. Merge it to publish.

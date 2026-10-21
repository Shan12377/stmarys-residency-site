# Rules for any AI agent editing this repo (Antigravity, Claude, others)

This is Dr. Shallanda Hunter's private St. Mary's Virtual Residency site. Full content rules: `src/CLAUDE.md`. Read it before editing.

## Where things live
- Edit only `src/`. Wiki pages are `src/wiki/<section>/<Page_Name>.md` (sections: clinical, curriculum, drug-hub, journal-club, cases, sources, st-marys). Home page: `src/index.md`. Tools: `src/tools/*.html`. Read aloud bar: `src/listen.js`. Free natural voice audio lives in `src/audio/` (made by Claude with `src/get_speech_text.mjs` and `src/make_audio.py`); don't edit or delete it. If you change a page, its old audio is skipped automatically until it is remade.
- Never edit `public/` by hand. It is build output.
- Never add a `raw/` folder or anything from the private interview prep or St. Mary's internal documents.

## Publish
1. Make the edit in `src/`.
2. Add one line at the top of `src/whats_new.md`: `- **YYYY-MM-DD:** what changed.`
3. Run `bash build.sh` (Node 22; first run downloads Quartz).
4. Commit `src/` and `public/` together and push to `main`. Cloudflare Pages deploys in about a minute. For big changes, push a branch and open a pull request instead.
5. Run `git pull` before starting, every time; other agents also push here.

## Content rules (short version)
- Sources go in a numbered "## Sources" list at the bottom, one per line as `n. [Title](url)`; the build turns each [n] in the text into a link. Put the original guideline or paper first (doi.org link when there is one), then a free summary after "· summary:".
- Every dose or threshold has its source and year and a mark: ✅✅ two independent sources, ✅ one source, ⚠️ [VERIFY]. Link the source. Two versions of the same label count as one source.
- No patient information. Cases are invented and labeled as teaching cases.
- Never name or describe colleagues, managers or leaders.
- Don't copy text from Pyrls, Lexicomp or other paid references; link instead.
- Style: no em dashes, no hyphens used as punctuation, plain wording.
- Every clinical page ends with "Verify locally at St. Mary's".

## Visuals
- Algorithms, timelines and decision paths: use Mermaid code blocks (Quartz renders them). Doses written in a diagram follow the same source rules as text.
- AI generated images: concepts and memory aids only. Never put doses, drug names or numbers inside a generated image (image models misspell them). Save images in `src/wiki/<section>/images/` and give each one alt text.

# Schema: St. Mary's Virtual Residency (read this first, every session)

This folder is Dr. Shallanda Hunter's self-built PGY1-equivalent residency for her Staff Pharmacist (PRN) role at St. Mary's Medical Center, West Palm Beach (Tenet). St. Mary's is a Level I trauma center and comprehensive stroke center, and it includes the Palm Beach Children's Hospital (NICU, PICU, pediatrics) and Labor & Delivery.

The goal: within her first months she practices, documents and quotes guidelines at the level of a pharmacist who completed residency.

## How this knowledge base works (LLM wiki pattern)
- `raw/` holds untouched sources: guideline PDFs, Pyrls exports, St. Mary's policies and order sets, notes from preceptors, interview prep files. Never edit files in raw.
- `wiki/` holds compiled pages Claude writes and maintains. One concept per page. Pages link to each other with [[Page_Name]] (Obsidian style).
- `index.md` lists every wiki page with a one line summary. Update it every time a page is added.
- `log.md` is an append-only log: date, what was ingested or changed, open questions.

## Operations
1. **Ingest:** when she drops a file in `raw/`, read it, update or create the wiki pages it affects, cite it, add a log entry.
2. **Query:** answer from the wiki first, then sources. If the answer is durable, file it back into the wiki.
3. **Lint (weekly):** check for outdated guidelines, contradictions between pages, missing links, pages with no "Verify locally" note, and doses without a source.
4. **Drill:** generate cases in `wiki/cases/` from the module pages; score her answers Weak / Solid / Top 10% and explain.

## App plan
This folder becomes a private web app (Quartz on Cloudflare Pages with Cloudflare Access). Follow APP_BUILD_SPEC.md for the source registry, footnote citations, case format, monthly update task and privacy rules.

## Rules (non-negotiable)
- Every dose or threshold names its source and year (for example "ACOG 2020", "AHA/AAP 2025"). If unverified, mark it **[VERIFY]**.
- St. Mary's order sets, protocols and policies override general guidelines. Every clinical page ends with a "Verify locally at St. Mary's" list.
- Scope: she is a staff pharmacist. Pages describe the pharmacist's role (verify, recommend, prepare, monitor, educate, escalate), not prescribing.
- No patient identifiers anywhere in this folder. Cases are invented teaching cases, labeled as such.
- Pyrls content is copyrighted. Link to the Pyrls section; do not paste its text.
- Style: no em dashes, no hyphens used as punctuation, no AI tell words. Credentials: PharmD, MBA, RPh, CFNMP.
- Do not mention her business, apps or content brands in this folder.
- Never name or describe colleagues, managers or leaders in the wiki or the site.

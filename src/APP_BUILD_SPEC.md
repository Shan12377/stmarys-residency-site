# App Build Spec: St. Mary's Virtual Residency (private web app)

Status: planned 2026-10-17. Read this with CLAUDE.md before building anything.

## 1. The core idea
The Obsidian folder **is** the app. One set of markdown files, three ways to use it:
- Edit in **Obsidian** on the Mac.
- Store in a **private GitHub repo** (history, backups, review of every change).
- Publish as a **private website on Cloudflare Pages**, locked with **Cloudflare Access** so only her email can log in.

No database, no custom backend. Markdown in, website out.

## 2. Stack (simplest that works)
| Need | Tool | Why |
|---|---|---|
| Site generator | **Quartz v4** (quartz.jzhao.xyz) | Built for Obsidian vaults: [[wikilinks]], backlinks, graph view, full text search, callouts, all built in |
| Quick find | Quartz built in search | Searches every page and heading; no extra code |
| Hosting | Cloudflare Pages | Free; deploys on every GitHub push |
| Privacy | Cloudflare Access (Zero Trust, free tier) | Login by one time code to her email only |
| Sync Obsidian to GitHub | Obsidian Git plugin, or GitHub Desktop | Push changes with one click |
| Monthly updates | Scheduled Claude task (see section 6) | Opens a pull request; she approves before anything goes live |

Skipped on purpose: custom app, user accounts, database, scoring backend. Add later only if a real need shows up (see section 8).

## 3. Repo layout
```
/content
  index.md                 home: modules, latest changes, quick links
  whats-new/               one page per month (2026-11.md ...)
  curriculum/
  clinical/                one page per module
  cases/                   one file per case
  sources/registry.md      every source with an ID
  quick-find/              one line answer pages (doses, antidotes, targets)
/raw                       NOT published (see privacy rules)
CLAUDE.md, APP_BUILD_SPEC.md, log.md
```

## 4. Every claim traceable (Pharmacy Decoder style)
**Source registry** (`sources/registry.md`), one entry per source:
```
### SRC-ACOG-CO767-2019
- Title: ACOG Committee Opinion 767, Emergent Therapy for Acute Onset Severe Hypertension
- Year: 2019 (reaffirmed: [date])
- Public link: https://...
- Pyrls link: https://app.pyrls.com/... (opens with her Pyrls login)
- DOI or PMID:
- Last verified: 2026-10-17
- Superseded by: (blank unless replaced)
```
**In the pages**, every dose or threshold gets a footnote pointing to the registry:
```
Magnesium sulfate 4 to 6 g IV load, then 1 to 2 g/h.[^acog222]
[^acog222]: [[registry#SRC-ACOG-PB222-2020]] · section "Seizure prophylaxis"
```
Quartz renders footnotes as hover previews, so each claim is one click from its source.

**Source order:** the original source comes first (guideline, trial, FDA label, ISMP page) so a colleague without Pyrls can open it. Pyrls is the second link. When Pyrls cites an original source, record that original in the registry too.

**Rule:** a claim with no footnote is marked [VERIFY] and listed on a "Needs source" page that builds itself from search.

## 5. Cases (realistic, overlapping)
One file per case with frontmatter:
```
---
id: CASE-OB-TRAUMA-001
modules: [LD_Obstetrics_Core, Trauma_Core, Anticoagulation_Core]
difficulty: 3        # 1 intern, 2 staff, 3 resident, 4 specialist
setting: ED trauma bay, 02:00
tags: [pregnancy, TXA, reversal, Rh immune globulin]
---
```
Body:
1. **Scenario** (labs, vitals, home meds, the order you're asked to verify).
2. **Questions** in order, the way it unfolds on a shift (3 to 6 per case).
3. **Answer** in a collapsed callout so it stays hidden until clicked:
   `> [!answer]- Model answer` ... `> [!protocol]- Clinical breakdown` (the step by step pharmacist workup, the sources, what to monitor, what to say on the phone).
4. **Links** to every module it touches, so backlinks show "cases that use this page."

**Overlap cases on purpose**, because that's how the hospital works. For example: pregnant trauma patient on enoxaparin; neonate whose mother got magnesium and an incomplete GBS course; stroke patient on apixaban who needs thrombectomy; PICU DKA patient with hypokalemia and cerebral edema.

Target: 10 cases per module (about 120), plus 20 overlap cases, built 8 to 10 per session.

## 6. Monthly update system
A **scheduled Claude task on the 1st of every month**:
1. Check each feed: FDA Drug Safety Communications and new approvals, ISMP Acute Care alerts, ASHP drug shortages, and AHA/ASA, ACOG, AAP, IDSA, SCCM, EAST, CHEST, ADA guideline pages.
2. For anything new, find the affected pages using the source registry ("which pages cite SRC-X?").
3. Write `whats-new/YYYY-MM.md`: what changed, why it matters at St. Mary's, the links, and the pages affected.
4. Propose page edits in a **pull request** on GitHub. Nothing changes the live site until she reviews and merges (clinical accuracy gate).
5. Update "Last verified" dates and run the lint (missing sources, superseded guidelines, broken links).

The home page shows the latest "What's New" at the top.

## 7. Privacy rules (must follow)
- **No patient information anywhere**, ever, including in the private site.
- **St. Mary's internal documents** (order sets, policies, protocols) stay in `/raw/stmarys/` on her Mac only. That folder is in `.gitignore` and never goes to GitHub or Cloudflare. Wiki pages can say "St. Mary's protocol: check order set X" without copying it.
- **Pyrls:** links only, no pasted content (copyright). The links work only when she's logged in, which is fine for a private site.
- Cloudflare Access policy: allow only her email.

## 8. Phases
| Phase | What | Done when |
|---|---|---|
| 1 | Private GitHub repo from this folder; Quartz installed; Cloudflare Pages + Access | She can open the private URL on her phone |
| 2 | Source registry; retrofit footnotes into Modules 1 to 6 | Every dose has a clickable source |
| 3 | Modules 7 to 12 (anticoagulation, ID, critical care, IV room, med safety, project) | All 12 built |
| 4 | Case bank to about 140 using the case format | All modules have 10 cases |
| 5 | Monthly scheduled task live | First "What's New" page published |
| Later, only if needed | Quiz scoring or spaced repetition (for example export cases to Anki), mobile app wrapper | She asks for it |

## 9. Other tools (link, don't merge)
Her MTM Clinical Workbench and CMR Command Center (in ~/hunter_holistic_app/Outcomes/Hunter_Holistic_MTM_Lab_Obsidian_Vault/) stay separate apps, because they serve her MTM contract work, not hospital practice. If wanted later: publish each as its own private Cloudflare site under the same Access login and add a small "My tools" link list on the home page. Never copy their content into this residency.

## 10. Interview question bank
The clinical, IV room and order verification questions in raw/interview_prep (05, 05b, 05c, 06, plus the clinical parts of 04 and 11) become cases in the case format. Skip the personal and story files (02, 02b, 03, 07, 09, 10).

## 11. Journal club library
- Template: wiki/journal-club/Journal_Club_Template.md (JAMA Users' Guides, RoB 2 domains, CONSORT 2025).
- One page per trial, tagged to modules (for example CRASH-2 to Trauma_Core). Bottom line first.

## 12. Drug information hub (her own references)
Build her own reference pages, organized the way hospital drug references are organized, but with her own names and her own content from public, citable sources. Do not copy content, screenshots, layouts or names from Lexicomp, Micromedex, Trissel's or Sanford (copyright and trademark).
| Her section | Modeled on the role of | Public sources to build from |
|---|---|---|
| Drug Monographs | general drug reference (Lexicomp or Micromedex type) | FDA label via DailyMed, openFDA, guidelines |
| IV Compatibility and Admin | IV compatibility reference (Trissel's type) | FDA labels (dilution, stability, Y site statements), published studies; every page says "confirm in the hospital's IV compatibility database" |
| Antimicrobial Guide | antimicrobial therapy guide (Sanford type) | IDSA, AAP Red Book public summaries, CDC |
| Literature | PubMed | Links only |
Simulations: each case names which type of reference a pharmacist would open first and why, then gives the answer and the source.

## 13. Handoff
New chat prompt: "Open my St. Mary's Virtual Residency folder. Read CLAUDE.md, APP_BUILD_SPEC.md, index.md and the end of log.md. Continue with the next phase."

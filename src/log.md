# Log

## 2026-10-17
- Created the virtual residency structure (CLAUDE.md, START_HERE, index, log, raw, wiki).
- Built curriculum (12 week plan, daily routine), leadership lens, sources, Pyrls map.
- Built Modules 1 to 3: L&D, NICU, PICU, plus 8 practice cases.
- Checked the 2025 AHA/AAP resuscitation updates (PALS: early epinephrine in nonshockable arrest; NRP: deferred cord clamping 60 s or longer, ventilation 30 to 60 per minute).
- Copied interview prep into raw/interview_prep for later modules.
- Open [VERIFY] items: St. Mary's magnesium renal thresholds, oxytocin concentration, neonatal sepsis and meningitis regimen, pediatric code sheet, DKA potassium cutoff, neonatal epinephrine wording in 2025 Part 5, antenatal steroid late preterm criteria, Florida CE rule.
- Next: Module 4, Codes and Resuscitation (ACLS, PALS, NRP 2025 full text).

## 2026-10-17 (later)
- Built Module 4 Codes and Resuscitation, Module 5 Stroke (AHA/ASA 2026 AIS guideline: tenecteplase equally preferred, extended window to 9 h with imaging, DAPT for NIHSS up to 5 and within 72 h), Module 6 Trauma, plus 8 cases.
- New [VERIFY] items: 2025 post ROSC temperature wording, alteplase tubing flush procedure, DOAC and lytic eligibility wording in 2026 AIS guideline, AF anticoagulation start timing, SAH BP target, TBI seizure prophylaxis agent, open fracture type III regimen, trauma VTE protocol, PE arrest alteplase dose.
- Next: Module 7 Anticoagulation.

## 2026-10-17 (app plan)
- Wrote APP_BUILD_SPEC.md: Quartz + private GitHub + Cloudflare Pages + Cloudflare Access; source registry with footnotes (Pyrls and public links); case format with overlap cases; monthly scheduled update task via pull request; privacy rules (St. Mary's documents stay local in raw/stmarys/).
- Next: Phase 1 setup, then Module 7 Anticoagulation.

## 2026-10-17 (decisions)
- Original sources are the primary citation, Pyrls second.
- MTM Workbench and CMR Command Center stay separate; link only, later.
- Next: convert interview clinical questions (05, 05b, 05c, 06, clinical parts of 04 and 11) into cases.

## 2026-10-17 (site live)
- Site live at stmarys-residency.pages.dev, locked with Cloudflare Access (her two emails). Tools at /tools/ (lowercase file names), personal sections removed from the site copies; removed text saved in the MTM vault as Personal_Pre-Call_Ritual_and_Trackers.md.
- Added Journal_Club_Template. Planned drug information hub (own names and public sources, no copying of commercial references).
- Next: journal club pages for key trials, drug hub pilot (10 high alert drugs), interview questions into cases, Module 7.

## 2026-10-17 (drug hub pilot)
- Built Drug_Hub and Heparin monograph. Verification marks: two sources, one source, or VERIFY. Open VERIFY: PCI dosing, prophylaxis, anti Xa range, pediatric dosing, warfarin start after HIT.
- Next: Enoxaparin.
- Built Enoxaparin monograph. Open VERIFY: obesity protocol, St. Mary's anti Xa ranges, current ASRA edition, pediatric dosing.
- Next: Insulin.

## 2026-10-17 (simulator)
- Built tools/verify_sim.html: generic EHR style verification queue (patient banner, labs, active meds, notes, verify / modify / reject with required reasoning, feedback with study page link). 10 cases: 8 orders, 2 IV room product checks. Linked from My Tools.
- tools/ now holds the site copies of all tools plus rebuild_site.sh (Quartz build steps).
- Plan (batches): B1 remaining 8 pilot drugs; B2 Module 7 Anticoagulation + 10 interview question cases + simulator cases to 25; B3 journal club pages (CRASH-2, NINDS, tenecteplase trials, WOMAN, ESETT); B4 ID module + Antimicrobial Guide + vancomycin AUC; B5 IV Compatibility section + IV room simulator set; B6 Adult Critical Care; B7 Med Safety and Florida law; B8 GitHub + monthly update task.

## 2026-10-17 (auto publish)
- Private repo github.com/Shan12377/stmarys-residency-site holds the built site in public/. Cloudflare Pages project stmarys-residency-site deploys automatically on every push to main (build command none, output public).
- New address: https://stmarys-residency-site.pages.dev (locked by the same Access app "Only me"; old upload-only project stmarys-residency still exists and is also locked; she can delete it later).
- Claude GitHub App installed on that one repo. tools/rebuild_site.sh builds Quartz and pushes.

## 2026-10-17 (Batch 1)
- Built 8 monographs: Insulin_IV_DKA, Magnesium_Sulfate, Potassium_Chloride_IV, Vancomycin, Gentamicin, Norepinephrine, Thrombolytics_Stroke, 4F_PCC.
- Corrections: L&D magnesium toxicity now uses FDA label levels (reflexes weaken above about 4 mEq/L, respiratory paralysis about 10); load over 15 to 20 min; renal dosing from label. PICU page notes adult DKA K cutoff 3.5 (2024 consensus). Raw interview prep files still say 3.3 for adults; do not use them for DKA.
- Next: Batch 2 (Module 7, interview cases, simulator to 25).

## 2026-10-17 (Batch 2)
- Built Module 7 Anticoagulation_Core (DOACs, warfarin, periop with CHEST 2022 and PAUSE, ASRA neuraxial timing). Apixaban and rivaroxaban doses checked against two sources; edoxaban one source.
- Built Cases_Anticoag_and_Verification (10 cases from interview questions 05 and 06; DKA K cutoff kept at 3.5 for adults).
- Simulator now 25 cases (DOAC dosing, periop holds, bridging, epidural timing, warfarin reversal, HIT, duplicate anticoagulation, 2 IV room label checks).
- Open [VERIFY]: US apixaban dialysis wording, edoxaban second source, warfarin timing for neuraxial, St. Mary's bridging policy, PCC INR recheck timing, morphine in dialysis reference, 5 unit insulin for hyperkalemia.
- Next: Batch 3 journal club pages.

## 2026-10-17 (Batch 3)
- Built 5 journal club pages: CRASH-2, NINDS, AcT, WOMAN, ESETT. Main results checked against two summaries each; ARR and NNT calculated.
- Open [VERIFY]: volume and pages for AcT, WOMAN, ESETT; WOMAN within 3 h arm percentages; TXA renal and seizure notes; fosphenytoin rate limits; NINDS fragility index second source.
- Next: Batch 4 (ID module and Antimicrobial Guide).

## 2026-10-17 (Batch 4)
- Built Module 8 ID_Core (SSC 2021 sepsis, beta lactam allergy with 2022 practice parameter, C. diff, IV to PO, daily catches, stewardship workflow) and drug hub Antimicrobial_Guide (CAP 2019, HAP 2016, cUTI 2025, SSTI, meningitis, C. diff).
- Open [VERIFY]: hydrocortisone dose in SSC 2021, severe delayed allergy wording, cefepime renal dosing, duplicate anaerobe policy, asymptomatic bacteriuria exceptions, meningitis second source, necrotizing infection regimen, ASHP surgical prophylaxis.
- Next: Batch 5 (IV Compatibility section and IV room simulator set).

## 2026-10-17 (Batch 5)
- Built Module 10 IV_Room_Core (USP 797 2023 BUDs, product check, catches) and drug hub IV_Compatibility (phenytoin, ceftriaxone and calcium, liposomal amphotericin, nitroglycerin, amiodarone, PN, lipids, vincristine; ONS/ASCO 2025 extravasation).
- Correction: interview prep PN filter rule (0.22 micron for 2 in 1) is INS 2021; ASPEN 2020 uses 1.2 micron for all PN. Follow St. Mary's policy.
- Simulator now 34 cases (9 new IV room and line cases).
- Open [VERIFY]: immediate use rules, ISO class wording, garbing SOP, USP 800 details, hyperosmolar extravasation, phenytoin second source.
- Next: Batch 6 (Module 9 Adult Critical Care).

## 2026-10-17 (Batch 6)
- Built Module 9 Adult_Critical_Care (SSC 2021 pressors, PADIS 2018, PRIS, hyperkalemia with KDIGO severity, hyponatremia limits with 2023 debate, ICU glucose 140 to 180 and NICE-SUGAR).
- Simulator now 38 cases (4 ICU orders).
- Open [VERIFY]: septic shock steroid dose, PADIS propofol vs dexmedetomidine wording, propofol kcal/mL, US 3% bolus volume, stress ulcer prophylaxis guideline, augmented renal clearance.
- Next: Batch 7 (Med Safety and Florida law).

## 2026-10-17 (Batch 7)
- Built Module 11 Med_Safety_and_Florida_Law: ISMP 2024 high alert list (TXA added), Joint Commission National Performance Goals (replaced NPSGs January 1, 2026), Do Not Use abbreviations, just culture, Florida CE (30 h, 2 h med errors, 2 h controlled substances, HIV once) and E-FORCSE reporting.
- Open [VERIFY]: full ISMP list against the PDF, current Do Not Use list, live CE hours conflict, her first renewal rules in CE Broker, PDMP rules for discharge prescriptions, just culture source.
- Next: Batch 8 (monthly What's New scheduled task).

## 2026-10-17 (Batch 8)
- Repo now holds the source in src/ (wiki, index, log, whats_new.md, CLAUDE.md, tool pages; raw/ is never copied) plus build.sh, which builds the site from a fresh clone (Quartz pinned to 97a2d05).
- What's New now comes from src/whats_new.md.
- Scheduled task "Residency monthly update" runs on the 1st of each month at 8:52 AM Eastern: checks FDA, ISMP, guideline bodies, Florida Board and shortages; edits src/; opens a pull request. She merges to publish.
- All planned batches done. Module 12 (practice project) is chosen on the job.

## 2026-10-17 (Module 12)
- Built Practice_Advancement: recommended project magnesium sulfate infusion safety MUE on L&D (backups: TXA timing, thrombolytic dose accuracy, DOAC admission dosing, vancomycin 48 h stop), draft criteria, ASHP MUE guideline 2021 steps, IHI model, QI vs research, 6 month timeline, inservice outline.
- Added tools/intervention_log.html (browser storage, CSV export, blocks MRN and DOB patterns). Linked in My Tools.
- Open [VERIFY]: St. Mary's magnesium order set, Tenet IRB process, FSHP and ASHP abstract dates, typical MUE sample size.

## 2026-10-17 (drug hub sections)
- Built Pediatric_Neonatal_Dosing and Pregnancy_Lactation.
- Correction to Med_Safety_and_Florida_Law: Florida dropped the 10 live CE hours rule (amended effective May 22, 2025). First renewal rules added from the Board page.
- Open [VERIFY]: acetaminophen daily mg cap, croup dexamethasone max (12 vs 16 mg), ondansetron, auto injector bands, term neonate ampicillin interval, neonatal cefepime dose, several LactMed entries (opioids, magnesium, methylergonovine, ibuprofen, acetaminophen).

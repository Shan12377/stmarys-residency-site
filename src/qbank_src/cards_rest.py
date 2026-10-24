# Stroke, trauma, NICU, PICU, IV room, IV to PO, safety, verification basics and evidence cards.
def card(title, sections, sources): return {'title': title, 'sections': sections, 'sources': sources}
def s(t, url, mark='✅'): return {'t': t, 'url': url, 'mark': mark}
AIS = s('AHA/ASA 2026 acute ischemic stroke guideline (Top Things to Know)', 'https://professional.heart.org/en/science-news/2026-guideline-for-the-early-management-of-patients-with-acute-ischemic-stroke/top-things-to-know', '✅✅')
SAH = s('2023 AHA/ASA aneurysmal SAH guideline. Stroke 2023;54:e314-e370', 'https://doi.org/10.1161/STR.0000000000000436')
CRASH2 = s('CRASH-2. Lancet 2010;376:23-32', 'https://doi.org/10.1016/S0140-6736(10)60835-5', '✅✅')
CRASH3 = s('CRASH-3. Lancet 2019;394:1713-1723', 'https://doi.org/10.1016/S0140-6736(19)32233-0')
BTF = s('Brain Trauma Foundation 4th edition. Neurosurgery 2017;80:6-15', 'https://doi.org/10.1227/NEU.0000000000001432')
CDCTET = s('CDC: wound management to prevent tetanus', 'https://www.cdc.gov/tetanus/hcp/clinical-guidance/', '✅✅')
PROPPR = s('PROPPR. JAMA 2015;313:471-482', 'https://doi.org/10.1001/jama.2015.12')
EPI = s('LHSC NICU: epinephrine (neonatal resuscitation)', 'https://www.lhsc.on.ca/nicu/epinephrine', '✅✅')
NRP = s('AHA/AAP 2025 neonatal resuscitation', 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines')
BILI = s('AAP 2022 hyperbilirubinemia guideline. Pediatrics 2022', 'https://doi.org/10.1542/peds.2022-058859')
PALS = s('AHA 2025 PALS', 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines')
AES = s('AES 2016 status epilepticus guideline. Epilepsy Curr 2016;16:48-61', 'https://doi.org/10.5698/1535-7597-16.1.48')
ESETT = s('ESETT. N Engl J Med 2019;381:2103-2113', 'https://doi.org/10.1056/NEJMoa1905795')
ISPAD = s('ISPAD 2022 DKA guideline. Pediatr Diabetes 2022;23:835-856', 'https://doi.org/10.1111/pedi.13406')
FLUIDS = s('AAP 2018 maintenance IV fluids. Pediatrics 2018', 'https://doi.org/10.1542/peds.2018-3083')
USP797 = s('USP General Chapter 797 (2023)', 'https://www.usp.org/compounding/general-chapter-797')
COMP = s('Open Exam Prep: USP 797 personnel competency summary', 'https://open-exam-prep.com/study-guides/bcscp/ch10-quality-management-competency/10-2-personnel-training-competency')
USP800 = s('USP General Chapter 800', 'https://www.usp.org/compounding/general-chapter-hazardous-drugs-handling-healthcare')
CYRIAC = s('Cyriac and James. IV to oral switch overview. J Pharmacol Pharmacother 2014;5:83-87', 'https://doi.org/10.4103/0976-500X.130042')
POET = s('POET. N Engl J Med 2019;380:415-424', 'https://doi.org/10.1056/NEJMoa1808312')
ISMP = s('ISMP high alert medications (2024)', 'https://home.ecri.org/blogs/ismp-resources/high-alert-medications-in-acute-care-settings', '✅✅')
NPG = s('Joint Commission National Performance Goals (2026), Relias summary', 'https://www.relias.com/blog/joint-commission-national-performance-goals-are-here')
FLREN = s('Florida Board of Pharmacy: renewal', 'https://floridaspharmacy.gov/pharmacist-renewal/', '✅✅')
DEA = s('21 CFR 1301.76 (eCFR)', 'https://www.ecfr.gov/current/title-21/chapter-II/part-1301/section-1301.76')
MUE = s('ASHP MUE guideline. Am J Health Syst Pharm 2021;78:168-175', 'https://doi.org/10.1093/ajhp/zxaa393')
LOCAL = {'t': "St. Mary's protocols (verify locally)", 'url': '', 'mark': '⚠️'}

REST = {
'thrombolytics': card('Thrombolytics for acute ischemic stroke (tenecteplase, alteplase)', [
  ('Choice', 'Either alteplase or tenecteplase in the 4.5 hour window (2026). Selected patients up to about 9 hours or unknown onset with advanced imaging ✅✅ [AIS 2026].'),
  ('Tenecteplase', '**0.25 mg/kg IV bolus over 5 seconds, max 25 mg.** The STEMI dose is double: never use it. Flush with normal saline (precipitates with dextrose). Waste the excess so only the stroke dose is in the syringe.'),
  ('Alteplase', '**0.9 mg/kg, max 90 mg:** 10% bolus over 1 minute, 90% over 60 minutes; remove excess from the vial before hanging.'),
  ('Show the math', 'Tenecteplase 82 kg: 0.25 x 82 = **20.5 mg** (4.1 mL of 5 mg/mL). Alteplase 70 kg: 63 mg total; 6.3 mg bolus; 56.7 mg over 60 minutes.'),
  ('Gates before giving', 'BP below 185/110; glucose checked (treat if below 50); know the anticoagulant and last dose; contraindications include INR above 1.7, platelets below 100,000, therapeutic heparin or enoxaparin, recent DOAC dose; not for mild nondisabling symptoms.'),
  ('After', 'BP below 180/105 for 24 hours (intensive lowering below 140 not recommended); no antithrombotics for 24 hours; neuro checks.'),
  ('BP drugs', 'Labetalol 10 to 20 mg IV over 1 to 2 minutes (repeat once); nicardipine 5 mg/h, titrate 2.5 mg/h every 5 to 15 minutes (max 15); clevidipine 1 to 2 mg/h (max 21).'),
  ('Complications', 'Angioedema (worse with ACE inhibitors): stop; methylprednisolone, diphenhydramine, famotidine; epinephrine if worsening; icatibant or C1 esterase inhibitor may be considered. Bleeding: stop; cryoprecipitate 10 units; TXA 1 g IV over 10 minutes (or aminocaproic acid).'),
  ('Afterwards', 'Minor stroke or high risk TIA: aspirin + clopidogrel for 21 days (clopidogrel 300 to 600 mg load, then 75 mg), high intensity statin, glucose 140 to 180.'),
], [AIS, LOCAL]),

'nimodipine': card('Nimodipine (aneurysmal SAH)', [
  ('Dose', '60 mg orally or by tube every 4 hours for 21 days; if BP drops, 30 mg every 2 hours ✅ [SAH 2023].'),
  ('Never IV', 'Boxed warning: deaths when capsule liquid was injected IV. Use oral or enteral syringes that cannot connect to IV lines, labeled oral only ✅.'),
  ('Antiseizure', 'If used, levetiracetam is preferred over phenytoin ✅ [SAH 2023].'),
], [SAH, LOCAL]),

'trauma_drugs': card('Trauma bay drugs (TXA, calcium, RSI, osmotherapy, antibiotics, tetanus)', [
  ('TXA', '1 g IV over 10 minutes, then 1 g over 8 hours, only within 3 hours of injury (later may harm). Ask EMS what was given ✅✅ [CRASH-2]. TBI: CRASH-3 benefit in mild to moderate TBI within 3 hours ✅ [CRASH-3].'),
  ('Massive transfusion', 'Close to 1:1:1; calcium chloride 1 g (central) or calcium gluconate 3 g guided by ionized calcium (citrate binds calcium); watch potassium and temperature ✅ [PROPPR].'),
  ('RSI', 'Ketamine 1 to 2 mg/kg or etomidate 0.3 mg/kg (avoid full dose propofol in shock); rocuronium 1 to 1.2 mg/kg (sugammadex 16 mg/kg for immediate reversal); succinylcholine 1 to 1.5 mg/kg but never in hyperkalemia or 24 to 48 hours after burns, crush or spinal cord injury; start analgesia and sedation right after the tube.'),
  ('TBI', 'Mannitol 0.25 to 1 g/kg, or 3% 250 mL, or 23.4% 30 mL central only (ISMP high alert); seizure prophylaxis 7 days; no steroids ✅ [BTF].'),
  ('Open fractures', 'Cefazolin 2 g (3 g if 120 kg+) within 1 hour; type III add gram negative coverage; penicillin for farm or soil contamination per protocol ⚠️.'),
  ('Tetanus', 'Clean minor wound: booster if more than 10 years. Dirty wound: more than 5 years. Dirty + unknown or fewer than 3 doses: Tdap plus TIG 250 units IM ✅✅ [CDC].'),
  ('Burns', 'Parkland: 4 mL x kg x %TBSA of lactated Ringer\'s over 24 hours, half in the first 8 hours from the time of the burn.'),
  ('Later', 'Enoxaparin prophylaxis once bleeding is stable (often 24 to 48 hours); multimodal pain for ribs; thiamine before glucose in alcohol use.'),
], [CRASH2, CRASH3, PROPPR, BTF, CDCTET, LOCAL]),

'neonatal': card('Neonatal dosing essentials', [
  ('Ages', 'GA = weeks at birth. PNA = days since birth. PMA = GA + weeks since birth. Many intervals depend on PMA and PNA.'),
  ('Errors', 'Calculate mg/kg on every dose; leading zero, no trailing zero; mg/kg/dose vs mg/kg/day; preservative free products (benzyl alcohol causes gasping syndrome); read heparin concentrations every time.'),
  ('NRP', 'Ventilation first. Epinephrine 0.1 mg/mL: IV/UVC 0.02 mg/kg (0.01 to 0.03); ETT 0.1 mg/kg (0.05 to 0.1); every 3 to 5 minutes. Normal saline 10 mL/kg over 5 to 10 minutes ✅✅ [NRP; LHSC].'),
  ('Routine', 'Vitamin K 0.5 to 1 mg IM; erythromycin 0.5% eye ointment; hepatitis B vaccine within 24 hours (+ HBIG within 12 hours if mom HBsAg positive).'),
  ('Sepsis', 'Early onset: ampicillin + gentamicin (unit chart). Meningitis: ampicillin + cefepime or ceftazidime (cefotaxime unavailable) ⚠️. HSV: acyclovir 20 mg/kg every 8 hours.'),
  ('Ceftriaxone', 'Never with IV calcium in neonates; avoid in hyperbilirubinemia ✅ [label; AAP 2022].'),
  ('Caffeine', 'Citrate 20 mg/kg load, then 5 to 10 mg/kg daily; 2 mg citrate = 1 mg base.'),
  ('Hypoglycemia', 'D10W 2 mL/kg, then infusion; never D50.'),
  ('TPN', 'Calcium and phosphate solubility curve; phosphate early, calcium last; cysteine helps; independent double check.'),
], [NRP, EPI, BILI, LOCAL]),

'peds': card('Pediatric dosing and emergencies', [
  ('Rule', 'mg/kg, never above the adult dose. Measured weight in kg.'),
  ('PALS', 'Epinephrine 0.01 mg/kg (0.1 mL/kg of 0.1 mg/mL), max 1 mg; amiodarone 5 mg/kg (max 300), up to 15 mg/kg; lidocaine 1 mg/kg; adenosine 0.1 mg/kg (max 6) then 0.2 mg/kg (max 12); atropine 0.02 mg/kg (max 0.5); calcium chloride 20 mg/kg; dextrose 0.5 to 1 g/kg ✅ [PALS 2025].'),
  ('Status epilepticus', 'Midazolam IM 10 mg (over 40 kg) or 5 mg (13 to 40 kg); lorazepam 0.1 mg/kg IV (max 4), repeat once. Then levetiracetam 60 mg/kg (max 4,500), fosphenytoin 20 mg PE/kg (max 1,500), or valproate 40 mg/kg (max 3,000) ✅✅ [AES; ESETT].'),
  ('DKA', 'No bolus; insulin 0.05 to 0.1 units/kg/h after the first hour of fluids; mannitol 0.5 to 1 g/kg or 3% 2.5 to 5 mL/kg ready ✅ [ISPAD 2022].'),
  ('Everyday', 'Acetaminophen 15 mg/kg every 6 hours (max 75 mg/kg/day, 4 g); ibuprofen 10 mg/kg every 6 to 8 hours (6 months+); Holliday Segar 4/2/1; isotonic maintenance fluids ✅ [AAP 2018].'),
  ('Withdrawal', 'After 5+ days of opioid or benzodiazepine infusions: WAT-1 scoring and a wean (enteral methadone, lorazepam).'),
  ('Poisoning', 'Sulfonylurea: dextrose + octreotide. Poison Control 1 800 222 1222.'),
], [PALS, AES, ESETT, ISPAD, FLUIDS, LOCAL]),

'usp797': card('USP 797 and the IV room (topic card)', [
  ('Competency', 'Training and knowledge every 12 months; garbing (gloved fingertip: 3 passes at 0 CFU to start) and aseptic technique (media fill + fingertip above 3 CFU fails + surface sample) every 6 months for Category 1 and 2, every 3 months for Category 3 ✅✅ [USP 797; summary].'),
  ('Garbing', 'Dirty to clean: shoe covers, hair cover, mask, wash 30 seconds, gown, sterile gloves, sterile 70% IPA often.'),
  ('Rooms', 'ISO 5 hood, ISO 7 buffer, ISO 8 ante (ISO 7 if it opens to negative pressure); buffer positive at least 0.02 inch water column; never block first air.'),
  ('Monitoring', 'Certification every 6 months; surface sampling at least monthly; viable air at least every 6 months; sporicidal cleaning at least monthly.'),
  ('BUDs', 'Immediate use: 3 products max, start within 4 hours. Category 1: 12 hours room temperature, 24 hours refrigerated. Category 2 (sterile ingredients, no sterility test): 4 days, 10 days, 45 days frozen; with a nonsterile ingredient: 1, 4, 45. Always the shorter of sterility and stability.'),
  ('Vials', 'Single dose: 12 hours if punctured in ISO 5 (1 hour outside). Multiple dose: 28 days unless labeled otherwise.'),
  ('Hazardous (USP 800)', 'Containment hood in a negative pressure room; double ASTM D6978 gloves; chemo gown; CSTD; spill kit ✅ [USP 800].'),
  ('Catches', 'Phenytoin NS only (filter, max 50 mg/min); liposomal amphotericin D5W only; ampicillin in NS; nitroglycerin non PVC; vincristine minibag; 3 in 1 PN 1.2 micron filter; peripheral PN 900 mOsm/L or less; peripheral KCl 10 mEq/h.'),
], [USP797, COMP, USP800, LOCAL]),

'iv_po': card('IV to PO conversion (topic card)', [
  ('Criteria', 'Working gut, taking other oral meds, improving and stable, an oral drug with good absorption.'),
  ('1:1', 'Levofloxacin, moxifloxacin, linezolid, metronidazole, fluconazole, levetiracetam, acetaminophen, pantoprazole ✅ [Cyriac; labels].'),
  ('Dose changes', 'Furosemide about 1:2 (IV:PO); ciprofloxacin 400 mg IV = 500 to 750 mg PO; metoprolol about 1:2.5; levothyroxine IV is lower (about 50 to 75% of oral).'),
  ('Stay IV', 'S. aureus bacteremia early, meningitis, endocarditis initially (POET: partial oral therapy in selected stable patients after at least 10 days IV, an ID decision) ✅ [POET].'),
  ('Interactions', 'Quinolones and tetracyclines with Ca, Mg, Al, Fe, Zn (cipro 2 hours before or 6 hours after); phenytoin and tube feeds; phenytoin sodium (92%) vs acid (100%).'),
], [CYRIAC, POET, LOCAL]),

'safety': card('Medication safety and Florida law (topic card)', [
  ('High alert', 'Insulin, anticoagulants, concentrated electrolytes, opioids, neuromuscular blockers, chemotherapy, magnesium, oxytocin, TXA injection (added 2024). Fix with standard concentrations, pump libraries, premixes, separate storage ✅✅ [ISMP].'),
  ('Abbreviations', 'No U, IU, QD, QOD, MS, MSO4, MgSO4, trailing zeros; always a leading zero.'),
  ('Joint Commission 2026', 'National Performance Goals replaced the NPSGs; medication management covers labeling, anticoagulants, pharmacist review, override review, standard concentrations, stewardship ✅ [NPG].'),
  ('Controlled substances', 'Suspected diversion: report per policy, never confront alone. Theft or significant loss: DEA in writing within 1 business day, then Form 106 ✅ [21 CFR 1301.76].'),
  ('Florida', 'Renew every 2 years, 30 hours, 2 h medication errors, 2 h controlled substances, no live hours since 2025; immunization 3 h; consultant 24 h. E-FORCSE reporting by the next business day ✅✅ [Board].'),
], [ISMP, NPG, DEA, FLREN]),

'verify_basics': card('Order verification basics (topic card)', [
  ('Order of checks', 'Patient (age, weight, allergies with reaction, pregnancy or breastfeeding), indication, labs (SCr, platelets, others by drug), drug and dose, duplicates and interactions, then decide.'),
  ('CrCl', 'Cockcroft Gault: (140 minus age) x weight in kg / (72 x SCr), x 0.85 if female. Think about which weight in obesity, very low weights, and changing creatinine.'),
  ('Allergies', 'Every allergy needs a reaction. Clarify vague labels; document tolerated drugs.'),
  ('Who to call', 'The prescriber (or covering prescriber) changes orders; the nurse gives information; your supervisor helps when you disagree. Use SBAR.'),
  ('Priorities', 'Life threatening now, then time sensitive (first doses, STAT), then routine, then questions.'),
  ('Drug information', 'Get background, find the real question, search (Trissel\'s or King for Y site; LactMed; Lexicomp or Micromedex), answer clearly, document. No data for a Y site pair means do not run them together.'),
], [ISMP, LOCAL]),

'evidence': card('Reading trials (topic card)', [
  ('Absolute vs relative', 'ARR = control rate minus treatment rate. RRR = ARR / control rate. NNT (or NNH) = 1 / ARR.'),
  ('Worked', 'NICE-SUGAR 27.5 vs 24.9%: ARI 2.6, NNH about 38. AMPLIFY-EXT 8.8 vs 1.7%: ARR 7.1, NNT about 14. BRIDGE bleeding 3.2 vs 1.3%: NNH about 53.'),
  ('Noninferiority', '"Not met" means not proven as good, not proven worse.'),
  ('Projects', 'MUE targets: high alert, high cost, high volume, new alert. Fix with order sets and pump limits. Ask the IRB before collecting data if you may present ✅ [ASHP MUE].'),
], [MUE]),
}

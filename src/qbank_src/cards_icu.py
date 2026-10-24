# ICU, ID and code drug cards.
def card(title, sections, sources): return {'title': title, 'sections': sections, 'sources': sources}
def s(t, url, mark='✅'): return {'t': t, 'url': url, 'mark': mark}
SSC = s('Surviving Sepsis Campaign 2021. Crit Care Med 2021;49:e1063-e1143', 'https://doi.org/10.1097/CCM.0000000000005337', '✅✅')
NE = s('Norepinephrine prescribing information (2022)', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215700s000lbl.pdf')
PADIS = s('PADIS guideline. Crit Care Med 2018;46:e825-e873', 'https://doi.org/10.1097/CCM.0000000000003299')
PRIS = s('Kam and Cardone. Propofol infusion syndrome. Anaesthesia 2007;62:690-701', 'https://doi.org/10.1111/j.1365-2044.2007.05055.x')
KDIGO = s('KDIGO dyskalemia conference. Kidney Int 2020;97:42-61', 'https://doi.org/10.1016/j.kint.2019.09.018', '✅✅')
HYPO = s('Society for Endocrinology: emergency management of severe hyponatraemia (2022)', 'https://www.endocrinology.org/media/xhrhxhxm/emergency-management-of-severe-and-moderately-severely-symptomatic-hyponatraemia-in-adult-patients-2022.pdf', '✅✅')
DKA = s('Hyperglycemic crises consensus. Diabetes Care 2024;47:1257-1275', 'https://doi.org/10.2337/dci24-0032', '✅✅')
KCL = s('Potassium Chloride Injection prescribing information (2019)', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/019904s020lbl.pdf')
SUP = s('SCCM/ASHP 2024 stress ulcer prophylaxis guideline', 'https://www.sccm.org/clinical-resources/guidelines/guidelines/sccm-ashp-guideline-prevention-of-ugib', '✅✅')
NICE = s('NICE-SUGAR. N Engl J Med 2009;360:1283-1297', 'https://doi.org/10.1056/NEJMoa0810625')
CAP = s('ATS/IDSA CAP 2019. Am J Respir Crit Care Med 2019;200:e45-e67', 'https://doi.org/10.1164/rccm.201908-1581ST', '✅✅')
HAP = s('IDSA/ATS HAP and VAP 2016. Clin Infect Dis 2016;63:e61-e111', 'https://doi.org/10.1093/cid/ciw353')
CUTI = s('IDSA 2025 complicated UTI. Clin Infect Dis 2025', 'https://doi.org/10.1093/cid/ciaf460', '✅✅')
MEN = s('IDSA bacterial meningitis 2004. Clin Infect Dis 2004;39:1267-1284', 'https://doi.org/10.1086/425368', '✅✅')
MERINO = s('MERINO. JAMA 2018;320:984-994', 'https://doi.org/10.1001/jama.2018.12163')
ALLERGY = s('Beta lactam allergy review citing the 2022 practice parameter (J Allergy Clin Immunol Glob 2024)', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11609518')
CEFEP = s('FDA safety alert: cefepime neurotoxicity (2012)', 'https://www.drugs.com/fda-alerts/544-0.html')
MRSA = s('IDSA MRSA guideline 2011. Clin Infect Dis 2011;52:e18-e55', 'https://doi.org/10.1093/cid/ciq146')
AHA = s('AHA CPR and ECC guidelines (2025)', 'https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines', '✅✅')
AHATOX = s('AHA 2023 focused update: cardiac arrest and toxicology. Circulation 2023', 'https://doi.org/10.1161/CIR.0000000000001161')
LAST = s('Third ASRA practice advisory on local anesthetic toxicity. Reg Anesth Pain Med 2018;43:113-123', 'https://doi.org/10.1097/AAP.0000000000000720')
MH = s('NYSORA: updated malignant hyperthermia guidelines (MHAUS based)', 'https://www.nysora.com/education-news/updated-guidelines-for-managing-malignant-hyperthermia/')
LOCAL = {'t': "St. Mary's ICU, antimicrobial and code protocols (verify locally)", 'url': '', 'mark': '⚠️'}

ICU = {
'pressors': card('Vasopressors and steroids in septic shock (norepinephrine, vasopressin, epinephrine, dobutamine, hydrocortisone)', [
  ('Order', 'Norepinephrine first to MAP 65; add vasopressin rather than raising norepinephrine; epinephrine next; dobutamine (or epinephrine) for poor heart function with low perfusion ✅✅ [SSC 2021].'),
  ('Steroids', 'Hydrocortisone 200 mg/day (50 mg IV every 6 hours or infusion) when norepinephrine or epinephrine is 0.25 mcg/kg/min or more for at least 4 hours ✅✅ [SSC 2021].'),
  ('Line', 'Central line preferred; short term peripheral start in a large proximal vein is acceptable while access is placed ✅ [SSC 2021]. Use St. Mary\'s standard concentrations only ⚠️.'),
  ('Show the math', 'Norepinephrine 4 mg/250 mL = 16 mcg/mL. For 80 kg at 0.1 mcg/kg/min: 8 mcg/min x 60 = 480 mcg/h ÷ 16 = **30 mL/h**.'),
  ('Extravasation', 'Stop, aspirate, remove the catheter, restart elsewhere, elevate; **phentolamine 5 to 10 mg in 10 to 15 mL NS** infiltrated into the area, best within 12 hours ✅ [label].'),
  ('Timing', 'Norepinephrine works and wears off within 1 to 2 minutes: never let the bag run dry; hang the next bag early.'),
], [SSC, NE, LOCAL]),

'sedation_icu': card('ICU analgesia and sedation (PADIS): fentanyl, propofol, dexmedetomidine, benzodiazepines', [
  ('Order of care', 'Analgesia first, then sedation; light sedation (RASS) for most; CPOT or BPS when the patient cannot report pain ✅ [PADIS].'),
  ('Preferred sedatives', 'Propofol or dexmedetomidine over benzodiazepines ✅ [PADIS].'),
  ('Delirium', 'Screen (CAM-ICU or ICDSC); no routine antipsychotics to prevent or treat; dexmedetomidine when agitation blocks extubation ✅ [PADIS].'),
  ('Propofol', 'Hypotension; lipid calories (about 1.1 kcal/mL); triglycerides and CK on long infusions; **PRIS** risk above about 4 mg/kg/h (about 67 mcg/kg/min) and after 48 hours, especially with catecholamines or steroids: acidosis, bradycardia, rhabdomyolysis, high triglycerides; stop it ✅ [Kam 2007].'),
  ('Dexmedetomidine', 'Bradycardia and hypotension; little respiratory depression.'),
  ('Withdrawal', 'After about 5 days or more of opioid or benzodiazepine infusions, wean rather than stop.'),
], [PADIS, PRIS]),

'hyperk': card('Hyperkalemia treatment (protect, shift, remove)', [
  ('Protect', 'Calcium gluconate 1 g (10 mL of 10%) IV over 2 to 5 minutes, repeat in 5 minutes if ECG changes persist (some protocols use 3 g; calcium chloride 1 g centrally has about 3 times the calcium) ✅✅ [KDIGO; protocol] ⚠️ check order set.'),
  ('Shift', 'Regular insulin 10 units IV with dextrose 25 g (D50 50 mL); **5 units** if kidney failure, low weight or elderly; glucose every hour for 4 to 6 hours. Nebulized albuterol 10 to 20 mg. Bicarbonate only if acidotic ✅✅ [KDIGO].'),
  ('Remove', 'Sodium zirconium cyclosilicate 10 g or patiromer 8.4 g; loop diuretic if urine is made; dialysis ✅✅ [KDIGO].'),
  ('Severity', 'Severe: K above 6.5, or 6.1 to 6.5 with ECG changes ✅ [KDIGO].'),
  ('Find the cause', 'ACE inhibitors, ARBs, spironolactone, trimethoprim, heparin, NSAIDs, potassium in fluids or TPN, missed dialysis, rhabdomyolysis.'),
  ('Avoid', 'Succinylcholine in hyperkalemia or after burns or crush (24 to 48 hours on).'),
], [KDIGO, LOCAL]),

'hyponatremia_tx': card('Severe hyponatremia (3% saline)', [
  ('Severe symptoms', '3% saline 100 to 150 mL over 10 to 20 minutes, repeat up to about 3 times; goal a 4 to 6 mmol/L rise; 100 mL raises Na about 2 to 3 ✅✅ [Society for Endocrinology; ACEP].'),
  ('Limits', 'About 10 mmol/L in the first 24 hours, then 8 per 24 hours; 8 per 24 hours if high risk (alcohol use, low potassium, malnutrition, liver disease) ✅✅.'),
  ('Overcorrection', 'Stop hypertonic fluid; hypotonic fluid with or without desmopressin ✅.'),
  ('Evidence note', 'Newer data suggest osmotic demyelination is rare; follow St. Mary\'s protocol ✅ [MacMillan 2023].'),
], [HYPO, LOCAL]),

'dka_insulin': card('DKA insulin and potassium (adults, 2024 consensus)', [
  ('Potassium first', 'K below 3.5: hold insulin, give potassium (about 10 mEq/h). K 3.5 to 5.0: add 10 to 20 mEq per liter of fluid and start insulin. K above 5.0: insulin only, recheck every 2 hours ✅✅ [2024 consensus].'),
  ('Insulin', 'Fixed rate regular insulin 0.1 units/kg/h, no routine bolus (only if IV access is delayed) ✅✅.'),
  ('Glucose below 250', 'Add D5 or D10; lower insulin to 0.05 units/kg/h; keep insulin until ketones clear ✅✅.'),
  ('Resolved', 'Beta hydroxybutyrate below 0.6 and pH 7.3 or more or bicarbonate 18 or more; give SC basal insulin 1 to 2 hours before stopping the drip ✅✅.'),
  ('Fluids', 'Isotonic saline or balanced crystalloid 500 to 1,000 mL/h for 2 to 4 hours if heart and kidneys allow ✅.'),
  ('Children', 'Different (ISPAD 2022): no bolus, 0.05 to 0.1 units/kg/h after the first hour of fluids, mannitol or 3% ready for cerebral edema.'),
], [DKA, LOCAL]),

'kcl_iv': card('IV potassium chloride', [
  ('Never', 'IV push (cardiac arrest). Always a premixed bag on a pump ✅ [label].'),
  ('Rates', 'Peripheral usually no faster than 10 mEq/h; faster needs a central line and continuous ECG per policy; label allows up to 40 mEq/h only for urgent K below 2.0 with ECG changes or paralysis ✅ [label].'),
  ('Expected rise', 'About 0.1 mEq/L per 10 mEq in a stable patient (rough guide); recheck after equilibration, not from the infusing arm.'),
  ('Magnesium', 'Replace low magnesium too, or potassium keeps leaking into urine.'),
  ('Kidneys', 'Reduce or hold with poor urine output or rising creatinine.'),
], [KCL, LOCAL]),

'sup': card('Stress ulcer prophylaxis (PPI or H2 blocker)', [
  ('Who', 'Critically ill adults with coagulopathy, shock or chronic liver disease ✅✅ [SCCM/ASHP 2024].'),
  ('Not', 'Ventilation alone is not an established indication; low risk patients on tube feeds.'),
  ('Stop', 'When risk resolves or at ICU transfer: a common source of unneeded PPIs at discharge.'),
], [SUP]),

'icu_glucose': card('ICU glucose control', [
  ('Target', 'Start insulin above 180; target 140 to 180 mg/dL ✅✅ [ADA; AACE].'),
  ('Why not tighter', 'NICE-SUGAR: 81 to 108 raised 90 day death (27.5% vs 24.9%) and severe hypoglycemia (6.8% vs 0.5%) ✅ [NICE-SUGAR].'),
], [NICE]),

'betalactams': card('Beta lactams in the hospital (cefazolin, ceftriaxone, cefepime, piperacillin tazobactam, meropenem)', [
  ('Common adult doses (normal kidneys)', 'Cefazolin 2 g IV every 8 hours (3 g for surgical prophylaxis if 120 kg+). Ceftriaxone 1 to 2 g daily (**2 g every 12 hours for meningitis**). Cefepime 2 g every 8 hours. Piperacillin tazobactam 4.5 g every 6 hours. Meropenem 1 g every 8 hours (2 g every 8 hours for meningitis) ✅ [IDSA; CAP; HAP].'),
  ('How they kill', 'Time dependent: keep levels above the MIC; prolonged infusion after the first dose suggested in sepsis ✅ [SSC 2021].'),
  ('Kidneys', 'Full first dose, then adjust. **Cefepime:** adjust when CrCl is 60 or less; accumulation causes confusion, myoclonus, nonconvulsive status ✅ [FDA alert].'),
  ('Allergy', 'Cross reactivity follows the R1 side chain. Cefazolin shares no side chain with other US beta lactams. With an unconfirmed non anaphylactic penicillin history, cephalosporins can be given without testing ✅ [2022 practice parameter].'),
  ('Coverage pearls', 'Ceftriaxone: no Pseudomonas, no Listeria, no enterococcus. Cefepime and pip tazo: Pseudomonas. Pip tazo and carbapenems already cover anaerobes (no metronidazole needed). ESBL bacteremia: carbapenem (MERINO) ✅ [MERINO].'),
  ('Neonates', 'No ceftriaxone with IV calcium or with hyperbilirubinemia.'),
], [CAP, HAP, MEN, SSC, CEFEP, ALLERGY, MERINO]),

'abx_syndromes': card('Empiric regimens and durations by syndrome', [
  ('CAP (floor)', 'Ceftriaxone + azithromycin, or a respiratory fluoroquinolone alone; beta lactam + doxycycline if macrolide and FQ are both unsuitable; at least 5 days ✅✅ [CAP 2019].'),
  ('HAP', 'Antipseudomonal single agent (pip tazo, cefepime, levofloxacin, meropenem) unless high risk; MRSA coverage only with risk factors; 7 days; stop vancomycin if MRSA nares negative ✅ [HAP 2016].'),
  ('cUTI and pyelonephritis', 'Ceftriaxone, a fluoroquinolone (not used in 12 months) or TMP SMX by susceptibility; 7 days (5 to 7 with FQ); no nitrofurantoin or oral fosfomycin; oral step down when improving ✅✅ [IDSA 2025].'),
  ('Asymptomatic bacteriuria', 'Do not treat, except pregnancy and before urologic procedures with mucosal trauma ✅✅ [IDSA 2019].'),
  ('Skin', 'Nonpurulent: cephalexin or cefazolin about 5 days. Abscess: drain; TMP SMX or doxycycline if over 2 cm or high risk ✅✅.'),
  ('Meningitis', 'Vancomycin + ceftriaxone 2 g every 12 hours; add ampicillin 2 g every 4 hours if over 50, pregnant or immunocompromised; dexamethasone 0.15 mg/kg every 6 hours started before or with the first dose ✅✅ [IDSA 2004].'),
  ('S. aureus bacteremia', 'MSSA: cefazolin or nafcillin/oxacillin (better than vancomycin); repeat cultures, ID consult, echo, at least 14 days IV for uncomplicated ✅ [IDSA MRSA 2011].'),
  ('C. difficile', 'Fidaxomicin 200 mg BID x 10 days preferred; oral vancomycin 125 mg QID x 10 days alternative.'),
], [CAP, HAP, CUTI, MEN, MRSA, LOCAL]),

'linezolid': card('Linezolid', [
  ('Dose', '600 mg IV or PO every 12 hours (1:1 oral) ✅ [label].'),
  ('Interactions', 'Weak MAO inhibitor: serotonin syndrome with SSRIs, SNRIs and other serotonergic drugs; tyramine foods in large amounts ✅ [label].'),
  ('Toxicity', 'Myelosuppression (platelets) usually after about 2 weeks; lactic acidosis, neuropathy with long use ✅ [label].'),
], [s('Linezolid prescribing information (DailyMed)', 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=linezolid')]),

'acls_drugs': card('Adult cardiac arrest and peri arrest drugs (AHA 2025)', [
  ('Epinephrine', '1 mg IV/IO every 3 to 5 minutes: as soon as possible in asystole or PEA; after initial shocks fail in VF or pulseless VT ✅✅ [AHA 2025].'),
  ('Amiodarone / lidocaine', 'Refractory VF or pulseless VT: amiodarone 300 mg push, then 150 mg; or lidocaine 1 to 1.5 mg/kg, then 0.5 to 0.75 mg/kg. After ROSC: amiodarone 1 mg/min x 6 h, then 0.5 mg/min x 18 h ✅✅.'),
  ('Not routine', 'Calcium, bicarbonate, magnesium only for specific causes; vasopressin offers no advantage over epinephrine.'),
  ('Reversible causes', 'Hyperkalemia: calcium chloride 1 g (or gluconate 3 g), insulin + dextrose, bicarbonate if acidotic. Torsades: magnesium 1 to 2 g. Opioids: naloxone (ventilate first). Tricyclics: bicarbonate 1 to 2 mEq/kg. Local anesthetic: lipid 20% 1.5 mL/kg then 0.25 mL/kg/min, epinephrine 1 mcg/kg or less ✅✅ [AHA 2023 tox; ASRA].'),
  ('Peri arrest', 'Bradycardia: atropine 1 mg every 3 to 5 min (max 3 mg), then epinephrine 2 to 10 mcg/min, dopamine 5 to 20 mcg/kg/min or pacing. SVT: adenosine 6 mg then 12 mg rapid push with flush (3 mg with central line, transplant, dipyridamole). Anaphylaxis: epinephrine 0.5 mg IM thigh every 5 to 15 min ✅✅.'),
  ('Malignant hyperthermia', 'Dantrolene 2.5 mg/kg IV, repeat to effect; know your product (Ryanodex reconstitutes faster) ✅ [MHAUS].'),
  ('After ROSC', 'SBP 90+ and MAP 65+, SpO2 92 to 98%, temperature below 37.5 °C with fever prevention ✅.'),
], [AHA, AHATOX, LAST, MH, LOCAL]),
}

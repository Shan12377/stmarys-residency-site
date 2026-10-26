# Module 14 balancing and Module 15 (Mixed Patients) rewrites.
R = {
('pa03', 1): [
 ('A small PDSA on one unit or shift', True, 'Plan Do Study Act: try, measure, adjust.'),
 ('Roll it out hospital wide on day one', False, 'Test small first.'),
 ('Run a randomized trial for 12 months', False, 'Research design; QI tests rapidly.'),
 ('Wait for next year\'s MUE to recheck', False, 'Too slow.')],
('pa04', 0): [
 ('2.6 percentage points', True, '27.5 minus 24.9.'),
 ('10.4% (2.6 / 24.9)', False, 'That is the relative risk increase.'),
 ('27.5 percentage points', False, 'The event rate, not the difference.'),
 ('1.1 (27.5 / 24.9)', False, 'That is the relative risk.')],
('pa05', 0): [
 ('ARR 7.1 points; NNT about 14', True, 'Over 12 months.'),
 ('ARR 81 points; NNT about 1', False, '81% is the relative reduction.'),
 ('ARR 7.1 points; NNT about 71', False, 'NNT = 1 / 0.071.'),
 ('ARR 1.7 points; NNT about 59', False, 'Uses the apixaban rate alone.')],
('pa06', 1): [
 ('Weigh the bleeding vs recurrence trade', True, 'For each patient, alongside CHEST 2021.'),
 ('Use full dose for every patient', False, 'Ignores the bleeding difference.'),
 ('Use reduced dose for every patient', False, 'Ignores the uncertainty.'),
 ('Ignore it; it failed its endpoint', False, 'Still informative.')],
('pa08', 0): [
 ('Why, what nurses see, numbers, antidote', True, 'Reflexes before breathing; one case; end with 3 questions.'),
 ('Forty slides of pharmacokinetics', False, 'Too much for 15 minutes.'),
 ('A handout and no discussion time', False, 'Less retention.'),
 ('Read the package insert aloud', False, 'Not focused on nurse actions.')],
('mx01', 0): [
 ('Check reflexes, RR and Mg level; lower the rate', True, 'Label: renal impairment maintenance 1 g/h; hold if UO below 100 mL per 4 h.'),
 ('Continue 2 g/h; UO above 15 mL/h is enough', False, 'Label requires 100 mL per 4 hours (25 mL/h).'),
 ('Stop magnesium and give calcium gluconate 1 g', False, 'Calcium is for toxicity signs, which are not described yet.'),
 ('Raise to 3 g/h now that fever is present', False, 'Accumulation risk with falling kidney function.')],
('mx01', 1): [
 ('Ampicillin 2 g IV q6h plus gentamicin', True, 'ACOG.'),
 ('Ampicillin 2 g IV q4h plus gentamicin', False, 'Every 4 hours is the meningitis interval.'),
 ('Cefazolin 2 g IV q8h plus gentamicin', False, 'The alternative for mild penicillin allergy; she has none.'),
 ('Vancomycin 1 g IV q12h alone', False, 'Misses gram negatives.')],
('mx01', 2): [
 ('Use levels, not normal clearance; watch Mg synergy', True, 'Magnesium plus aminoglycosides both block the neuromuscular junction.'),
 ('Hartford 7 mg/kg; SCr 1.3 is still normal', False, 'Rising SCr and low UO mean clearance is falling.'),
 ('Gentamicin 5 mg/kg q24h; no levels needed', False, 'Changing kidneys need levels.'),
 ('Double the gentamicin to overcome fever', False, 'Raises toxicity.')],
('mx02', 0): [
 ('Load 20 to 35 mg/kg (about 2,000 mg), full', True, 'Not reduced for kidneys; maintenance by kidneys and levels (Rybak 2020, max 3 g).'),
 ('1,000 mg, reduced for CrCl 25', False, 'Loads are not reduced for kidneys.'),
 ('15 mg/kg (1,200 mg) every 12 hours', False, 'Maintenance style dosing; too frequent for CrCl 25.'),
 ('3,500 mg (about 45 mg/kg) once', False, 'Above the 3 g max.')],
('mx02', 1): [
 ('Full first dose now; adjust maintenance', True, 'For CrCl 25, to avoid neurotoxicity.'),
 ('Continue 2 g q8h for the whole course', False, 'Accumulation and neurotoxicity risk.'),
 ('Halve the first dose to 1 g now', False, 'First doses are not reduced.'),
 ('Hold cefepime until CrCl improves', False, 'Never delay antibiotics in shock.')],
('mx02', 2): [
 ('Hydrocortisone 200 mg/day', True, 'Norepinephrine 0.25 or more for over 4 hours.'),
 ('Vasopressin added, not more norepinephrine', True, ''),
 ('Stress ulcer prophylaxis (shock)', True, ''),
 ('Tight glucose 80 to 110 mg/dL', False, 'Target 140 to 180.'),
 ('Dexamethasone 6 mg daily for 10 days', False, 'The COVID 19 regimen.')],
('mx03', 0): [
 ('4F-PCC; SBP about 140 (not below 130)', True, 'ICH 2022; andexanet withdrawn from the US in 2025.'),
 ('Vitamin K 10 mg IV; SBP below 110', False, 'Warfarin reversal; too low a BP target.'),
 ('Andexanet alfa; SBP below 160', False, 'Withdrawn from the US market.'),
 ('Idarucizumab 5 g; SBP about 140', False, 'Dabigatran only.')],
('mx03', 1): [
 ('Should have been 2.5 mg BID (3 of 3 criteria)', True, 'Age 80+, weight 60 kg or less, SCr 1.5+.'),
 ('Correct: only 2 of 3 criteria are met', False, 'All three are met.'),
 ('Should have been 2.5 mg daily', False, 'Not an AF dose.'),
 ('Should have been stopped for SCr 1.6', False, 'Apixaban is still used; dose reduced.')],
('mx03', 2): [
 ('24 to 48 h after the bleed is stable', True, 'Heparin or enoxaparin (ICH 2022).'),
 ('Never after any ICH, for life', False, 'VTE risk is high; prophylaxis is reasonable.'),
 ('Full dose apixaban on day 2', False, 'Treatment dose is a different decision.'),
 ('Only after 14 days in hospital', False, 'Earlier is reasonable once stable.')],
('mx04', 0): [
 ('Calcium, then insulin + dextrose, then removal', True, 'Consider 5 units with kidney injury; binder, dialysis.'),
 ('Calcium alone; it lowers the potassium', False, 'Calcium stabilizes but does not lower K.'),
 ('Binder alone; it works within minutes', False, 'Binders take hours.'),
 ('Insulin 20 units IV with no dextrose', False, 'Hypoglycemia risk.')],
('mx04', 1): [
 ('Rocuronium; avoid succinylcholine', True, 'Crush injury after 24 to 48 hours and K 6.8.'),
 ('Succinylcholine 1.5 mg/kg', False, 'Raises K further; arrest risk.'),
 ('Succinylcholine at half dose', False, 'Still raises potassium.'),
 ('Vecuronium 0.01 mg/kg', False, 'A priming dose only.')],
('mx04', 2): [
 ('Ask for a non nephrotoxic option; levels if continued', True, 'Rhabdomyolysis and falling urine output.'),
 ('Continue the same gentamicin dose', False, 'Nephrotoxicity risk.'),
 ('Raise gentamicin for better bone penetration', False, 'Raises toxicity.'),
 ('Stop all antibiotics for the fracture', False, 'Coverage is still needed.')],
('mx05', 0): [
 ('No: replace K to 3.5+, and Mg, first', True, '2024 consensus.'),
 ('Yes: start insulin with KCl in the fluids', False, 'K below 3.5 risks arrhythmia with insulin.'),
 ('Yes: K above 3.0 is enough to start', False, 'Threshold is 3.5.'),
 ('Yes: give a 10 unit bolus first', False, 'No bolus, and K is too low.')],
('mx05', 1): [
 ('QTc 510, low K and Mg, plus QT drugs', True, 'Azithromycin and ondansetron prolong QT: torsades risk.'),
 ('Ceftriaxone with calcium containing fluids', False, 'A neonatal concern, not adult.'),
 ('Insulin drip with dextrose fluids', False, 'Standard DKA care.'),
 ('Azithromycin and ceftriaxone duplication', False, 'Different coverage; not duplicates.')],
('mx05', 2): [
 ('Ceftriaxone plus doxycycline', True, 'ATS/IDSA alternative when a macrolide should be avoided.'),
 ('Levofloxacin 750 mg alone', False, 'Fluoroquinolones also prolong QT.'),
 ('Ceftriaxone plus moxifloxacin', False, 'QT prolonging and duplicate.'),
 ('Ceftriaxone plus clarithromycin', False, 'Another QT prolonging macrolide.')],
('mx06', 0): [
 ('Enoxaparin', True, ''),
 ('Warfarin', True, ''),
 ('Unfractionated heparin', True, 'Not transferred into milk.'),
 ('Apixaban', False, 'Limited data; avoid while breastfeeding (ASH).'),
 ('Rivaroxaban', False, 'Limited data; avoid while breastfeeding.')],
('mx06', 1): [
 ('Labetalol, nifedipine ER or enalapril', True, 'ACOG; enalapril is compatible with breastfeeding.'),
 ('Lisinopril is contraindicated after pregnancy', False, 'ACE inhibitors are avoided in pregnancy, not postpartum.'),
 ('Atenolol, preferred for breastfeeding', False, 'Concentrates in milk; less preferred.'),
 ('Methyldopa, preferred postpartum', False, 'Linked to postpartum depression; not first choice postpartum.')],
('mx06', 2): [
 ('Avoid codeine and tramadol', True, 'Scheduled acetaminophen and ibuprofen; short low dose oxycodone if needed (FDA 2017).'),
 ('Fine at standard doses for 7 days', False, 'Ultrarapid metabolizers expose the infant to morphine.'),
 ('Fine if the infant is over 1 week old', False, 'Risk at any age while breastfeeding.'),
 ('Switch to tramadol 50 mg every 6 hours', False, 'Same FDA warning.')],
('mx07', 0): [
 ('No: Kcentra contains heparin; HIT contraindicates', True, 'Kcentra label.'),
 ('Yes: heparin content is too small to matter', False, 'Labeled contraindication.'),
 ('Yes: HIT from 2023 is no longer relevant', False, 'Label lists known HIT; follow policy.'),
 ('Yes: if given with vitamin K', False, 'Does not remove the heparin.')],
('mx07', 1): [
 ('Vitamin K 10 mg IV plus plasma (FFP)', True, 'Team weighs volume; or a heparin free factor product if stocked.'),
 ('Vitamin K 10 mg IV only; wait 24 hours', False, 'Too slow for a bleed.'),
 ('Protamine 50 mg IV', False, 'Reverses heparin, not warfarin.'),
 ('Andexanet alfa', False, 'Withdrawn, and not for warfarin.')],
('mx07', 2): [
 ('Heparin flushes and heparin coated catheters', True, ''),
 ('Enoxaparin', True, 'Cross reacts with HIT antibodies.'),
 ('Heparin containing products like Kcentra', True, ''),
 ('Fondaparinux', False, 'Used as an HIT alternative; little cross reactivity.'),
 ('Argatroban', False, 'An HIT treatment.')],
('mx08', 0): [
 ('Linezolid myelosuppression (after ~2 weeks)', True, ''),
 ('HIT possible; timing and other cause lower 4Ts', True, ''),
 ('Sertraline induced thrombocytopenia', False, 'Rare; not the leading cause.'),
 ('Lab error only; no action', False, 'Recheck, but treat as real.'),
 ('Pseudothrombocytopenia from EDTA', False, 'Possible but not a leading cause here.')],
('mx08', 1): [
 ('Serotonin syndrome: monitor', True, 'Linezolid is a weak MAO inhibitor; discuss with the team.'),
 ('QT prolongation is the main concern', False, 'Serotonin is the classic warning.'),
 ('Linezolid lowers sertraline levels', False, 'Not the interaction.'),
 ('No interaction between the two', False, 'FDA warning exists.')],
('mx08', 2): [
 ('Score 4Ts, test if needed, ask ID', True, 'HIT testing if intermediate; ask ID about an alternative to linezolid.'),
 ('Transfuse platelets to above 150,000', False, 'No bleeding; platelets can worsen HIT clots.'),
 ('Start argatroban for all thrombocytopenia', False, 'Only if HIT is likely.'),
 ('Stop heparin and do nothing else', False, 'Incomplete.')],
}

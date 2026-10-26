# Module 7 (Critical Care) rewrites.
R = {
('cc01', 0): [
 ('MAP of 65 mmHg', True, 'SSC 2021 initial target.'),
 ('MAP of 80 to 85 mmHg', False, 'SEPSISPAM: higher targets did not lower mortality; more arrhythmia.'),
 ('MAP of 55 to 60 mmHg', False, 'Permissive targets of 60 to 65 were studied in older adults (65 trial), not below 60.'),
 ('Systolic BP of 90 mmHg', False, 'A screening cutoff (qSOFA uses 100); SSC targets MAP.')],
('cc01', 1): [
 ('Add vasopressin 0.03 units/min', True, 'SSC 2021: usually at norepinephrine 0.25 to 0.5 mcg/kg/min.'),
 ('Switch norepinephrine to dopamine', False, 'Dopamine causes more arrhythmias (SOAP II).'),
 ('Add phenylephrine as second agent', False, 'Not the SSC second agent; may lower cardiac output.'),
 ('Add vasopressin 0.1 units/min', False, 'Doses above 0.03 to 0.04 units/min raise ischemia risk.')],
('cc01', 2): [
 ('Hydrocortisone 200 mg/day IV', True, '50 mg every 6 hours or an infusion (SSC 2021).'),
 ('Dexamethasone 6 mg IV daily', False, 'The COVID 19 (RECOVERY) dose, not septic shock.'),
 ('Methylprednisolone 1 g IV daily', False, 'A pulse dose for autoimmune disease.'),
 ('Hydrocortisone 100 mg IV once', False, 'A single dose; SSC uses 200 mg/day until the pressor is off.')],
('cc01', 3): [
 ('Dobutamine (or switch to epinephrine)', True, 'SSC 2021 for low output with adequate MAP.'),
 ('Raise vasopressin to 0.06 units/min', False, 'Vasopressin raises tone, not contractility.'),
 ('Add phenylephrine 100 mcg/min', False, 'Pure alpha; can lower output further.'),
 ('Milrinone 50 mcg/kg bolus', False, 'The bolus drops blood pressure; not the SSC suggestion.')],
('cc02', 0): [
 ('Phentolamine 5 to 10 mg in 10 mL NS, infiltrated', True, 'As soon as possible, into the area (norepinephrine label).'),
 ('Hyaluronidase 150 units, infiltrated', False, 'For non vasopressor extravasation such as hyperosmolar fluids.'),
 ('Phentolamine 5 to 10 mg IV push', False, 'Given locally, not systemically.'),
 ('Dexrazoxane 1,000 mg/m2 IV', False, 'For anthracycline extravasation.')],
('cc02', 1): [
 ('Stop, aspirate, remove, restart elsewhere, elevate', True, 'Then document and monitor the site.'),
 ('Stop, apply warm compresses, keep the line', False, 'The catheter must come out; restart at another site.'),
 ('Slow the rate by half and keep watching', False, 'Ischemia progresses.'),
 ('Stop, apply ice packs, restart same site', False, 'Cold worsens vasoconstriction; never reuse the site.')],
('cc03', 0): [
 ('Analgesia first, using CPOT or BPS', True, 'PADIS 2018.'),
 ('Deep sedation with a benzodiazepine', False, 'PADIS favors light sedation and non benzodiazepines.'),
 ('Haloperidol 5 mg IV for agitation', False, 'Treats agitation before finding pain.'),
 ('Restraints and a sedation holiday', False, 'Assess and treat pain first.')],
('cc03', 1): [
 ('Propofol or dexmedetomidine, light sedation', True, 'PADIS 2018.'),
 ('Lorazepam infusion, RASS of minus 3', False, 'Benzodiazepines and deep sedation worsen outcomes.'),
 ('Midazolam infusion, RASS of 0 to minus 1', False, 'Light target, but benzodiazepine is not preferred.'),
 ('Ketamine infusion as first line', False, 'An adjunct, not the preferred sedative.')],
('cc03', 2): [
 ('No; PADIS advises against routine use', True, 'For prevention or treatment of delirium.'),
 ('Yes, haloperidol 2 mg IV every 8 hours', False, 'Routine use not recommended (also REDUCE trial).'),
 ('Yes, quetiapine 50 mg at bedtime', False, 'Same recommendation applies.'),
 ('Only if the CAM ICU screen is negative', False, 'Not a prevention strategy.')],
('cc04', 0): [
 ('Propofol infusion syndrome (PRIS)', True, 'Risk above about 4 mg/kg/h (67 mcg/kg/min) for over 48 h.'),
 ('Sepsis related lactic acidosis only', False, 'Rising CK and triglycerides point to propofol.'),
 ('Refeeding syndrome', False, 'Low phosphate, not CK and triglycerides.'),
 ('Neuroleptic malignant syndrome', False, 'Needs a dopamine blocker exposure.')],
('cc04', 1): [
 ('Stop propofol and change sedative', True, 'Supportive care; consider dialysis.'),
 ('Lower propofol by 10 mcg/kg/min', False, 'PRIS needs the drug stopped.'),
 ('Keep propofol; add a statin', False, 'No role.'),
 ('Keep propofol; add fenofibrate', False, 'Treats triglycerides, not PRIS.')],
('cc04', 2): [
 ('Triglycerides, CK, lipase; count lipid calories', True, '1.1 kcal/mL from the lipid.'),
 ('Serum sodium and osmolality daily', False, 'Not a propofol issue.'),
 ('TSH and free T4 weekly', False, 'Not a propofol issue.'),
 ('Serum levels of propofol', False, 'Not available or useful clinically.')],
('cc05', 0): [
 ('Calcium gluconate 1 g IV over 2 to 5 minutes', True, 'Repeat if ECG changes persist.'),
 ('Sodium zirconium cyclosilicate 10 g PO', False, 'Removes potassium over hours; does not protect the heart.'),
 ('Regular insulin 10 units IV with dextrose', False, 'Shifts potassium but does not stabilize the membrane.'),
 ('Sodium bicarbonate 50 mEq IV', False, 'Weak effect without acidosis; not first.')],
('cc05', 1): [
 ('Insulin 5 units IV + dextrose 25 g', True, 'Lower dose for kidney failure lowers hypoglycemia.'),
 ('Insulin 10 units IV + no dextrose', False, 'Glucose is only 110; hypoglycemia risk.'),
 ('Insulin 20 units IV + dextrose 25 g', False, 'Far too much insulin.'),
 ('Insulin 10 units SC + dextrose 25 g', False, 'SC absorption is unreliable in emergencies.')],
('cc05', 2): [
 ('A binder (SZC 10 g or patiromer 8.4 g) plus dialysis', True, 'Calcium, insulin and albuterol do not remove potassium.'),
 ('Calcium gluconate repeated every hour', False, 'Calcium stabilizes, does not remove.'),
 ('Albuterol 10 to 20 mg nebulized', False, 'Shifts potassium into cells.'),
 ('Insulin infusion until potassium is 4', False, 'Shifts potassium into cells.')],
('cc06', 0): [
 ('3% saline 100 to 150 mL over 10 to 20 min, up to 3x', True, 'Aim for a 4 to 6 mmol/L rise.'),
 ('3% saline 500 mL over 1 hour', False, 'Too much too fast; overcorrection risk.'),
 ('Normal saline 1 L over 8 hours', False, 'Too slow for a seizure; may worsen SIADH.'),
 ('Fluid restriction to 1 L per day', False, 'For chronic, asymptomatic SIADH.')],
('cc06', 1): [
 ('About 10 in 24 h; 8 per 24 h if high risk', True, 'High risk: alcohol use, low K, malnutrition, liver disease.'),
 ('About 12 in 24 h and 18 in 48 h', False, 'An older, higher limit.'),
 ('About 4 in 24 h for all patients', False, 'That is the initial emergency goal, not the limit.'),
 ('About 20 in 24 h if symptomatic', False, 'Causes osmotic demyelination.')],
('cc06', 2): [
 ('Stop hypertonic; give D5W, with or without desmopressin', True, 'Re lower per protocol.'),
 ('Continue 3% saline at a slower rate', False, 'Already past the limit.'),
 ('Switch to normal saline 100 mL/h', False, 'Still raises sodium.'),
 ('Start tolvaptan 15 mg PO', False, 'Raises sodium further.')],
('cc07', 0): [
 ('Insulin above 180; target 140 to 180 mg/dL', True, 'ADA Standards; NICE SUGAR.'),
 ('Target 80 to 110 mg/dL', False, 'NICE SUGAR: more deaths and hypoglycemia.'),
 ('Target 110 to 140 mg/dL for all', False, 'May suit select patients only, without hypoglycemia.'),
 ('Insulin above 250; target 200 to 250', False, 'Too loose.')],
('cc08', 0): [
 ('No: replace K first until K is 3.5 or more', True, '2024 consensus.'),
 ('Yes, with 20 mEq/L of KCl in fluids', False, 'Below 3.5 insulin can drop K dangerously.'),
 ('Yes, if potassium is above 3.0', False, 'The threshold is 3.5.'),
 ('Yes; insulin raises the potassium', False, 'Insulin drives K into cells.')],
('cc08', 1): [
 ('Regular insulin 0.1 units/kg/h (7 units/h)', True, 'No routine bolus.'),
 ('Regular insulin 0.14 units/kg/h (10 units/h)', False, 'The older 2009 no bolus rate; the 2024 consensus uses 0.1.'),
 ('Regular insulin 0.05 units/kg/h (3.5 units/h)', False, 'The rate once glucose is near 250.'),
 ('Insulin glargine 0.3 units/kg SC', False, 'Basal insulin, not the initial DKA drip.')],
('cc08', 2): [
 ('Add D5 or D10; lower insulin to 0.05 units/kg/h', True, 'Keep insulin until ketones clear.'),
 ('Stop insulin; restart at glucose 300', False, 'Ketones keep building.'),
 ('Keep 0.1 units/kg/h with no dextrose', False, 'Hypoglycemia risk.'),
 ('Switch now to sliding scale insulin', False, 'DKA is not resolved.')],
('cc08', 3): [
 ('DKA resolved; SC basal 1 to 2 h before stopping', True, 'BHB below 0.6 and pH 7.3+ or bicarbonate 18+.'),
 ('Glucose below 200 on two checks', False, 'Glucose falls before ketones clear.'),
 ('Anion gap below 20 mEq/L', False, 'Use the consensus resolution criteria.'),
 ('After 24 hours of the drip', False, 'Time alone does not decide.')],
('cc09', 0): [
 ('40 mEq/h is far above peripheral 10 mEq/h', True, 'Usual peripheral limit; check local policy.'),
 ('KCl must be given in D5W only', False, 'Diluent is not the issue.'),
 ('40 mEq/h is fine for K of 2.9', False, 'Unsafe peripherally.'),
 ('Use KCl 40 mEq IV push instead', False, 'Never push KCl.')],
('cc09', 1): [
 ('Replace magnesium too', True, 'Low Mg makes K hard to correct.'),
 ('Replace phosphate first', False, 'Not the linked deficit.'),
 ('Give calcium gluconate 1 g', False, 'Not indicated.'),
 ('Check a cortisol level first', False, 'Not needed.')],
('cc09', 2): [
 ('Never', True, 'ISMP high alert; fatal.'),
 ('Yes, 10 mEq over 5 minutes', False, 'Fatal arrhythmia.'),
 ('Yes, in cardiac arrest only', False, 'Still never pushed.'),
 ('Yes, if diluted to 10 mL first', False, 'Dilution in a syringe does not make it safe.')],
('cc10', 0): [
 ('B: shock', True, ''),
 ('C: coagulopathy and chronic liver disease', True, ''),
 ('A: ventilator alone with tube feeds', False, 'SCCM/ASHP 2024 suggests against for patients without risk factors on enteral feeds.'),
 ('A: any ICU stay longer than 48 hours', False, 'ICU stay alone is not an indication.'),
 ('All three, because ICU patients bleed', False, 'Risk based, not universal.')],
('cc10', 1): [
 ('When the risk resolves or at ICU transfer', True, 'Avoid continuing at discharge.'),
 ('At hospital discharge only', False, 'Often continued by mistake.'),
 ('After 6 weeks of treatment', False, 'Not a prophylaxis duration.'),
 ('Never; continue for life', False, 'Long term PPI risks.')],
('cc11', 0): [
 ('K 7.0 with wide QRS: calcium now', True, ''),
 ('The pressor bag running out soon', False, 'Second.'),
 ('The PPI IV switch question', False, 'Routine.'),
 ('The TPN label for tomorrow', False, 'Routine.')],
('cc11', 1): [
 ('Prepare the replacement pressor bag', True, 'Before the current one runs out.'),
 ('Answer the PPI switch question', False, 'Routine.'),
 ('Fix the TPN label for tomorrow', False, 'Routine.'),
 ('Recheck the potassium in 4 hours', False, 'Planned follow up, not the next urgent task.')],
}

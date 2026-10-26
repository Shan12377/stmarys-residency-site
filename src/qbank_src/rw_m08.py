# Module 8 (Codes) rewrites.
R = {
('cd01', 0): [
 ('Epinephrine 1 mg IV now, then every 3 to 5 min', True, 'Non shockable rhythm: give as soon as possible (AHA).'),
 ('Epinephrine 1 mg IV after the second shock', False, 'That timing is for VF/pVT; asystole is not shocked.'),
 ('Atropine 1 mg IV every 3 to 5 min, max 3 mg', False, 'Removed from arrest algorithms in 2010; it is a bradycardia drug.'),
 ('Vasopressin 40 units IV in place of epinephrine', False, 'Removed from the adult algorithm in 2015; no added benefit.')],
('cd01', 1): [
 ('Call out epinephrine timing ("Epi due in 1 minute")', True, ''),
 ('Prepare the next doses; prompt the H\'s and T\'s', True, ''),
 ('Confirm weight and allergies; help record drugs and times', True, ''),
 ('Run the code and assign compressor roles', False, 'The code leader runs the code.'),
 ('Decide when to stop resuscitation', False, 'A physician decision.')],
('cd02', 0): [
 ('After the second shock, then every 3 to 5 min', True, 'AHA: after initial defibrillation attempts fail.'),
 ('Before the first shock, then every 3 to 5 min', False, 'Shock first in VF; that early timing is for non shockable rhythms.'),
 ('After the third shock, with amiodarone 300 mg', False, 'The third shock is when amiodarone or lidocaine is added.'),
 ('Only after 10 minutes of CPR with no ROSC', False, 'No such delay.')],
('cd02', 1): [
 ('Amiodarone 300 mg IV/IO push, then 150 mg', True, ''),
 ('Lidocaine 1 to 1.5 mg/kg, then 0.5 to 0.75 mg/kg', True, ''),
 ('Amiodarone 150 mg over 10 minutes, then 1 mg/min', False, 'The stable VT and post ROSC dosing.'),
 ('Procainamide 20 to 50 mg/min, max 17 mg/kg', False, 'For stable wide complex tachycardia, not arrest.'),
 ('Adenosine 6 mg, then 12 mg', False, 'For stable SVT.')],
('cd02', 2): [
 ('No; only for specific causes', True, 'Hyperkalemia, torsades, tricyclic overdose, known acidosis.'),
 ('Yes, calcium chloride 1 g every code', False, 'Routine calcium is not helpful (and may harm).'),
 ('Yes, bicarbonate 1 mEq/kg every 10 min', False, 'Routine bicarbonate is not recommended.'),
 ('Yes, magnesium 2 g in every VF arrest', False, 'Only for torsades.')],
('cd03', 0): [
 ('Calcium chloride 1 g IV (or gluconate 3 g)', True, ''),
 ('Regular insulin 10 units IV with dextrose 25 g', True, ''),
 ('Sodium bicarbonate 50 mEq IV if acidotic', True, ''),
 ('Calcium gluconate 1 g as the full arrest dose', False, 'Gluconate has a third of the calcium; 3 g matches 1 g chloride.'),
 ('Sodium zirconium cyclosilicate 10 g by tube', False, 'Works over hours; not an arrest drug.')],
('cd04', 0): [
 ('Magnesium sulfate 1 to 2 g IV push', True, 'Torsades in arrest.'),
 ('Magnesium sulfate 4 to 6 g IV over 20 min', False, 'The eclampsia load.'),
 ('Procainamide 20 to 50 mg/min IV', False, 'Prolongs QT further.'),
 ('Amiodarone 300 mg IV push alone', False, 'Prolongs QT; magnesium is the drug for torsades.')],
('cd04', 1): [
 ('Stop QT drugs; replace K and Mg; check CredibleMeds', True, 'Keep K above 4 and Mg above 2 commonly.'),
 ('Continue methadone; stop only ondansetron', False, 'Review both; methadone dose or alternative must be addressed.'),
 ('Swap ondansetron for haloperidol for nausea', False, 'Also prolongs QT.'),
 ('Switch ondansetron to droperidol for nausea', False, 'Droperidol carries a boxed QT warning.')],
('cd05', 0): [
 ('Bag mask breaths and naloxone 0.4 mg IV', True, 'Repeat or increase to 2 mg; 4 mg intranasal if no IV.'),
 ('Naloxone 2 mg IV only, no ventilation', False, 'Ventilate first; large doses cause abrupt withdrawal.'),
 ('Flumazenil 0.2 mg IV over 30 seconds', False, 'Reverses benzodiazepines, not opioids.'),
 ('Sternal rub and a recheck in 15 minutes', False, 'RR 4 needs treatment now.')],
('cd05', 1): [
 ('Naloxone lasts 30 to 90 min; opioids can last longer', True, 'Repeat doses or an infusion may be needed.'),
 ('Naloxone lasts 12 to 24 hours like methadone', False, 'Methadone is the long one.'),
 ('Naloxone is cleared faster in kidney failure', False, 'Duration is short in everyone.'),
 ('Naloxone is inactivated by the PCA opioid', False, 'Not the mechanism.')],
('cd06', 0): [
 ('Lipid 20%: 1.5 mL/kg bolus, then 0.25 mL/kg/min', True, '105 mL over 2 to 3 minutes for 70 kg (ASRA).'),
 ('Lipid 20%: 15 mL/kg bolus, then 2.5 mL/kg/min', False, 'Ten times the dose.'),
 ('Propofol 1 mg/kg IV for the seizure', False, 'Propofol is a lipid but too little and depresses the heart.'),
 ('Naloxone 0.4 mg IV, repeated every 2 min', False, 'Not an opioid toxicity.')],
('cd06', 1): [
 ('Smaller doses: 1 mcg/kg or less', True, 'ASRA LAST checklist.'),
 ('Standard 1 mg every 3 to 5 minutes', False, 'Large epinephrine doses worsen LAST outcomes.'),
 ('Double: 2 mg every 3 to 5 minutes', False, 'Harmful.'),
 ('Replace epinephrine with vasopressin', False, 'Vasopressin is not recommended in LAST.')],
('cd07', 0): [
 ('Sodium bicarbonate 1 to 2 mEq/kg IV, repeat', True, 'To narrow the QRS; aim pH 7.45 to 7.55.'),
 ('Procainamide 20 to 50 mg/min IV', False, 'Class IA; worsens sodium channel block.'),
 ('Physostigmine 1 to 2 mg IV slowly', False, 'Contraindicated in TCA overdose (seizures, asystole).'),
 ('Flumazenil 0.2 mg IV for co ingestion', False, 'Can trigger seizures in TCA overdose.')],
('cd08', 0): [
 ('Atropine 1 mg IV every 3 to 5 min, max 3 mg', True, 'AHA 2020.'),
 ('Atropine 0.5 mg IV every 3 to 5 min, max 3 mg', False, 'The older dose before 2020.'),
 ('Adenosine 6 mg rapid IV push', False, 'For SVT; slows the heart further.'),
 ('Epinephrine 1 mg IV push every 3 min', False, 'The arrest dose.')],
('cd08', 1): [
 ('Epinephrine 2 to 10 mcg/min, dopamine, or pacing', True, 'Dopamine 5 to 20 mcg/kg/min.'),
 ('Isoproterenol 20 mcg/min as first choice', False, 'Possible, but not the AHA first options.'),
 ('Dopamine 1 to 3 mcg/kg/min "renal dose"', False, 'Too low; no renal benefit.'),
 ('Atropine 1 mg more, above the 3 mg max', False, 'Beyond 3 mg adds no effect.')],
('cd09', 0): [
 ('Rapid IV push, then an immediate saline flush', True, 'Half life under 10 seconds.'),
 ('Slow IV push over 1 to 2 minutes, no flush', False, 'It breaks down before reaching the heart.'),
 ('IV piggyback over 15 minutes', False, 'Never works this way.'),
 ('Rapid push into the lower leg vein', False, 'Use a large proximal (antecubital) vein.')],
('cd09', 1): [
 ('3 mg first (instead of 6 mg)', True, 'Central line or on dipyridamole; heart transplant also lower.'),
 ('12 mg first (instead of 6 mg)', False, '12 mg is the second peripheral dose.'),
 ('6 mg first, same as peripheral', False, 'Central lines deliver it faster and stronger.'),
 ('0.1 mg/kg first, max 6 mg', False, 'The pediatric dose.')],
('cd10', 0): [
 ('Epinephrine 0.5 mg IM (1 mg/mL), outer thigh', True, 'Repeat every 5 to 15 minutes.'),
 ('Diphenhydramine 50 mg IV as the first drug', False, 'Antihistamines do not treat shock or airway swelling.'),
 ('Epinephrine 1 mg IV push (0.1 mg/mL)', False, 'The arrest dose; dangerous with a pulse.'),
 ('Epinephrine 0.5 mg SC into the upper arm', False, 'SC is slower; IM thigh is preferred.')],
('cd10', 1): [
 ('Epinephrine infusion and IV fluids', True, 'Refractory anaphylaxis, with the team.'),
 ('More diphenhydramine 50 mg IV', False, 'Does not treat shock.'),
 ('Methylprednisolone 125 mg IV alone', False, 'Slow; does not treat shock.'),
 ('Famotidine 20 mg IV and observe', False, 'An adjunct only.')],
('cd11', 0): [
 ('Dantrolene 2.5 mg/kg IV, repeat until resolved', True, 'MHAUS.'),
 ('Dantrolene 1 mg/kg IV once, max 10 mg/kg', False, '1 mg/kg is too low a starting dose; repeat as needed.'),
 ('Acetaminophen 1 g IV and cooling only', False, 'Does not stop the muscle reaction.'),
 ('Bromocriptine 2.5 mg by tube', False, 'For neuroleptic malignant syndrome.')],
('cd11', 1): [
 ('Where the MH cart is and which product you stock', True, 'Ryanodex reconstitutes much faster than Dantrium.'),
 ('That dantrolene must be refrigerated', False, 'Stored at room temperature.'),
 ('That dantrolene needs a 0.2 micron filter', False, 'Not the key detail.'),
 ('That dantrolene is only given IM', False, 'Given IV.')],
('cd12', 0): [
 ('SBP at least 90 and MAP at least 65', True, ''),
 ('SpO2 about 92 to 98%, avoiding hyperoxia', True, ''),
 ('Temperature control with fever prevention', True, 'Keep below 37.5 °C.'),
 ('SpO2 100% on FiO2 1.0 for 24 hours', False, 'Hyperoxia may harm the brain.'),
 ('Glucose 80 to 110 mg/dL', False, 'Too tight; hypoglycemia risk.')],
('cd12', 1): [
 ('1 mg/min for 6 h, then 0.5 mg/min for 18 h', True, 'After the 150 mg load if not already given.'),
 ('0.5 mg/min for 6 h, then 1 mg/min for 18 h', False, 'Reversed.'),
 ('2 mg/min for 6 h, then 1 mg/min for 18 h', False, 'Double.'),
 ('10 mg/min for 15 min, then 1 mg/min', False, 'Confuses the 150 mg over 10 min load rate.')],
}

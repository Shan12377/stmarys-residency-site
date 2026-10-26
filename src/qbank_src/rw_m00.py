# Module 0 rewrites (Pharmacy Decoder rules).
R = {
('h01', 0): [
 ('Patient first: age, weight, allergies with reactions, pregnancy', True, 'Every dose decision depends on who the patient is.'),
 ('Indication first, then weight and kidney function later', False, 'Indication is step two; without patient basics (weight, allergy) you cannot judge it.'),
 ('Drug first: check the dose against the usual range', False, 'Checking the drug before the patient misses wrong patient, allergy and weight errors.'),
 ('Duplicates first: scan the MAR for other anticoagulants', False, 'Duplicate checking is a later step in the routine.')],
('h01', 1): [
 ('Prophylaxis and treatment doses differ several fold', True, '40 mg daily (prophylaxis) vs 1 mg/kg every 12 hours (treatment).'),
 ('Indication decides the needle size and injection site', False, 'Administration technique does not depend on indication.'),
 ('Indication decides whether anti Xa levels are routine', False, 'Anti Xa levels are for special populations (kidneys, pregnancy, extremes of weight), not set by indication alone.'),
 ('Indication only matters for billing and coding', False, 'It drives the dose.')],
('h01', 2): [
 ('Serum creatinine, to estimate CrCl', True, 'Enoxaparin dosing changes below CrCl 30.'),
 ('Platelets', True, 'Baseline for HIT and bleeding risk.'),
 ('aPTT, to set the enoxaparin dose', False, 'aPTT monitors unfractionated heparin; enoxaparin barely changes it.'),
 ('INR, to set the enoxaparin dose', False, 'INR monitors warfarin.'),
 ('Hemoglobin A1c', False, 'Not relevant to anticoagulant dosing.')],
('h01', 3): [
 ('Verify the order as written', True, 'CrCl 62, normal platelets, no epidural, no duplicates: 40 mg daily is correct.'),
 ('Change it to 30 mg daily for her age', False, '30 mg daily is the prophylaxis dose when CrCl is below 30, not an age rule.'),
 ('Change it to 30 mg every 12 hours', False, '30 mg every 12 hours is an orthopedic or trauma prophylaxis regimen.'),
 ('Change it to 1 mg/kg every 24 hours', False, 'That is the treatment dose when CrCl is below 30.')],
('h02', 0): [
 ('Cockcroft Gault creatinine clearance', True, 'Most labels base renal adjustments on Cockcroft Gault.'),
 ('CKD-EPI eGFR (2021, race free)', False, 'eGFR stages kidney disease; many labels and pharmacy protocols still dose by Cockcroft Gault.'),
 ('MDRD eGFR', False, 'An older staging equation, not the label dosing standard.'),
 ('Schwartz equation', False, 'Used for children.')],
('h02', 1): [
 ('About 49 mL/min', True, '(140 minus 70) x 80 / (72 x 1.6) = 48.6.'),
 ('About 44 mL/min', False, 'That uses ideal body weight (73 kg) instead of the actual weight asked for.'),
 ('About 41 mL/min', False, 'That applies the 0.85 female factor to a male patient.'),
 ('About 78 mL/min', False, 'That uses an SCr of 1.0, a rounding practice sometimes used for low SCr in older adults, not for 1.6.')],
('h02', 2): [
 ('Obesity, very low weight, or a weight that looks wrong', True, 'Choose actual, ideal or adjusted weight per protocol; confirm the weight.'),
 ('Only when the patient is over 65 years old', False, 'Age is already in the formula.'),
 ('Only when SCr is above 2.0 mg/dL', False, 'SCr does not decide which weight to use.'),
 ('Only for drugs dosed in mg/kg', False, 'Weight choice affects CrCl for every renally dosed drug.')],
('h03', 0): [
 ('Ask what the reaction actually was', True, 'Most penicillin labels are not true allergy; the reaction decides the next step.'),
 ('Change to vancomycin to avoid any cross reactivity', False, 'Vancomycin is less effective for MSSA and strep skin infections.'),
 ('Change to clindamycin as the standard alternative', False, 'Clindamycin is for confirmed severe allergy; resistance is common.'),
 ('Verify cefazolin; cross reactivity is always zero', False, 'Cefazolin cross reactivity is very low, but you still clarify and document.')],
('h03', 1): [
 ('Verify cefazolin; record the rash and the tolerated cephalexin', True, 'Documentation helps every future prescriber.'),
 ('Request vancomycin, since any rash means avoid beta lactams', False, 'A benign childhood rash is low risk.'),
 ('Hold the antibiotic until an allergist sees the patient', False, 'Delays treatment for a low risk history.'),
 ('Remove the allergy entirely without telling anyone', False, 'Delabeling follows policy and documentation.')],
('h04', 0): [
 ('The prescriber, or the covering prescriber at night', True, 'Only a prescriber (or a protocol) changes an order.'),
 ('The charge nurse, after talking with you', False, 'Nurses can relay information but do not change orders.'),
 ('You alone, because pharmacists can always change doses', False, 'Only with a pharmacy to dose protocol or collaborative agreement.'),
 ('The pharmacy technician entering the order', False, 'Not within technician scope.')],
('h04', 1): [
 ('Check the policy: many hospitals have pharmacy to dose', True, 'If St. Mary\'s protocol covers vancomycin, you can adjust and document.'),
 ('Yes: Florida law lets any pharmacist change any dose', False, 'Changes need a protocol or prescriber authorization.'),
 ('No: pharmacists may never change a dose in Florida', False, 'Pharmacy to dose protocols exist.'),
 ('Only after the attending signs a new order each day', False, 'Protocols remove that need.')],
('h04', 2): [
 ('Explain the risk once more with a source, then escalate', True, 'Chain of command when patient safety is at stake.'),
 ('Verify it, because the prescriber takes the responsibility', False, 'You share responsibility for what you verify.'),
 ('Delete the order and tell the nurse to hold the drug', False, 'Never delete an order unilaterally.'),
 ('Verify it but write a note that you disagreed', False, 'Documentation does not protect the patient.')],
('h05', 0): [
 ('The MAR (medication administration record)', True, 'Shows what was given and when.'),
 ('The active order in the order profile', False, 'Shows what should be given, not what was.'),
 ('The dispensing cabinet removal log', False, 'Shows what was removed, not given.'),
 ('The pharmacy verification history', False, 'Shows what you verified.')],
('h05', 1): [
 ('Give the dose as soon as possible and retime the next dose', True, 'For time sensitive antibiotics, the missed dose matters most.'),
 ('File an event report first, then give the dose', False, 'Report after the patient is safe.'),
 ('Skip the dose and give the next one on schedule', False, 'A missed antibiotic dose can fail treatment.'),
 ('Give a double dose at the next scheduled time', False, 'Never double to catch up.')],
('h06', 0): [
 ('True emergencies using drugs on the approved override list', True, 'Joint Commission expects policies and override review.'),
 ('Any time the pharmacist has not verified within 15 minutes', False, 'Delay alone is not an emergency.'),
 ('Any drug, as long as a second nurse witnesses it', False, 'Witnessing is for controlled substance waste, not override rules.'),
 ('Never; every dose must be verified first', False, 'Overrides exist for emergencies.')],
('h06', 1): [
 ('Review the order as if not yet given, and follow up', True, 'Your review still matters for the next doses.'),
 ('Nothing, because the dose was already given', False, 'Future doses and errors still need review.'),
 ('Report the nurse for using override', False, 'Overrides in emergencies are appropriate.'),
 ('Reverse the dispense in the cabinet', False, 'Inventory fixes do not replace clinical review.')],
('h07', 0): [
 ('The code and the stroke alert together (call backup)', True, 'Both are life threatening and time critical.'),
 ('The STAT antibiotic, since first doses are time sensitive', False, 'Important, but after life threatening events.'),
 ('The crush question, since it takes 30 seconds', False, 'Fast does not beat life threatening.'),
 ('The queue in order received, to be fair to everyone', False, 'Triage by harm if delayed.')],
('h07', 1): [
 ('The new antibiotic order (time sensitive first dose)', True, ''),
 ('The discharge interaction question for tomorrow', False, 'Can wait.'),
 ('The crush question before the antibiotic', False, 'The first dose is more time sensitive.'),
 ('Documentation of the code before anything else', False, 'Document after time sensitive care.')],
('h07', 2): [
 ('Check the ISMP Do Not Crush list and the exact product', True, 'Extended release and enteric coated products are classic no crush.'),
 ('Check the drug\'s pregnancy category', False, 'Unrelated.'),
 ('Check Trissel\'s for compatibility', False, 'Trissel\'s covers IV compatibility, not crushing.'),
 ('Check the formulary price list', False, 'Unrelated.')],
('h08', 0): [
 ('Which drug, what concentration, and what else is in the line', True, 'Compatibility depends on all three.'),
 ('How long the heparin has been running', False, 'Not the compatibility question.'),
 ('The patient\'s weight and kidney function', False, 'Matters for dosing, not Y site compatibility.'),
 ('Whether the line is peripheral or central only', False, 'Line type matters for some drugs, but compatibility needs the drugs and concentrations.')],
('h08', 1): [
 ('Trissel\'s or the King Guide (or free Stabilis)', True, ''),
 ('LactMed', False, 'Breastfeeding reference.'),
 ('The ISMP Do Not Crush list', False, 'Oral dosage forms.'),
 ('NeoFax', False, 'Neonatal dosing.')],
('h08', 2): [
 ('No data: do not run them together; separate line or flush', True, 'Absence of data is treated as incompatible.'),
 ('No data: probably fine if the concentrations are low', False, 'Concentration can change compatibility, but no data means avoid.'),
 ('No data: run them together and watch for cloudiness', False, 'Precipitates can be invisible.'),
 ('No data: mix them in the same bag instead', False, 'Admixture compatibility is a separate, stricter question.')],
('h09', 0): [
 ('Errors with these drugs are more likely to cause harm', True, 'ISMP definition.'),
 ('They are the most often prescribed drugs', False, 'Frequency is not the definition.'),
 ('They need a second pharmacist to verify by law', False, 'Double checks are policy based, not a legal definition.'),
 ('They are all controlled substances', False, 'Many are not (insulin, heparin).')],
('h09', 1): [
 ('Standard concentrations matched to the pump library', True, ''),
 ('Independent double checks where policy requires them', True, ''),
 ('Premixed bags when available', True, ''),
 ('Custom concentrations for each patient\'s fluid needs', False, 'Custom concentrations defeat pump safety limits.'),
 ('Storing insulin vials next to heparin vials for speed', False, 'Look alike storage causes mix ups.')],
('h10', 0): [
 ('"U" can be misread as 0 or 4: write "units"', True, ''),
 ('A trailing zero (2.0 mg) can be misread as 20 mg', True, ''),
 ('"IV" must be written as "intravenous"', False, '"IV" is acceptable; "IU" is the Do Not Use item.'),
 ('"PRN" is on the Do Not Use list', False, 'PRN is acceptable.')],
('h10', 1): [
 ('A leading zero: 0.5 mg', True, ''),
 ('No zero: .5 mg', False, 'The decimal can be missed: read as 5 mg.'),
 ('A trailing zero: 0.50 mg', False, 'Trailing zeros are on the Do Not Use list.'),
 ('A fraction: 1/2 mg', False, 'Fractions invite misreading.')],
('h11', 0): [
 ('Yes: report near misses in St. Mary\'s reporting system', True, 'Near misses show system weaknesses for free.'),
 ('No: reports are only for errors that reached the patient', False, 'Near misses are reported too.'),
 ('Only if the prescriber agrees to the report', False, 'No permission needed.'),
 ('Only to ISMP, not internally', False, 'Internal reporting comes first; ISMP reporting is optional and voluntary.')],
('h12', 0): [
 ('Pending items, who you wait on, and what to do if no callback', True, 'Hand off what is pending, not what is done.'),
 ('Only what you finished, so nothing gets repeated', False, 'Finished work needs no handoff.'),
 ('Nothing; the next pharmacist will find it in the queue', False, 'Callbacks are not in the queue.'),
 ('Everything you did on the shift in time order', False, 'Too long; the next pharmacist needs the open items.')],
('h13', 0): [
 ('The patient or family, using open questions', True, ''),
 ('Outpatient pharmacy fill history or a call to the pharmacy', True, ''),
 ('Pill bottles brought from home', True, ''),
 ('The last discharge summary from 2 years ago, as is', False, 'Useful as a starting point, but out of date without confirmation.'),
 ('The usual dose for each drug class', False, 'Guessing creates errors.')],
('h13', 1): [
 ('Missed home drugs cause withdrawal; errors carry to discharge', True, 'For example beta blocker withdrawal.'),
 ('It only matters for billing and insurance', False, ''),
 ('It only matters for controlled substances', False, ''),
 ('It only matters after discharge, not during the stay', False, 'Inpatient omissions cause harm too.')],
('h14', 0): [
 ('ASHP shortage list plus St. Mary\'s substitution protocol', True, 'Joint Commission expects written substitution protocols.'),
 ('FDA Orange Book therapeutic equivalence ratings', False, 'The Orange Book lists generic equivalence, not shortage alternatives.'),
 ('The FDA Purple Book', False, 'Biologic and biosimilar listings.'),
 ('Each prescriber chooses their own substitute', False, 'Uncoordinated substitution causes errors.')],
}

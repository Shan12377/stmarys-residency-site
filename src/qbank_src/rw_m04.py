# Module 3 balancing fixes and Module 4 (IV to PO) rewrites.
R = {
('pk05', 1): [
 ('Near new steady state and with kidney changes', True, 'Bayesian tools allow earlier checks.'),
 ('Only at the end of the planned course', False, 'Too late to adjust.'),
 ('Every day for the whole course', False, 'More often than needed when stable.'),
 ('Never again once one AUC is on target', False, 'Kidney function changes during illness.')],
('iv01', 2): [
 ('More than 3 CFU total fails', True, 'After the media fill (both hands).'),
 ('More than 0 CFU total fails', False, 'That is the action level after garbing.'),
 ('More than 1 CFU per hand fails', False, 'Not the USP 797 level.'),
 ('More than 10 CFU total fails', False, 'Far too loose.')],
('iv03', 2): [
 ('20 to 25 °C and 30 to 35 °C, 7 days each', True, '2023 chapter.'),
 ('30 to 35 °C only, for 48 to 72 hours', False, 'Resembles fingertip plate incubation, not media fill.'),
 ('2 to 8 °C, refrigerated, for 14 days', False, 'Refrigeration stops growth.'),
 ('20 to 25 °C only, for 5 to 7 days', False, 'Both ranges are needed.')],
('iv04', 2): [
 ('HEPA filtered air before it touches anything', True, 'Never block it.'),
 ('Air in the ante room right after garbing', False, 'Not first air.'),
 ('The first full air change of the shift', False, 'Not a USP term.'),
 ('Room air drawn back into the HEPA filter', False, 'That air has already touched surfaces.')],
('iv05', 0): [
 ('Every 6 months and after major repairs', True, ''),
 ('Every 12 months and after major repairs', False, '12 months is the training cycle.'),
 ('Every month and after major repairs', False, 'Monthly is surface sampling.'),
 ('Every 3 months and after major repairs', False, '3 months is the Category 3 competency cycle.')],
('iv06', 1): [
 ('Top to bottom, back to front, away from HEPA', True, ''),
 ('Front to back, moving toward the HEPA filter', False, 'Pushes dirt into the critical area.'),
 ('Bottom to top, then back to front', False, 'Drips fall onto cleaned areas.'),
 ('Circles from the center of the work surface', False, 'Not the recommended pattern.')],
('iv06', 2): [
 ('At least monthly (and if contamination suspected)', True, ''),
 ('At least weekly, on the same day each week', False, 'More often than required.'),
 ('At least every 6 months, at certification', False, '6 months is certification and air sampling.'),
 ('Only after a positive surface sample result', False, 'It is scheduled, not only reactive.')],
('iv10', 2): [
 ('Spill kit and full PPE; contain from outside in', True, 'Dispose of waste as hazardous.'),
 ('Paper towels, then the regular trash bin', False, 'Exposure and improper disposal.'),
 ('Pour bleach directly on it, then mop it up', False, 'Contain first with the spill kit.'),
 ('Leave it for environmental services staff', False, 'Trained staff with PPE contain it.')],
('iv13', 0): [
 ('Calcium phosphate crystals in lung vessels', True, 'Deaths have occurred.'),
 ('Lipid emulsion breaking (oiling out)', False, 'A 3 in 1 stability risk.'),
 ('Vitamin breakdown from light exposure', False, 'Potency, not a fatal precipitate.'),
 ('Dextrose caramelizing inside the bag', False, 'Not a PN risk.')],
('iv14', 1): [
 ('A central concentration; peripheral max about 10 mEq/h', True, '40 mEq/100 mL.'),
 ('The bag needs a 1.2 micron in line filter', False, 'Filter choice is not the problem.'),
 ('KCl must be mixed in D5W instead of NS', False, 'Diluent is not the problem.'),
 ('Nothing; label wording is only cosmetic', False, 'Route mismatch is dangerous.')],
('iv15', 1): [
 ('The first dose cefepime for sepsis', True, ''),
 ('The TPN that is due at 2100', False, 'Due tonight.'),
 ('The morning batch of 40 piggybacks', False, 'Routine.'),
 ('Restocking the hood for the day', False, 'After the first dose.')],
('po01', 0): [
 ('Working gut: eating and taking other oral meds', True, ''),
 ('Improving and hemodynamically stable', True, ''),
 ('A well absorbed oral option exists', True, 'Levofloxacin is about 99% absorbed.'),
 ('Afebrile for at least 7 days', False, 'Most criteria use 24 to 48 hours afebrile.'),
 ('WBC fully normal for 72 hours', False, 'Improving WBC is enough.')],
('po01', 1): [
 ('750 mg PO daily (1:1)', True, ''),
 ('500 mg PO daily', False, '500 mg is an older levofloxacin dose; IV and PO are equivalent at 750 mg.'),
 ('750 mg PO every 12 hours', False, 'Doubles the dose.'),
 ('1,500 mg PO daily', False, 'No adjustment for oral absorption needed.')],
('po01', 2): [
 ('Fewer line infections, earlier discharge, lower cost', True, ''),
 ('Oral antibiotics penetrate the lungs better', False, 'Not generally true.'),
 ('Oral dosing avoids kidney adjustment', False, 'Renal adjustment applies by either route.'),
 ('IV levofloxacin cannot be given beyond 3 days', False, 'No such limit.')],
('po02', 0): [
 ('Levofloxacin and moxifloxacin', True, ''),
 ('Linezolid', True, ''),
 ('Metronidazole', True, ''),
 ('Fluconazole', True, ''),
 ('Ciprofloxacin', False, 'About 70% absorbed: 400 mg IV = 500 to 750 mg PO.'),
 ('Vancomycin (for systemic infection)', False, 'Oral vancomycin is not absorbed.')],
('po02', 1): [
 ('Levetiracetam', True, ''),
 ('Acetaminophen', True, ''),
 ('Pantoprazole', True, ''),
 ('Furosemide', False, 'About 50% absorbed: roughly 1:2.'),
 ('Metoprolol', False, 'Large first pass loss: roughly 1:2.5.')],
('po03', 0): [
 ('About 80 mg PO twice daily (1:2)', True, 'Oral bioavailability about 50%, variable.'),
 ('40 mg PO twice daily (1:1)', False, 'Usually less diuresis.'),
 ('160 mg PO twice daily (1:4)', False, 'Overestimates; may cause overdiuresis.'),
 ('20 mg PO twice daily (2:1)', False, 'Reversed.')],
('po03', 1): [
 ('500 to 750 mg PO every 12 hours', True, 'About 70% absorbed.'),
 ('400 mg PO every 12 hours', False, '1:1 applies to levofloxacin, not ciprofloxacin.'),
 ('750 mg PO daily', False, 'That is the levofloxacin daily dose.'),
 ('250 mg PO every 12 hours', False, 'Too low for serious infection.')],
('po03', 2): [
 ('About 12.5 to 25 mg PO every 6 hours', True, 'Roughly 1:2.5; titrate to heart rate and BP.'),
 ('5 mg PO every 6 hours (1:1)', False, 'Far too low orally.'),
 ('50 mg PO every 6 hours (1:10)', False, 'Overestimates.'),
 ('25 mg ER once daily', False, 'Lower daily total and a different product.')],
('po03', 3): [
 ('IV is lower, about 50 to 75% of oral', True, 'Label: relative oral bioavailability about 48 to 74%.'),
 ('IV is the same as oral (1:1)', False, 'Overdoses with IV.'),
 ('IV is double the oral dose', False, 'Reversed.'),
 ('IV is about 25% of oral', False, 'Too low.')],
('po04', 0): [
 ('S. aureus bacteremia, early', True, 'Oral step down only in selected patients after clearance, with ID.'),
 ('Meningitis', True, ''),
 ('Endocarditis, at least initially', True, 'POET: partial oral therapy after at least 10 days IV in selected stable patients.'),
 ('Pyelonephritis improving on day 2', False, 'A classic case for switching.'),
 ('Community acquired pneumonia improving on day 3', False, 'Also a classic case for switching.')],
('po04', 1): [
 ('Vomiting, ileus, severe diarrhea or malabsorption', True, ''),
 ('NPO with no feeding tube', True, ''),
 ('Unstable vitals or worsening infection', True, ''),
 ('Age over 80 years', False, 'Age alone does not block a switch.'),
 ('CrCl below 30 mL/min', False, 'Adjust the dose; route can still be oral.')],
('po05', 0): [
 ('Ca, Mg, Al, Fe and Zn bind ciprofloxacin', True, 'Absorption can drop dramatically.'),
 ('Calcium speeds ciprofloxacin clearance', False, 'The problem is binding in the gut, not clearance.'),
 ('Ciprofloxacin depletes magnesium', False, 'Not the interaction.'),
 ('Iron raises ciprofloxacin levels', False, 'It lowers absorption.')],
('po05', 1): [
 ('Cipro 2 h before or 6 h after the minerals', True, 'Per label; or hold supplements during the course.'),
 ('Cipro 6 h before or 2 h after the minerals', False, 'Reversed.'),
 ('Take them together with food', False, 'Food with calcium (dairy) still binds.'),
 ('Double the ciprofloxacin dose', False, 'Raises toxicity without fixing binding.')],
('po05', 2): [
 ('Tetracyclines (doxycycline, minocycline)', True, ''),
 ('Beta lactams (amoxicillin, cephalexin)', False, 'Not meaningfully affected.'),
 ('Macrolides (azithromycin)', False, 'Not the chelation problem.'),
 ('Linezolid', False, 'Not affected.')],
('po06', 0): [
 ('Feeds bind phenytoin; hold feeds 1 to 2 h around doses', True, 'Monitor levels closely.'),
 ('Feeds speed phenytoin metabolism', False, 'Binding, not metabolism.'),
 ('Feeds have no effect on phenytoin', False, 'Well known interaction.'),
 ('Feeds raise phenytoin levels', False, 'They lower absorption.')],
('po06', 1): [
 ('Capsules are 92% phenytoin (sodium); suspension is 100% (acid)', True, ''),
 ('Capsules are 100%; suspension is 92%', False, 'Reversed.'),
 ('Both are phenytoin acid at 100%', False, 'Capsules are the sodium salt.'),
 ('Only the IV form contains phenytoin sodium', False, 'Extended capsules are the sodium salt too.')],
('po06', 2): [
 ('Extended release and enteric coated tablets', True, 'Check the ISMP Do Not Crush list.'),
 ('Plain immediate release levothyroxine tablets', False, 'Can be crushed.'),
 ('Plain immediate release metoprolol tartrate tablets', False, 'Can be crushed; the succinate ER cannot.'),
 ('Acetaminophen regular tablets', False, 'Can be crushed (liquid preferred).')],
('po07', 0): [
 ('600 mg PO every 12 hours (1:1)', True, ''),
 ('600 mg PO daily', False, 'Halves exposure.'),
 ('1,200 mg PO every 12 hours', False, 'Doubles.'),
 ('400 mg PO every 12 hours', False, 'Not a standard dose.')],
('po07', 1): [
 ('Serotonin syndrome: linezolid is a weak MAO inhibitor', True, ''),
 ('QT prolongation with sertraline', False, 'Sertraline has low QT risk; the key issue is serotonin.'),
 ('Linezolid lowers sertraline levels', False, 'Not the interaction.'),
 ('Bleeding from combined platelet effects', False, 'SSRIs affect platelets, but serotonin syndrome is the classic warning.')],
('po07', 2): [
 ('Platelets and blood counts after about 2 weeks', True, ''),
 ('INR weekly', False, 'Warfarin monitoring.'),
 ('Serum potassium daily', False, 'Not a linezolid issue.'),
 ('TSH monthly', False, 'Not a linezolid issue.')],
('po08', 0): [
 ('Use the automatic conversion protocol when eligible', True, 'Document the change.'),
 ('Recommend to the prescriber with criteria and dose', True, 'Make yes easy.'),
 ('Switch everything on day 3 without checking', False, 'Each patient must meet criteria.'),
 ('Wait for the prescriber to ask', False, 'Proactive switching is the pharmacist\'s value.')],
}

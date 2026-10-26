# Module 2 balancing fixes and Module 3 (USP 797) rewrites built on real USP trap pairs.
R = {
('pk05', 1): [
 ('Near the new steady state, and whenever kidneys change', True, 'Bayesian tools allow earlier checks.'),
 ('Only at the end of the planned course', False, 'Too late to adjust.'),
 ('Every day for the whole course', False, 'More often than needed when stable.'),
 ('Never again once one AUC is on target', False, 'Kidney function changes during illness.')],
('pk07', 0): [
 ('Vancomycin infusion reaction (rate related)', True, 'Histamine release.'),
 ('IgE mediated anaphylaxis needing epinephrine', False, 'No hypotension, wheeze or airway swelling.'),
 ('DRESS syndrome from a new drug exposure', False, 'Appears days to weeks into therapy.'),
 ('Linear IgA bullous dermatosis', False, 'A rare blistering reaction days into therapy.')],
('pk10', 2): [
 ('Y site compatibility with drugs in the line', True, 'It runs all day.'),
 ('Light protection for the bag and tubing', False, 'Not required.'),
 ('PVC free tubing to prevent adsorption', False, 'Matters for nitroglycerin and insulin.'),
 ('A 0.22 micron in line filter', False, 'Needed for phenytoin, not routine here.')],
('pk12', 1): [
 ('Fidaxomicin 200 mg BID x 10 days preferred', True, 'IDSA/SHEA 2021; oral vancomycin 125 mg QID x 10 days is the alternative.'),
 ('Oral vancomycin 500 mg QID x 10 days', False, '500 mg QID is for fulminant disease.'),
 ('Metronidazole 500 mg TID x 10 days', False, 'Only for nonsevere disease when the others are unavailable.'),
 ('Pulsed fidaxomicin after 5 days of BID', False, 'Extended pulsed dosing is a recurrence option.')],
('pk15', 2): [
 ('Hold doses; redose when the level is below 1', True, 'Clearance too slow for the method.'),
 ('Give the next dose in 48 hours anyway', False, 'Too much drug still on board.'),
 ('Give 3.5 mg/kg every 48 hours instead', False, 'Not a Hartford step.'),
 ('Switch to 1 mg/kg every 8 hours now', False, 'That is synergy dosing.')],
('pk17', 0): [
 ('1 mg/kg every 8 hours; peak 3 to 4, trough below 1', True, 'AHA 2015 synergy dosing.'),
 ('7 mg/kg once daily by the Hartford nomogram', False, 'Endocarditis is a Hartford exclusion.'),
 ('5 mg/kg once daily, adjusted by levels', False, 'Gram negative extended interval dosing.'),
 ('2 mg/kg load, then 1.5 mg/kg every 8 hours', False, 'The intraamniotic infection regimen.')],
('iv01', 0): [
 ('Training plus a knowledge test', True, 'Initially, then at least every 12 months.'),
 ('Garbing and hand hygiene with gloved fingertip sampling', True, ''),
 ('Media fill, fingertip sampling and a surface sample', True, 'The aseptic manipulation competency.'),
 ('Viable air sampling of the room by the compounder', False, 'Air sampling is facility monitoring (every 6 months), not a personnel competency.'),
 ('Hood certification performed by the compounder', False, 'Certification is done by a qualified certifier every 6 months.')],
('iv01', 1): [
 ('Three times, each with zero CFU', True, 'Initial garbing qualification: action level above 0 CFU.'),
 ('Three times, each with 3 CFU or fewer', False, 'Above 3 CFU is the action level after a media fill, not after garbing.'),
 ('Once, with zero CFU', False, 'Initial qualification needs three consecutive passes.'),
 ('Once, with 3 CFU or fewer', False, 'Mixes the media fill action level with a single test.')],
('iv01', 2): [
 ('More than 3 CFU total (both hands) fails', True, 'After the media fill.'),
 ('More than 0 CFU fails', False, 'That is the action level after garbing.'),
 ('More than 1 CFU per hand fails', False, 'Not the USP 797 level.'),
 ('More than 10 CFU total fails', False, 'Far too loose.')],
('iv01', 3): [
 ('At least every 6 months', True, 'Category 1 and 2 compounders.'),
 ('At least every 3 months', False, 'Every 3 months applies to Category 3 compounders.'),
 ('At least every 12 months', False, '12 months is the training and knowledge test cycle (and supervisors who do not compound).'),
 ('At least every 24 months', False, 'No USP 797 competency runs every 2 years.')],
('iv02', 0): [
 ('Dirtiest to cleanest', True, 'Shoe and hair covers before washing.'),
 ('Cleanest to dirtiest', False, 'Reversed.'),
 ('Top of the body to the bottom', False, 'Shoe covers go on first.'),
 ('Any order, as long as gloves go on last', False, 'Order matters to avoid touching dirty items with clean hands.')],
('iv02', 1): [
 ('Shoe covers, hair cover, mask, wash, gown, sterile gloves', True, ''),
 ('Wash, shoe covers, hair cover, mask, gown, sterile gloves', False, 'Touching shoe covers after washing recontaminates hands.'),
 ('Shoe covers, hair cover, mask, gown, wash, sterile gloves', False, 'The gown goes on after washing.'),
 ('Hair cover, mask, wash, gown, shoe covers, sterile gloves', False, 'Shoe covers after the gown recontaminate hands and gown.')],
('iv02', 2): [
 ('At least 30 seconds, nails cleaned, to the elbows', True, ''),
 ('At least 15 seconds, hands and wrists only', False, 'Too short and too limited.'),
 ('At least 20 seconds, as in routine patient care', False, '20 seconds is general hand hygiene; compounding needs at least 30.'),
 ('At least 2 minutes with a scrub brush', False, 'Brushes are not required and can damage skin.')],
('iv02', 3): [
 ('Sterile 70% IPA, reapplied often, allowed to dry', True, ''),
 ('Nonsterile 70% IPA, since gloves are already sterile', False, 'Sterile IPA is required inside ISO 5.'),
 ('Alcohol based hand rub applied over the gloves', False, 'Hand rub is for bare hands before gloving.'),
 ('Nothing once sterile gloves are on', False, 'Gloves pick up contamination.')],
('iv03', 0): [
 ('Prove aseptic technique with growth medium', True, 'Copies your most complex manipulations.'),
 ('Test the hood\'s HEPA filter integrity', False, 'That is certification.'),
 ('Measure particle counts in the buffer room', False, 'That is certification.'),
 ('Check that the BUD on labels is correct', False, 'Unrelated.')],
('iv03', 1): [
 ('Failure: retrain and repeat the whole competency', True, 'If any part fails, the whole aseptic assessment is repeated.'),
 ('Normal: growth medium always turns cloudy', False, 'Clear means pass.'),
 ('Failure: repeat only the fingertip sample', False, 'The whole aseptic manipulation assessment is repeated.'),
 ('Pass, if fewer than 3 units are cloudy', False, 'Any turbid unit is a failure.')],
('iv03', 2): [
 ('20 to 25 °C and 30 to 35 °C, at least 7 days each', True, '2023 chapter.'),
 ('30 to 35 °C only, for 48 to 72 hours', False, 'That resembles gloved fingertip plate incubation, not media fill.'),
 ('2 to 8 °C for 14 days', False, 'Refrigeration stops growth.'),
 ('20 to 25 °C only, for 5 to 7 days', False, 'Both temperature ranges are needed.')],
('iv04', 0): [
 ('Hood ISO 5; buffer ISO 7; ante ISO 8', True, 'Ante ISO 7 if it opens to a negative pressure buffer room.'),
 ('Hood ISO 5; buffer ISO 8; ante ISO 7', False, 'Buffer and ante are reversed.'),
 ('Hood ISO 7; buffer ISO 7; ante ISO 8', False, 'The hood must be ISO 5.'),
 ('Hood ISO 5; buffer ISO 5; ante ISO 7', False, 'Only the hood is ISO 5.')],
('iv04', 1): [
 ('Buffer to ante (buffer positive, at least 0.02 inch)', True, 'For non hazardous compounding.'),
 ('Ante to buffer (buffer negative, 0.01 to 0.03 inch)', False, 'Negative pressure is for hazardous drug rooms (USP 800).'),
 ('No airflow between rooms (equal pressure)', False, 'Pressure difference protects the buffer room.'),
 ('Buffer to hallway, skipping the ante room', False, 'Air flows clean to less clean through the ante room.')],
('iv04', 2): [
 ('HEPA filtered air before it touches anything', True, 'Never block it with hands or items.'),
 ('Air in the ante room after garbing', False, 'Not first air.'),
 ('The first air change of the shift', False, 'Not a USP term.'),
 ('Air returning to the HEPA filter', False, 'That air has already touched surfaces.')],
('iv05', 0): [
 ('At least every 6 months and after major repairs', True, ''),
 ('At least every 12 months', False, '12 months is the training cycle.'),
 ('At least monthly', False, 'Monthly is surface sampling.'),
 ('At least every 3 months', False, '3 months is the Category 3 competency cycle.')],
('iv05', 1): [
 ('At least monthly', True, '2023 chapter.'),
 ('At least every 6 months', False, '6 months is viable air sampling and certification.'),
 ('At least weekly', False, 'More often than required.'),
 ('At least every 12 months', False, 'Too infrequent.')],
('iv05', 2): [
 ('Investigate, sporicidal clean, resample, document', True, 'Any mold in ISO 5 needs action.'),
 ('Ignore it if the count is under the action level', False, 'Mold in ISO 5 always needs investigation.'),
 ('Clean with sterile IPA only and continue', False, 'IPA does not kill spores.'),
 ('Wait for the next 6 month certification', False, 'Too late.')],
('iv06', 0): [
 ('Clean, disinfect, then apply sterile 70% IPA', True, 'Respect each product\'s contact time.'),
 ('Spray sterile IPA and wipe immediately', False, 'IPA alone does not clean residue; wiping too soon defeats contact time.'),
 ('Disinfect first, then clean, then IPA', False, 'Cleaning removes residue first.'),
 ('Sporicidal agent daily instead of cleaning', False, 'Sporicidal is at least monthly, on top of routine cleaning.')],
('iv06', 1): [
 ('Top to bottom, back to front, away from the HEPA', True, ''),
 ('Front to back, toward the HEPA filter', False, 'Pushes dirt into the critical area.'),
 ('Bottom to top, back to front', False, 'Drips fall onto cleaned areas.'),
 ('Circular motions from the center out', False, 'Not the USP recommended pattern.')],
('iv06', 2): [
 ('At least monthly, and when contamination is suspected', True, ''),
 ('At least weekly', False, 'More often than required (allowed, not required).'),
 ('At least every 6 months', False, '6 months is certification and air sampling.'),
 ('Only after a positive surface sample', False, 'It is scheduled, not only reactive.')],
('iv07', 0): [
 ('3 sterile products max; start within 4 hours', True, 'Immediate use.'),
 ('3 sterile products max; start within 12 hours', False, '12 hours is the Category 1 room temperature BUD.'),
 ('5 sterile products max; start within 4 hours', False, 'The limit is 3.'),
 ('3 sterile products max; start within 1 hour', False, '1 hour applies to a single dose vial punctured outside ISO 5.')],
('iv07', 1): [
 ('Made outside clean air: little time for growth', True, ''),
 ('Amiodarone degrades within 4 hours', False, 'The limit is about sterility, not stability.'),
 ('Code drugs are always given within 1 hour', False, 'Not the reason.'),
 ('Only pharmacists may compound beyond 4 hours', False, 'Not the reason.')],
('iv08', 0): [
 ('Category 1: 12 h room temp or 24 h refrigerated', True, 'A hood in a segregated area makes Category 1 only.'),
 ('Category 2: 4 days room temp or 10 days refrigerated', False, 'Category 2 needs a cleanroom suite.'),
 ('Immediate use: 4 hours', False, 'It was made in a hood, not under immediate use rules.'),
 ('Category 1: 24 h room temp or 48 h refrigerated', False, 'Category 1 limits are 12 and 24 hours.')],
('iv08', 1): [
 ('4 days room temp, 10 days fridge, 45 days frozen', True, 'Sterile starting ingredients, no sterility test.'),
 ('1 day room temp, 4 days fridge, 45 days frozen', False, 'That is Category 2 with a nonsterile ingredient.'),
 ('30 days room temp, 45 days fridge, 60 days frozen', False, 'That requires a passed sterility test.'),
 ('12 hours room temp, 24 hours fridge', False, 'That is Category 1.')],
('iv08', 2): [
 ('1 day room temp, 4 days fridge, 45 days frozen', True, ''),
 ('4 days room temp, 10 days fridge, 45 days frozen', False, 'That is all sterile ingredients.'),
 ('12 hours room temp, 24 hours fridge', False, 'Category 1 limits.'),
 ('No change; sterility of ingredients does not matter', False, 'It shortens the BUD.')],
('iv08', 3): [
 ('Chemical and physical stability of the drug', True, 'The BUD is the shorter of sterility and stability.'),
 ('The manufacturer\'s expiration date on the vial', False, 'Vial expiration limits the vial, but the CSP BUD comes from USP limits and stability.'),
 ('The patient\'s expected length of stay', False, 'Irrelevant.'),
 ('The pump\'s programmed infusion time', False, 'Irrelevant.')],
('iv09', 0): [
 ('Yes: up to 12 hours if punctured and kept in ISO 5', True, ''),
 ('Yes: up to 28 days, like a multiple dose vial', False, '28 days is the multiple dose vial rule.'),
 ('Yes: up to 1 hour only', False, '1 hour applies when punctured outside ISO 5.'),
 ('No: single dose vials are always one entry only', False, 'USP allows 12 hours inside ISO 5.')],
('iv09', 1): [
 ('Yes: 28 days after opening unless labeled otherwise', True, ''),
 ('No: 14 days after opening is the limit', False, 'Not the USP default.'),
 ('No: 12 hours after first puncture', False, 'That is the single dose vial rule.'),
 ('Yes: until the manufacturer expiration date', False, 'Opening starts the 28 day clock.')],
('iv10', 0): [
 ('Containment hood in a negative pressure room', True, 'USP 800.'),
 ('Laminar airflow hood in a positive pressure room', False, 'Pushes hazardous drug toward people.'),
 ('Containment hood in a positive pressure room', False, 'The room must be negative.'),
 ('Any hood if the compounder wears double gloves', False, 'Engineering controls come first.')],
('iv10', 1): [
 ('Two pairs of ASTM D6978 chemotherapy gloves', True, ''),
 ('A permeation resistant gown that closes in the back', True, ''),
 ('A closed system transfer device when possible', True, 'Required for administration, recommended for compounding.'),
 ('One pair of sterile nitrile exam gloves', False, 'Not protective enough.'),
 ('A cloth lab coat over scrubs', False, 'Absorbs hazardous drug.')],
('iv10', 2): [
 ('Spill kit, full PPE, contain outside in, hazardous waste', True, ''),
 ('Paper towels, then regular trash', False, 'Exposure and improper disposal.'),
 ('Bleach directly on the spill, then mop', False, 'Contain first with the spill kit; deactivation follows the kit steps.'),
 ('Leave it for environmental services', False, 'Trained staff with PPE contain it.')],
('iv11', 0): [
 ('In a minibag, never a syringe', True, 'Intrathecal vincristine is almost always fatal; a minibag cannot connect to a spinal needle.'),
 ('In a syringe labeled "For IV use only"', False, 'Labels alone have failed.'),
 ('In a syringe with a non luer connector', False, 'ISMP still recommends the minibag.'),
 ('In a syringe, kept in a separate bin from intrathecal drugs', False, 'Separation helps, but the minibag is the safeguard.')],
('iv12', 0): [
 ('Phenytoin in D5W', True, 'Precipitates; NS only, 0.22 micron filter, max 50 mg/min.'),
 ('Liposomal amphotericin B in normal saline', True, 'Saline breaks the liposomes; D5W only.'),
 ('Ampicillin in D5W for a long infusion', True, 'Much less stable in dextrose.'),
 ('Vancomycin in normal saline', False, 'Fine in NS or D5W.'),
 ('Cefazolin in D5W', False, 'Compatible.')],
('iv12', 1): [
 ('Glass or polyolefin bag with non PVC tubing', True, 'Nitroglycerin is absorbed into PVC.'),
 ('Standard PVC bag with a 0.22 micron filter', False, 'Filters do not stop PVC absorption.'),
 ('Amber PVC bag to protect from light', False, 'Light is not the main issue; PVC is.'),
 ('Any bag, with a higher starting rate to compensate', False, 'Unpredictable dosing.')],
('iv13', 0): [
 ('Calcium phosphate crystals blocking lung vessels', True, 'Deaths have occurred.'),
 ('Lipid emulsion breaking (oiling out)', False, 'A 3 in 1 stability risk, not the calcium phosphate risk.'),
 ('Vitamin degradation from light', False, 'A potency issue, not a fatal precipitate.'),
 ('Dextrose caramelization in the bag', False, 'Not a PN compounding risk.')],
('iv13', 1): [
 ('1.2 micron filter', True, 'Lipid droplets clog 0.22 micron filters.'),
 ('0.22 micron filter', False, 'For 2 in 1 PN without lipid.'),
 ('5 micron filter', False, 'Used for some drugs drawn from ampules (filter needles), not PN.'),
 ('No filter needed with lipids', False, 'A 1.2 micron filter is used.')],
('iv13', 2): [
 ('About 900 mOsm/L or less', True, ''),
 ('About 1,500 mOsm/L or less', False, 'Requires a central line.'),
 ('About 600 mOsm/L or less', False, 'Lower than the usual limit.'),
 ('No limit if the IV is in a large vein', False, 'The limit still applies.')],
('iv14', 0): [
 ('What went in: vials, pull back, images or weight', True, ''),
 ('Full label: patient, drug, concentration, volume, BUD', True, ''),
 ('Visual check for particles, cloudiness, leaks', True, ''),
 ('The technician\'s confirmation that it is right', False, 'Your check is independent.'),
 ('The patient\'s insurance coverage', False, 'Not a CSP check.')],
('iv14', 1): [
 ('40 mEq/100 mL is a central concentration; peripheral max about 10 mEq/h', True, ''),
 ('The bag needs a 1.2 micron filter', False, 'Filter choice is not the problem.'),
 ('KCl must be in D5W, not NS', False, 'Diluent is not the problem.'),
 ('Nothing; label wording is cosmetic', False, 'Route mismatch is dangerous.')],
('iv15', 0): [
 ('Certification lapsed: tell the supervisor, follow the SOP', True, 'Compounding in an uncertified hood violates USP 797.'),
 ('Nothing: certification is paperwork only', False, 'It proves the air is clean.'),
 ('Run a surface sample, then compound if clean', False, 'A surface sample does not replace certification.'),
 ('Compound only Category 2 products until recertified', False, 'Category 2 needs certified controls too.')],
('iv15', 1): [
 ('The first dose cefepime for the septic patient', True, ''),
 ('The TPN due at 2100', False, 'Due tonight.'),
 ('The morning batch of 40 piggybacks', False, 'Routine.'),
 ('Restocking the hood for the day', False, 'After the first dose.')],
}

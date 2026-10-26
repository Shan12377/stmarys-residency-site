# Rewritten options for L&D cases ld21 to ld40.
R = {
('ld21', 0): [
 ('A: positive GBS culture at 36 weeks', True, 'Culture at 36 0/7 to 37 6/7 weeks is the screening window (CO 797).'),
 ('B: unknown status, membranes ruptured 20 hours', True, 'Unknown status plus rupture 18 hours or longer means treat.'),
 ('C: negative culture at 36 weeks, no fever', False, 'A negative culture within 5 weeks means no prophylaxis unless a new risk factor appears.'),
 ('C, but only if membranes rupture for 12 hours', False, '12 hours is not the threshold; the unknown status trigger is 18 hours, and C is culture negative anyway.')],
('ld21', 1): [
 ('GBS bacteriuria at any time this pregnancy', True, 'Treat in labor regardless of culture (CO 797).'),
 ('A previous infant with invasive GBS disease', True, 'Treat regardless of culture.'),
 ('A positive GBS culture in a previous pregnancy only', False, 'Prior pregnancy colonization alone is not an indication; rescreen this pregnancy (some may offer based on shared decision) ⚠️.'),
 ('A prior cesarean delivery', False, 'Matters for misoprostol and TOLAC, not GBS prophylaxis.')],
('ld22', 0): [
 ('Penicillin G 5 million units IV, then 2.5 to 3 million units every 4 hours', True, 'First choice (CO 797).'),
 ('Ampicillin 2 g IV, then 1 g every 4 hours', True, 'Acceptable alternative.'),
 ('Ampicillin 2 g IV every 6 hours', False, '2 g every 6 hours is the intraamniotic infection dose (with gentamicin), not GBS prophylaxis.'),
 ('Cefazolin 2 g IV, then 1 g every 8 hours', False, 'Cefazolin is for low risk penicillin allergy; with no allergy, penicillin or ampicillin is preferred.')],
('ld22', 1): [
 ('Penicillin, ampicillin or cefazolin started at least 4 hours before delivery', True, 'CO 797.'),
 ('Any beta lactam started at least 2 hours before delivery', False, 'Two hours is not adequate; the threshold is 4 hours.'),
 ('Penicillin, ampicillin, cefazolin, clindamycin or vancomycin started 4 hours before', False, 'Clindamycin and vancomycin do not count as adequate for the newborn algorithm.'),
 ('Penicillin started at least 8 hours before delivery', False, 'Eight hours is longer than required.')],
('ld23', 0): [
 ('Low risk: a childhood rash without hives or a severe reaction', True, 'CO 797 low risk: no anaphylaxis, angioedema, respiratory distress, hives or severe skin reaction.'),
 ('High risk: any rash counts as high risk', False, 'Only hives or severe skin reactions (SJS, TEN, DRESS) are high risk.'),
 ('High risk because the reaction was never tested', False, 'Lack of testing does not make a benign rash high risk.'),
 ('Not an allergy at all; give penicillin', False, 'Possible after evaluation or testing, but on L&D the CO 797 pathway is cefazolin.')],
('ld23', 1): [
 ('Cefazolin 2 g IV, then 1 g every 8 hours', True, 'Low risk allergy; also counts as adequate.'),
 ('Clindamycin 900 mg IV every 8 hours', False, 'Clindamycin is for high risk allergy and only if susceptible.'),
 ('Vancomycin 20 mg/kg IV every 8 hours', False, 'Vancomycin is reserved for high risk allergy without clindamycin susceptibility, and is not adequate for the newborn algorithm.'),
 ('Cefazolin 2 g IV, then 1 g every 4 hours', False, 'Every 4 hours is the ampicillin and penicillin interval; cefazolin is every 8 hours.')],
('ld24', 0): [
 ('Susceptibility to clindamycin, including inducible resistance testing', True, 'CO 797: clindamycin only if susceptible.'),
 ('A penicillin skin test', False, 'Useful later, but with anaphylaxis history the question is clindamycin susceptibility now.'),
 ('A vancomycin trough', False, 'Levels are not needed to choose the drug.'),
 ('Her creatinine clearance', False, 'Matters for vancomycin dosing, not the clindamycin decision.')],
('ld24', 1): [
 ('20 mg/kg every 8 hours, max 2 g per dose (about 1,440 mg)', True, 'CO 797; round per protocol (for example 1,500 mg).'),
 ('1 g every 12 hours', False, 'That is the intraamniotic infection alternative dose in CO 712, not GBS prophylaxis.'),
 ('15 mg/kg every 12 hours', False, 'A general adult maintenance dose; CO 797 uses 20 mg/kg every 8 hours for GBS.'),
 ('20 to 35 mg/kg once, max 3 g', False, 'That is the critical illness loading dose range (Rybak 2020).')],
('ld25', 0): [
 ('Ampicillin 2 g IV every 6 hours plus gentamicin', True, 'ACOG CO 712.'),
 ('Penicillin G 5 million units, then 2.5 to 3 million every 4 hours', False, 'That is GBS prophylaxis; no gram negative coverage.'),
 ('Ceftriaxone 2 g IV daily', False, 'A pyelonephritis option; misses enterococcus and Listeria.'),
 ('Cefazolin 2 g IV every 8 hours alone', False, 'Cefazolin plus gentamicin is for mild penicillin allergy; alone it is not enough.')],
('ld25', 1): [
 ('2 mg/kg load, then 1.5 mg/kg every 8 hours', True, 'CO 712.'),
 ('5 mg/kg every 24 hours', True, 'CO 712.'),
 ('7 mg/kg every 24 hours (Hartford)', False, 'Hartford excludes pregnancy.'),
 ('1 mg/kg every 8 hours', False, 'That is endocarditis synergy dosing.')],
('ld25', 2): [
 ('One more dose plus clindamycin 900 mg or metronidazole 500 mg', True, 'Anaerobic coverage after cesarean (CO 712).'),
 ('Stop all antibiotics at delivery', False, 'That is the vaginal delivery pathway.'),
 ('Continue for 7 days after delivery', False, 'Long courses are not routine.'),
 ('Add vancomycin for MRSA coverage', False, 'Not part of the regimen.')],
('ld25', 3): [
 ('No further doses are required', True, 'CO 712.'),
 ('One more dose plus anaerobic coverage', False, 'That is the cesarean pathway.'),
 ('24 more hours of ampicillin and gentamicin', False, 'Not required after vaginal delivery.'),
 ('Switch to oral amoxicillin clavulanate for 7 days', False, 'No.')],
('ld26', 0): [
 ('Clindamycin 900 mg every 8 hours (or vancomycin 1 g every 12 hours) plus gentamicin', True, 'CO 712 severe allergy.'),
 ('Cefazolin 2 g every 8 hours plus gentamicin', False, 'That is the mild allergy regimen.'),
 ('Gentamicin alone', False, 'Misses gram positives.'),
 ('Aztreonam alone', False, 'No gram positive coverage.')],
('ld26', 1): [
 ('Cefazolin 2 g every 8 hours plus gentamicin', True, 'CO 712.'),
 ('Clindamycin 900 mg every 8 hours plus gentamicin', False, 'Reserved for severe allergy.'),
 ('Ceftriaxone 1 g daily plus gentamicin', False, 'Not the CO 712 regimen.'),
 ('Cefazolin 2 g once, then 1 g every 8 hours, no gentamicin', False, 'That is GBS prophylaxis; infection needs gentamicin too.')],
('ld27', 0): [
 ('Betamethasone 12 mg IM every 24 hours for 2 doses', True, 'CO 713.'),
 ('Dexamethasone 6 mg IM every 12 hours for 4 doses', True, 'CO 713.'),
 ('Dexamethasone 6 mg IV daily for 10 days', False, 'That is the COVID-19 regimen.'),
 ('Betamethasone 12 mg IM every 12 hours for 4 doses', False, 'Mixes the two regimens; betamethasone is every 24 hours for 2.')],
('ld27', 1): [
 ('Mature fetal lungs and lower RDS, brain bleeds and death', True, 'CO 713.'),
 ('Lower cerebral palsy risk', False, 'That is magnesium neuroprotection before 32 weeks.'),
 ('Stop contractions', False, 'Tocolysis.'),
 ('Prevent GBS infection', False, 'Antibiotics.')],
('ld28', 0): [
 ('Pregestational diabetes', True, 'Excluded from ALPS.'),
 ('Multiple gestation', True, 'Excluded.'),
 ('Chorioamnionitis', True, 'Excluded.'),
 ('A prior course of steroids', True, 'Excluded.'),
 ('Gestational age 34 to 36 weeks', False, 'That is the population ALPS did study.')],
('ld28', 1): [
 ('Neonatal hypoglycemia', True, 'ALPS.'),
 ('Neonatal hypermagnesemia', False, 'A magnesium effect.'),
 ('Neonatal bradycardia', False, 'A labetalol effect.'),
 ('Neonatal withdrawal', False, 'Opioid exposure.')],
('ld29', 0): [
 ('Indomethacin is for use only before 32 weeks', True, 'Ductal constriction risk rises after 32 weeks.'),
 ('It should not run longer than 48 hours', True, 'Low amniotic fluid and ductal effects.'),
 ('It should not run longer than 5 to 7 days', False, '5 to 7 days is the magnesium label limit.'),
 ('It is used only before 34 weeks', False, '34 weeks is the antenatal steroid cutoff.')],
('ld29', 1): [
 ('Prostaglandins keep the ductus open; NSAIDs block them', True, ''),
 ('NSAIDs raise fetal blood pressure', False, 'No.'),
 ('NSAIDs cause fetal low calcium', False, 'That is long magnesium courses.'),
 ('NSAIDs lower fetal glucose', False, 'That is steroid or beta blocker related.')],
('ld30', 0): [
 ('Rh(D) immune globulin 300 mcg IM within 72 hours of delivery', True, 'PB 181.'),
 ('Nothing; the 28 week dose covers delivery', False, 'The 28 week dose does not cover the delivery bleed.'),
 ('300 mcg IM within 28 days of delivery', False, '28 days is the outer limit sometimes quoted when 72 hours is missed, not the goal ⚠️.'),
 ('50 mcg IM within 72 hours', False, '50 mcg products are for early first trimester events.')],
('ld30', 1): [
 ('Large fetal to maternal bleed: a screen decides the number of vials', True, 'One vial covers about 30 mL fetal whole blood.'),
 ('Mother weighs over 100 kg', False, 'Dosing depends on bleed size, not weight.'),
 ('Baby is a girl', False, 'No.'),
 ('Cesarean delivery', False, 'Delivery route alone does not decide the dose.')],
('ld31', 0): [
 ('Aspirin 81 mg daily after 12 weeks for high risk patients', True, 'USPSTF 2021 (Grade B).'),
 ('Aspirin 81 mg daily starting after 28 weeks', False, '28 weeks is when antenatal RhIG is given; aspirin should start before 16 weeks for best effect.'),
 ('Aspirin 325 mg daily after 12 weeks', False, 'Too high; the studied dose is low dose.'),
 ('Aspirin 81 mg only if she develops severe range BP', False, 'Aspirin is prevention, started before preeclampsia appears.')],
('ld31', 1): [
 ('Prior preeclampsia', True, ''),
 ('Multifetal pregnancy', True, ''),
 ('Chronic hypertension, pregestational diabetes, kidney or autoimmune disease', True, ''),
 ('First pregnancy (nulliparity) alone', False, 'A moderate risk factor; needs more than one moderate factor to qualify.')],
('ld32', 0): [
 ('Misoprostol is avoided after a prior cesarean (uterine rupture risk)', True, 'PB 107.'),
 ('The dose should be 50 mcg every 4 hours', False, '50 mcg is an oral dose used in some protocols, not a fix for a uterine scar.'),
 ('The interval should be every 6 hours instead', False, 'The interval is not the issue.'),
 ('Fine if she had a low transverse incision', False, 'Still avoided for ripening after cesarean.')],
('ld32', 1): [
 ('25 mcg vaginally every 3 to 6 hours', True, 'PB 107.'),
 ('600 to 1,000 mcg once', False, 'That is the postpartum hemorrhage dose.'),
 ('100 mcg vaginally every 4 hours', False, 'Higher doses raise tachysystole.'),
 ('25 mcg vaginally every 12 hours', False, 'Interval too long.')],
('ld33', 0): [
 ('No: at least 12 hours after a prophylactic dose, so not before 1800', True, 'ASRA (4th ed); check 5th edition and St. Mary\'s policy.'),
 ('Yes: 8 hours is enough for prophylactic enoxaparin', False, 'Eight hours is not enough.'),
 ('No: at least 24 hours, so not before 0600 tomorrow', False, '24 hours is for treatment doses.'),
 ('Yes: 4 hours is enough', False, '4 hours is the wait AFTER catheter removal.')],
('ld33', 1): [
 ('At least 24 hours', True, ''),
 ('At least 12 hours', False, 'Prophylactic dose rule.'),
 ('At least 72 hours', False, 'Apixaban or rivaroxaban rule (ASRA 4th).'),
 ('At least 4 hours', False, 'After removal rule.')],
('ld33', 2): [
 ('At least 4 hours after removal', True, 'Lovenox label.'),
 ('At least 6 hours after removal', False, '6 hours is the DOAC restart time after catheter removal.'),
 ('At least 12 hours after removal', False, '12 hours is the hold before placement.'),
 ('Immediately after removal', False, 'Too soon.')],
('ld34', 0): [
 ('Insulin is preferred; metformin and glyburide cross the placenta', True, 'ADA 2025.'),
 ('Metformin first line, insulin if metformin fails', False, 'Older practice; ADA 2025 says not first line.'),
 ('Glyburide first line because it is oral', False, 'Glyburide crosses the placenta and causes neonatal hypoglycemia.'),
 ('A GLP-1 receptor agonist first line', False, 'GLP-1 RAs are not used in pregnancy.')],
('ld34', 1): [
 ('Recommend insulin and support dosing, teaching and monitoring', True, ''),
 ('Verify metformin because it was ordered', False, 'Recommend the guideline option.'),
 ('Hold all therapy until delivery', False, 'Uncontrolled glucose harms the baby.'),
 ('Start an SGLT2 inhibitor', False, 'Not used in pregnancy.')],
('ld35', 0): [
 ('Avoid NSAIDs from 20 weeks: fetal kidney problems and low fluid', True, 'FDA 2020.'),
 ('Avoid NSAIDs only after 30 weeks', False, '30 weeks was the older ductus warning; FDA moved it to 20 weeks.'),
 ('Avoid NSAIDs only after 32 weeks', False, '32 weeks is the indomethacin tocolysis cutoff.'),
 ('NSAIDs are fine at any age if under 48 hours', False, '48 hours is the indomethacin tocolysis limit, not a general rule.')],
('ld35', 1): [
 ('Low dose aspirin 81 mg for preeclampsia prevention', True, 'FDA exception.'),
 ('Indomethacin for any indication', False, 'Specific tocolysis rules apply.'),
 ('Ibuprofen under 400 mg', False, 'No dose exception.'),
 ('Topical diclofenac', False, 'Not the stated exception.')],
('ld35', 2): [
 ('Acetaminophen', True, ''),
 ('Naproxen', False, 'Another NSAID.'),
 ('Codeine', False, 'Opioids carry their own risks and codeine is avoided while breastfeeding later.'),
 ('Celecoxib', False, 'Still an NSAID.')],
('ld36', 0): [
 ('Avoid codeine (and tramadol) while breastfeeding', True, 'FDA 2017: ultrarapid metabolizers.'),
 ('Fine because codeine is a weak opioid', False, 'The risk is metabolism to morphine in mother and milk.'),
 ('Fine if limited to 3 days', False, 'No safe duration was set.'),
 ('Avoid only in mothers of preterm infants', False, 'The warning applies to all breastfeeding.')],
('ld36', 1): [
 ('Scheduled acetaminophen plus ibuprofen', True, 'NSAIDs are fine after delivery.'),
 ('Short, low dose oxycodone if needed, watching the baby', True, 'LactMed.'),
 ('Tramadol as a safer opioid', False, 'Tramadol has the same warning.'),
 ('Ibuprofen is avoided because she is still within 20 weeks', False, 'The 20 week rule applies to pregnancy, not after delivery.')],
('ld37', 0): [
 ('LactMed (NIH)', True, 'Free and primary.'),
 ('The pregnancy letter category', False, 'Letters were removed by the PLLR and never applied to lactation.'),
 ('Briggs pregnancy reference only', False, 'Briggs covers lactation too, but LactMed is the free primary source.'),
 ('NeoFax', False, 'Neonatal dosing reference.')],
('ld37', 1): [
 ('Relative infant dose (RID); under 10% generally acceptable', True, ''),
 ('Milk to plasma ratio above 1 means safe', False, 'A high ratio means more drug in milk.'),
 ('Pregnancy category B means safe', False, 'Categories are gone.'),
 ('Half life over 24 hours means safe', False, 'Long half life raises infant accumulation.')],
('ld37', 2): [
 ('Short half life', True, ''),
 ('High protein binding', True, ''),
 ('Low oral bioavailability', True, ''),
 ('High lipid solubility', False, 'Raises milk transfer.'),
 ('Low molecular weight', False, 'Raises milk transfer.')],
('ld38', 0): [
 ('Blanket contraindication removed (2021); most stop, very high risk may continue', True, 'FDA 2021.'),
 ('Absolutely contraindicated for everyone', False, 'Outdated.'),
 ('Continue for everyone; benefit outweighs risk', False, 'Most patients stop.'),
 ('Switch to ezetimibe for everyone', False, 'Not the guidance.')],
('ld38', 1): [
 ('Not recommended while breastfeeding', True, 'FDA 2021.'),
 ('Compatible at any dose', False, ''),
 ('Compatible only with pravastatin', False, 'Not stated.'),
 ('Compatible after 6 weeks postpartum', False, 'Not stated.')],
('ld39', 0): [
 ('Yes: milk levels rise only slightly and infants absorb little', True, 'LactMed.'),
 ('No: pump and discard for 24 hours after stopping', False, 'Not needed.'),
 ('No: wait 5 to 7 days', False, '5 to 7 days is the pregnancy duration warning.'),
 ('Yes, but only after the level is below 2.5 mEq/L', False, 'No level requirement.')],
('ld40', 0): [
 ('The magnesium patient: possible respiratory failure', True, 'Airway first.'),
 ('The GBS dose, because adequacy depends on timing', False, 'Second.'),
 ('The lanolin question, because it is fastest', False, 'Fast does not beat life threatening.'),
 ('All three at once by phone', False, 'Prioritize.')],
('ld40', 1): [
 ('The GBS penicillin dose', True, 'Timing affects adequacy for the newborn.'),
 ('The lanolin question', False, 'Last.'),
 ('Charting the magnesium event first', False, 'Document after the time sensitive dose.'),
 ('Calling the newborn team about GBS', False, 'Give the dose; the team uses the timing.')],
}

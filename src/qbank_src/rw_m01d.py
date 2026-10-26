# Final balancing pass for L&D (overrides earlier rw_m01 files).
R = {
('ld04', 2): [
 ('Label warns against it; ACOG still combines them with close monitoring', True, 'Label: avoid with calcium channel blockers; ACOG CO 767 uses the combination for severe BP with BP, reflex and breathing checks.'),
 ('Absolutely contraindicated; stop magnesium before giving nifedipine', False, 'Seizure prevention is not traded away for a BP drug.'),
 ('No interaction, because the two drugs act on different receptors', False, 'Both reduce calcium entry: additive hypotension and neuromuscular effects.'),
 ('Halve the magnesium dose whenever nifedipine is also given', False, 'Magnesium is reduced for kidney impairment (1 g/h), not for nifedipine.')],
('ld11', 0): [
 ('It blocks neuromuscular transmission and can trigger crisis', True, 'Myasthenia gravis is a label contraindication.'),
 ('It blocks pyridostigmine absorption from the gut', False, 'IV magnesium acts at the neuromuscular junction, not on absorption.'),
 ('It causes heart block in patients with myasthenia', False, 'Heart block is a separate label contraindication.'),
 ('It is safe in myasthenia at the renal dose of 1 g/h', False, 'A lower dose does not remove the contraindication.')],
('ld15', 1): [
 ('Contracting muscle squeezes the open placental vessels shut', True, 'The "living ligature."'),
 ('Contraction releases platelets stored in the uterine wall', False, 'No.'),
 ('Contraction blocks the breakdown of clots at the placental site', False, 'That is how TXA works.'),
 ('Contraction narrows arteries throughout the body to lower flow', False, 'That systemic effect is methylergonovine (and why it raises BP).')],
('ld16', 0): [
 ('No: contraindicated with preeclampsia and hypertension', True, 'ACOG PB 183.'),
 ('Yes, at half the usual dose (0.1 mg IM)', False, 'No dose is safe with preeclampsia.'),
 ('Yes, if it is given IM rather than IV', False, 'Both routes constrict vessels.'),
 ('Yes, once her BP is below the 160/110 threshold', False, '160/110 is the severe range treatment threshold, not a methylergonovine cutoff.')],
('ld19', 1): [
 ('The mortality benefit was seen when given within 3 hours', True, 'WOMAN trial.'),
 ('The benefit was seen only when given within 1 hour of birth', False, 'Earlier is better, but the window is 3 hours.'),
 ('It works best after 6 hours, once larger clots have formed', False, 'Benefit fades with time.'),
 ('Timing matters only in trauma bleeding (CRASH-2), not PPH', False, 'Time matters in both trials.')],
('ld20', 0): [
 ('Vial mix ups with spinal anesthetics: intrathecal TXA kills', True, 'ISMP 2024.'),
 ('Seizures occur at the standard 1 g IV PPH dose', False, 'Seizures are mostly with high doses.'),
 ('A dangerous interaction with oxytocin infusions on L&D', False, 'No such interaction.'),
 ('Frequent dosing after the 3 hour benefit window has passed', False, 'A dosing issue, not the reason for the listing.')],
('ld23', 0): [
 ('Low risk: childhood rash without hives or severe reaction', True, 'CO 797.'),
 ('High risk: any rash after penicillin counts as high risk', False, 'Only hives or severe skin reactions are high risk.'),
 ('High risk: the reaction was never confirmed by testing', False, 'Lack of testing does not make a benign rash high risk.'),
 ('Not an allergy: give penicillin G without any further thought', False, 'Possible after evaluation, but L&D follows the cefazolin pathway.')],
('ld24', 0): [
 ('Clindamycin susceptibility, including inducible resistance', True, 'CO 797.'),
 ('A penicillin skin test before choosing any antibiotic', False, 'Useful later, not the decision now.'),
 ('A vancomycin trough before the first vancomycin dose', False, 'Not needed to choose a drug.'),
 ('Her creatinine clearance before clindamycin is started', False, 'Clindamycin is not renally adjusted.')],
('ld30', 0): [
 ('Rh(D) immune globulin 300 mcg IM within 72 hours', True, 'PB 181.'),
 ('Nothing: the 28 week dose also covers the delivery bleed', False, 'It does not cover delivery.'),
 ('Rh(D) immune globulin 300 mcg IM within 28 days', False, '28 days is sometimes quoted as an outer limit when 72 hours is missed, not the goal ⚠️.'),
 ('Rh(D) immune globulin 50 mcg IM within 72 hours', False, '50 mcg is for early first trimester events.')],
('ld30', 1): [
 ('A large fetal to maternal bleed found on screening', True, 'One vial covers about 30 mL fetal whole blood.'),
 ('A mother who weighs more than 100 kg at delivery', False, 'Dose depends on bleed size, not weight.'),
 ('A baby who weighs more than 4 kg at birth', False, 'Birth weight does not decide the dose.'),
 ('Any cesarean delivery, whatever the blood loss', False, 'Route alone does not decide.')],
('ld33', 0): [
 ('No: wait 12 hours after a prophylactic dose (1800)', True, 'ASRA 4th edition; check the 5th edition and policy.'),
 ('Yes: 8 hours after a prophylactic dose is enough', False, 'Eight hours is not enough.'),
 ('No: wait 24 hours after any enoxaparin dose (0600)', False, '24 hours is for treatment doses.'),
 ('Yes: 4 hours after a prophylactic dose is enough', False, '4 hours is the wait after catheter removal.')],
('ld34', 0): [
 ('Insulin first: metformin and glyburide cross the placenta', True, 'ADA 2025.'),
 ('Metformin first line, then insulin if metformin fails', False, 'ADA 2025 says metformin is not first line.'),
 ('Glyburide first line because it is easier than insulin', False, 'Crosses the placenta; neonatal hypoglycemia.'),
 ('A GLP-1 receptor agonist first line for weight and glucose', False, 'Not used in pregnancy.')],
('ld35', 0): [
 ('Avoid NSAIDs from 20 weeks: fetal kidneys, low fluid', True, 'FDA 2020.'),
 ('Avoid NSAIDs only after 30 weeks (ductus closure)', False, '30 weeks was the older label warning; FDA moved it to 20.'),
 ('Avoid NSAIDs only after 32 weeks, as with indomethacin', False, '32 weeks is the indomethacin tocolysis cutoff.'),
 ('NSAIDs are fine at any age when used for under 48 hours', False, '48 hours is the indomethacin tocolysis limit.')],
('ld35', 2): [
 ('Acetaminophen', True, ''),
 ('Naproxen', False, 'Another NSAID.'),
 ('Celecoxib', False, 'Still an NSAID.'),
 ('Ketorolac', False, 'Still an NSAID.')],
('ld37', 1): [
 ('Relative infant dose; under 10% generally acceptable', True, ''),
 ('Milk to plasma ratio; above 1 means the drug is safe', False, 'A high ratio means more drug in milk.'),
 ('Pregnancy letter category; B or better means safe', False, 'Categories were removed and never addressed lactation.'),
 ('Half life; longer than 24 hours means safer for the baby', False, 'Long half life raises infant accumulation.')],
('ld39', 0): [
 ('Yes: milk levels rise little and infants absorb little', True, 'LactMed.'),
 ('No: pump and discard until 24 hours after the drip stops', False, 'Not needed.'),
 ('No: wait 5 to 7 days, as with the pregnancy warning', False, '5 to 7 days is the pregnancy duration warning.'),
 ('Yes, but only once her level is below 2.5 mEq/L', False, 'No level requirement.')],
}

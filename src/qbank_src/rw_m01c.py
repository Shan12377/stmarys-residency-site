# Length and plausibility balancing for L&D steps still giving the answer away (overrides rw_m01a/b).
R = {
('ld05', 2): [
 ('Tell OB about the exposure so they can check amniotic fluid', True, 'Fetal kidney injury shows up as low amniotic fluid and growth problems; ultrasound review is the follow up.'),
 ('Check maternal potassium and creatinine, then stop', False, 'Reasonable for ACE inhibitors in general, but the pregnancy issue is the fetus.'),
 ('Plan to restart lisinopril after delivery for breastfeeding', False, 'Enalapril or captopril are the studied ACE inhibitors in breastfeeding.'),
 ('File a near miss report; no clinical follow up needed', False, 'Weeks of exposure is a real exposure needing clinical follow up.')],
('ld07', 3): [
 ('For 24 hours after delivery or the last seizure', True, 'ACOG PB 222.'),
 ('For 12 hours after delivery or the last seizure', False, '12 hours is the maximum of the fetal neuroprotection protocol.'),
 ('Until delivery, then stop in the delivery room', False, 'Eclampsia risk continues postpartum.'),
 ('For 5 to 7 days, then reassess the need', False, '5 to 7 days is the label warning limit, not a target.')],
('ld10', 1): [
 ('Protect the airway, treat severe BP, check for toxicity', True, 'Treat the whole patient.'),
 ('Load phenytoin 15 to 20 mg/kg as the next routine step', False, 'An ACOG checklist alternative only when magnesium fails or cannot be used.'),
 ('Prepare for an emergency cesarean during the seizure', False, 'Stabilize first; delivery planning follows.'),
 ('Stop the magnesium because it did not prevent the seizure', False, 'Magnesium remains the best agent: give the extra dose and continue.')],
('ld11', 1): [
 ('Ask OB and neurology for another plan, such as levetiracetam', True, 'ACOG checklist alternative; phenytoin can also worsen myasthenia.'),
 ('Verify magnesium at 1 g/h with hourly reflex checks', False, 'The renal dose does not remove the myasthenia risk.'),
 ('Change magnesium to the IM route to limit peak levels', False, 'The route does not change neuromuscular blockade.'),
 ('Substitute phenytoin 15 to 20 mg/kg as the standard plan', False, 'Can worsen myasthenia; not automatic.')],
('ld12', 0): [
 ('Lower cerebral palsy risk in babies born before 32 weeks', True, 'ACOG CO 455.'),
 ('Stop preterm contractions for up to 48 hours', False, 'That is tocolysis (indomethacin before 32 weeks).'),
 ('Prevent maternal eclamptic seizures in labor', False, 'No preeclampsia here; the order is for the baby.'),
 ('Speed fetal lung maturity before preterm birth', False, 'That is antenatal corticosteroids.')],
('ld15', 0): [
 ('Oxytocin 10 to 40 units in 500 to 1,000 mL IV', True, 'First line (ACOG PB 183); 10 units IM if no IV.'),
 ('Methylergonovine 0.2 mg IM every 2 to 4 hours', False, 'Second line, and contraindicated with hypertension.'),
 ('Carboprost 250 mcg IM every 15 to 90 minutes', False, 'Second line, contraindicated in asthma.'),
 ('Misoprostol 600 to 1,000 mcg orally or rectally', False, 'Second line.')],
('ld16', 2): [
 ('Strong CYP3A4 inhibitors such as clarithromycin', True, 'Boxed warning: vasospasm and ischemia.'),
 ('Strong P-gp inducers such as rifampin', False, 'That class matters for DOACs.'),
 ('Serotonergic drugs such as sertraline', False, 'That is the linezolid warning.'),
 ('QT prolonging drugs such as ondansetron', False, 'Not this boxed warning.')],
('ld19', 0): [
 ('1 g IV over 10 minutes; repeat 1 g after 30 minutes if needed', True, 'WOMAN trial; ACOG PB 183.'),
 ('1 g IV over 10 minutes, then 1 g infused over 8 hours', False, 'That is the CRASH-2 trauma regimen.'),
 ('1 g IV push over 1 minute; repeat 1 g after 5 minutes', False, 'Rapid push raises hypotension risk.'),
 ('10 mg/kg IV over 10 minutes, then 1 mg/kg/h infusion', False, 'Cardiac surgery style weight based dosing, not PPH.')],
('ld19', 2): [
 ('It blocks clot breakdown, so new clots stay in place', True, 'Antifibrinolytic.'),
 ('It contracts the uterine muscle around the vessels', False, 'Uterotonics do that.'),
 ('It replaces factors II, VII, IX and X in the blood', False, 'That is 4F-PCC.'),
 ('It activates platelets at the placental site', False, 'Not TXA\'s mechanism.')],
('ld20', 0): [
 ('Vial mix ups with spinal anesthetics: intrathecal TXA is toxic', True, 'ISMP 2024; about 50% mortality in reported cases.'),
 ('Seizures occur at the usual 1 g IV dose', False, 'Seizures are mostly with high doses.'),
 ('A dangerous interaction with oxytocin infusions', False, 'No such interaction.'),
 ('Frequent dosing after the 3 hour benefit window', False, 'A dosing issue, not the reason for the listing.')],
('ld24', 0): [
 ('Clindamycin susceptibility, including inducible resistance', True, 'CO 797.'),
 ('A penicillin skin test before any antibiotic', False, 'Useful later, not the decision now.'),
 ('A vancomycin trough before the first dose', False, 'Not needed to choose a drug.'),
 ('Her creatinine clearance before clindamycin', False, 'Clindamycin is not renally adjusted.')],
('ld24', 1): [
 ('20 mg/kg every 8 hours, max 2 g per dose', True, 'CO 797: 72 kg x 20 = 1,440 mg (round per protocol).'),
 ('1 g every 12 hours regardless of weight', False, 'That is the CO 712 intraamniotic infection alternative.'),
 ('15 mg/kg every 12 hours, max 2 g per dose', False, 'General adult maintenance, not the GBS regimen.'),
 ('20 to 35 mg/kg once, then levels, max 3 g', False, 'The critical illness loading range (Rybak 2020).')],
('ld25', 2): [
 ('One more dose plus clindamycin or metronidazole', True, 'CO 712.'),
 ('Stop every antibiotic once the baby is delivered', False, 'That is the vaginal delivery pathway.'),
 ('Continue the same regimen for 7 days after surgery', False, 'Not routine.'),
 ('One more dose plus vancomycin for MRSA coverage', False, 'Not part of the regimen.')],
('ld26', 0): [
 ('Clindamycin 900 mg every 8 hours plus gentamicin', True, 'CO 712 (vancomycin 1 g every 12 hours is the other option).'),
 ('Cefazolin 2 g every 8 hours plus gentamicin', False, 'Mild allergy regimen.'),
 ('Gentamicin 5 mg/kg every 24 hours alone', False, 'Misses gram positives.'),
 ('Aztreonam 2 g every 8 hours alone', False, 'No gram positive coverage.')],
('ld27', 1): [
 ('Mature fetal lungs; fewer RDS cases, brain bleeds and deaths', True, 'CO 713.'),
 ('Lower cerebral palsy risk for babies born before 32 weeks', False, 'That is magnesium neuroprotection.'),
 ('Stop contractions long enough to transfer the mother', False, 'That is tocolysis.'),
 ('Prevent early onset GBS infection in the newborn', False, 'Antibiotics do that.')],
('ld29', 1): [
 ('Prostaglandins keep the ductus open; NSAIDs block them', True, ''),
 ('NSAIDs raise fetal blood pressure and strain the ductus', False, 'Not the mechanism.'),
 ('NSAIDs lower fetal calcium, which weakens the ductus', False, 'Low fetal calcium is a long magnesium course effect.'),
 ('NSAIDs lower fetal glucose, which closes the ductus', False, 'Not the mechanism.')],
('ld30', 1): [
 ('A large fetal to maternal bleed found on a screening test', True, 'Kleihauer Betke or flow cytometry decides extra vials.'),
 ('A mother who weighs more than 100 kg', False, 'Dose depends on bleed size, not maternal weight.'),
 ('A baby who weighs more than 4 kg at birth', False, 'Birth weight does not decide the dose.'),
 ('Any cesarean delivery, regardless of bleeding', False, 'Route alone does not decide.')],
('ld32', 0): [
 ('Misoprostol is avoided after a cesarean (rupture risk)', True, 'PB 107.'),
 ('The dose should be 50 mcg orally every 4 hours', False, '50 mcg oral is used in some protocols, but it does not fix the uterine scar problem.'),
 ('The interval should be every 6 hours, not every 4', False, 'The interval is not the issue.'),
 ('It is fine because her incision was low transverse', False, 'Still avoided for ripening after cesarean.')],
('ld34', 1): [
 ('Recommend insulin and support dosing and teaching', True, ''),
 ('Verify metformin because the prescriber chose it', False, 'Recommend the guideline option.'),
 ('Hold all diabetes therapy until delivery', False, 'Uncontrolled glucose harms the baby.'),
 ('Recommend glyburide because it is easier to take', False, 'Crosses the placenta (neonatal hypoglycemia).')],
('ld35', 1): [
 ('Low dose aspirin 81 mg for preeclampsia prevention', True, 'FDA exception.'),
 ('Indomethacin for preterm labor at any gestational age', False, 'Limited to before 32 weeks and 48 hours.'),
 ('Ibuprofen at doses of 400 mg or less per dose', False, 'No dose based exception.'),
 ('Ketorolac for 5 days or less after 20 weeks', False, '5 days is the ketorolac maximum duration in adults generally, not a pregnancy exception.')],
('ld38', 0): [
 ('No longer a blanket contraindication; most stop', True, 'FDA 2021: very high risk patients may continue with their doctor.'),
 ('Still absolutely contraindicated for every patient', False, 'Outdated.'),
 ('Continue for every patient; benefit outweighs risk', False, 'Most stop.'),
 ('Switch every patient to ezetimibe for the pregnancy', False, 'Not the guidance.')],
}

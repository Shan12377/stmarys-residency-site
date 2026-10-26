# Rewritten options for L&D cases ld01 to ld20 (Pharmacy Decoder rules: adjacent real values, parallel length, boundary teaching).
# Key: (case id, step index) -> list of (text, correct, why).
R = {
('ld01', 0): [
 ('Systolic 160 or more OR diastolic 110 or more, persisting 15 minutes', True, 'ACOG CO 767: either number, confirmed 15 minutes apart, defines severe range and starts the treatment clock.'),
 ('Systolic 160 or more AND diastolic 110 or more, persisting 15 minutes', False, '"And" is the trap: requiring both numbers misses most severe range patients. ACOG uses either one.'),
 ('Systolic 140 or more OR diastolic 90 or more, on two readings 4 hours apart', False, '140/90 on two readings 4 hours apart is the definition of gestational hypertension (PB 222), not the urgent treatment threshold.'),
 ('Systolic 180 or more OR diastolic 120 or more, persisting 15 minutes', False, '180/120 is the nonpregnant hypertensive emergency threshold. Pregnancy treats lower, at 160/110.')],
('ld01', 1): [
 ('Within 30 to 60 minutes of confirmation', True, 'ACOG CO 767: treat as soon as possible, within 30 to 60 minutes, to lower stroke risk.'),
 ('Within 10 minutes, before a repeat reading', False, '10 minutes is the labetalol recheck interval, not the treatment start window; severe range must persist 15 minutes first.'),
 ('Within 2 hours, after labs return', False, 'Labs (platelets, LFTs, creatinine) guide the preeclampsia workup but never delay severe BP treatment.'),
 ('Within 4 hours, once delivery is planned', False, '4 hours is the interval between the two readings that diagnose gestational hypertension, not a treatment window.')],
('ld01', 2): [
 ('IV labetalol', True, 'First line (ACOG CO 767).'),
 ('IV hydralazine', True, 'First line (ACOG CO 767).'),
 ('Immediate release oral nifedipine', True, 'First line, and the go to option without IV access (ACOG CO 767).'),
 ('Oral methyldopa', False, 'Methyldopa is an option for chronic hypertension in pregnancy, but too slow for acute severe range BP.'),
 ('Extended release oral nifedipine', False, 'ER nifedipine is for chronic or postpartum maintenance; the acute algorithm uses immediate release.')],
('ld02', 0): [
 ('Labetalol 40 mg IV over 2 minutes, recheck in 10 minutes', True, 'ACOG algorithm: 20, then 40, then 80 mg, each with a 10 minute recheck.'),
 ('Labetalol 20 mg IV over 2 minutes, recheck in 10 minutes', False, 'Repeating 20 mg is a nonescalating pattern; the algorithm doubles to 40 mg when BP stays severe.'),
 ('Labetalol 80 mg IV over 2 minutes, recheck in 10 minutes', False, '80 mg is the third step, after 40 mg fails. Skipping steps raises overshoot risk.'),
 ('Labetalol 40 mg IV over 2 minutes, recheck in 20 minutes', False, '20 minutes is the recheck time for hydralazine and nifedipine, which act more slowly. Labetalol is rechecked at 10.')],
('ld02', 1): [
 ('Switch to hydralazine 10 mg IV and get urgent consultation', True, 'After labetalol 20, 40 and 80 mg fail, ACOG switches drug class (hydralazine 10 mg) and calls for MFM, anesthesia or critical care help.'),
 ('Give labetalol 80 mg IV again and recheck in 10 minutes', False, 'Repeat 80 mg doses (up to a 300 mg cumulative label cap) are used outside obstetrics; the ACOG algorithm switches class after 80 mg.'),
 ('Start a labetalol infusion at 1 to 2 mg/min', False, 'A labetalol infusion is an option only with consultation and ICU level care, not the next algorithm step on L&D.'),
 ('Give nifedipine extended release 30 mg orally', False, 'ER nifedipine is a maintenance drug; the acute algorithm uses immediate release and only when labetalol or hydralazine is not working.')],
('ld02', 2): [
 ('Asthma', True, 'Beta blockade can trigger bronchospasm; start with hydralazine or nifedipine.'),
 ('Heart block or heart rate below 60', True, 'Labetalol slows conduction further.'),
 ('Decompensated heart failure', True, 'Beta blockade worsens acute heart failure.'),
 ('Maternal heart rate above 110', False, 'The opposite: with HR above 110, labetalol is preferred because it slows the heart (CMQCC algorithm).'),
 ('Gestational diabetes', False, 'Not a contraindication. Labetalol can mask hypoglycemia symptoms, so counsel, but it is still used.')],
('ld03', 0): [
 ('5 to 10 mg IV over 2 minutes, recheck in 20 minutes', True, 'ACOG CO 767. Hydralazine peaks in 10 to 20 minutes.'),
 ('5 to 10 mg IV over 2 minutes, recheck in 10 minutes', False, '10 minutes is the labetalol recheck; hydralazine has not peaked yet, so you risk stacking doses.'),
 ('20 mg IV over 2 minutes, recheck in 20 minutes', False, '20 mg is above the ACOG starting dose and raises overshoot risk (fetal heart rate changes).'),
 ('10 to 20 mg IV over 2 minutes, recheck in 20 minutes', False, 'Labetalol 10 to 20 mg IV is the post thrombolysis stroke BP dose, not hydralazine for pregnancy.')],
('ld03', 1): [
 ('Hydralazine 10 mg IV again, then switch to labetalol if still severe', True, 'ACOG: repeat hydralazine 10 mg at 20 minutes; if still severe, labetalol 20 mg (asthma permitting) and get consultation.'),
 ('Labetalol 20 mg IV now, since hydralazine failed once', False, 'Switching after a single hydralazine dose skips the second hydralazine step; and this patient has asthma.'),
 ('Immediate release nifedipine 10 mg now, alongside more hydralazine', False, 'Adding a second agent while the first is still peaking stacks drops in BP and harms placental flow.'),
 ('Hydralazine 20 mg IV, then recheck in 20 minutes', False, 'The second hydralazine dose in the ACOG algorithm is 10 mg, not 20 mg.')],
('ld03', 2): [
 ('Overshoot hypotension and fetal heart rate changes', True, 'Too fast a drop reduces placental blood flow.'),
 ('Reflex tachycardia and headache', True, 'Classic hydralazine effects; headache can mimic worsening preeclampsia.'),
 ('Bronchospasm in patients with asthma', False, 'That is the labetalol warning; hydralazine is the preferred choice in asthma.'),
 ('Neonatal bradycardia and hypoglycemia', False, 'Those are labetalol warnings (beta blockade crosses the placenta).')],
('ld04', 0): [
 ('Immediate release nifedipine 10 mg PO', True, 'ACOG first line oral option without IV access.'),
 ('Extended release nifedipine 30 mg PO', False, 'ER is for chronic or postpartum maintenance; onset is too slow for acute severe BP.'),
 ('Hydralazine 10 mg PO', False, 'Oral hydralazine is a slow chronic agent; ACOG\'s acute hydralazine doses are IV (or IM).'),
 ('Labetalol 200 mg PO', False, 'Oral labetalol is a maintenance dose for chronic hypertension, not the acute algorithm.')],
('ld04', 1): [
 ('Recheck in 20 minutes; if still severe, 20 mg, then 20 mg again', True, 'ACOG: 10, 20, 20 mg with 20 minute rechecks, then switch to labetalol.'),
 ('Recheck in 10 minutes; if still severe, 20 mg, then 40 mg', False, '10 minute rechecks and doubling doses describe IV labetalol, not oral nifedipine.'),
 ('Recheck in 20 minutes; if still severe, 10 mg every 20 minutes', False, 'The nifedipine algorithm escalates to 20 mg after the first 10 mg dose.'),
 ('Recheck in 60 minutes; if still severe, 30 mg ER', False, 'ER nifedipine is maintenance; waiting 60 minutes breaks the 30 to 60 minute treatment goal.')],
('ld04', 2): [
 ('The label warns against combining with calcium channel blockers; ACOG still uses them together with close monitoring', True, 'Label: avoid with calcium channel blockers such as nifedipine; ACOG CO 767 notes the combination is used for severe BP because data do not show more neuromuscular blockade.'),
 ('The combination is absolutely contraindicated; stop magnesium to give nifedipine', False, 'Seizure prevention is not traded away for a BP drug; ACOG accepts the combination with monitoring.'),
 ('There is no interaction because they act on different receptors', False, 'Both block calcium entry; additive hypotension and neuromuscular effects are possible.'),
 ('The magnesium dose must be halved whenever nifedipine is given', False, 'Magnesium is reduced for kidney impairment (label: 1 g/h), not for nifedipine.')],
('ld05', 0): [
 ('ACE inhibitors are contraindicated in pregnancy (fetal kidney injury)', True, 'Stop and switch; ACE inhibitors and ARBs cause fetal renal damage and low amniotic fluid.'),
 ('Lisinopril is fine in pregnancy but must be lowered to 10 mg', False, 'No dose of an ACE inhibitor is acceptable in pregnancy.'),
 ('Lisinopril is fine until 34 weeks, then switch', False, 'Fetal kidney injury comes from second and third trimester exposure, so stopping later is worse.'),
 ('Only ARBs are contraindicated; ACE inhibitors are allowed', False, 'Both ACE inhibitors and ARBs are contraindicated in pregnancy.')],
('ld05', 1): [
 ('Labetalol', True, 'Preferred oral agent (ACC 2026; ACOG).'),
 ('Nifedipine extended release', True, 'Preferred oral agent.'),
 ('Methyldopa', True, 'Long track record in pregnancy; less used now because of sedation.'),
 ('Atenolol', False, 'Atenolol is linked to fetal growth restriction; not preferred.'),
 ('Enalapril', False, 'Enalapril is preferred only after delivery (breastfeeding), never during pregnancy.')],
('ld05', 2): [
 ('Tell the OB team about the exposure so they can review amniotic fluid and fetal growth', True, 'The harm is to fetal kidneys; ultrasound review is the follow up.'),
 ('Order a maternal potassium level and stop', False, 'Potassium matters for ACE inhibitors in general, but the key pregnancy issue is fetal exposure.'),
 ('Restart lisinopril after delivery while breastfeeding', False, 'Enalapril (or captopril) is the studied ACE inhibitor in breastfeeding, not lisinopril.'),
 ('Report a near miss only; no clinical follow up needed', False, 'The drug was taken for weeks: this is an exposure needing clinical follow up, not only a report.')],
('ld06', 0): [
 ('Yes: 160 or 110 for 15 minutes still means treat within 30 to 60 minutes', True, 'ACOG CO 767 applies postpartum; postpartum stroke and eclampsia are real risks.'),
 ('No: postpartum severe range BP can wait until the 1 week visit', False, 'The 1 week (or 72 hour) visit is for BP checks in hypertensive patients, not for treating severe range BP.'),
 ('Yes, but the threshold rises to 180/120 after delivery', False, '180/120 is the nonpregnant emergency threshold; postpartum stays at 160/110.'),
 ('No: only treat if she also has a headache or vision change', False, 'Symptoms add concern but are not required; numbers alone qualify.')],
('ld06', 1): [
 ('Labetalol', True, 'Compatible with breastfeeding (ACC; LactMed).'),
 ('Nifedipine ER', True, 'Compatible with breastfeeding.'),
 ('Enalapril', True, 'Preferred ACE inhibitor in breastfeeding; the pregnancy ban ends at delivery.'),
 ('Atenolol', False, 'Atenolol concentrates in milk and has caused infant bradycardia; not preferred.'),
 ('Lisinopril', False, 'Less infant data than enalapril or captopril; not the studied first choice.')],
('ld07', 0): [
 ('Prevent eclamptic seizures', True, 'Magnesium is seizure prophylaxis in preeclampsia with severe features.'),
 ('Lower blood pressure', False, 'Magnesium is not an antihypertensive; severe BP still needs labetalol, hydralazine or nifedipine.'),
 ('Stop preterm contractions (tocolysis)', False, 'Magnesium was used as a tocolytic, but at 32 weeks with severe preeclampsia the indication is seizure prevention.'),
 ('Fetal neuroprotection', False, 'Neuroprotection is a separate indication for anticipated delivery before 32 weeks; she is 32 weeks with severe features.')],
('ld07', 1): [
 ('Yes: load 4 to 6 g, then 1 to 2 g/h', True, 'Label and ACOG PB 222.'),
 ('No: the load should be 2 to 4 g', False, '2 to 4 g is the extra dose for a seizure that occurs while already on magnesium.'),
 ('No: maintenance should be 1 g/h because of the 6 g load', False, '1 g/h is the renal impairment maintenance in the label; her kidneys are normal.'),
 ('No: the load should be 10 g', False, '10 g (5 g each buttock) is the IM regimen when there is no IV access.')],
('ld07', 2): [
 ('Premixed bag on a dedicated pump channel', True, 'ISMP high alert safeguards.'),
 ('Load and maintenance programmed separately, with an independent double check', True, 'Prevents the whole bag running at the bolus rate.'),
 ('Calcium gluconate 1 g at the bedside', True, 'The antidote must be ready before the drip starts.'),
 ('Infuse through the same channel as oxytocin to save a pump', False, 'Oxytocin and magnesium must be kept apart; mix ups between them are a known L&D error.'),
 ('Calcium chloride 1 g at the bedside instead of gluconate', False, 'Calcium chloride is a code and central line drug; obstetric magnesium toxicity protocols use calcium gluconate 1 g peripherally.')],
('ld07', 3): [
 ('24 hours after delivery (or after the last seizure)', True, 'ACOG PB 222.'),
 ('12 hours after delivery', False, '12 hours is the maximum duration of the fetal neuroprotection regimen, not postpartum seizure prophylaxis.'),
 ('Until delivery only', False, 'The postpartum period still carries eclampsia risk.'),
 ('5 to 7 days', False, '5 to 7 days is the label warning limit for continuous use in pregnancy, not a target duration.')],
('ld08', 0): [
 ('Magnesium toxicity, made worse by low urine output', True, 'Absent reflexes, slow breathing and drowsiness with oliguria.'),
 ('Expected magnesium effect at a therapeutic level', False, 'At therapeutic levels (label 2.5 to 5 mEq/L) reflexes are still present.'),
 ('A postictal state after an unwitnessed eclamptic seizure', False, 'Possible to consider, but absent reflexes plus RR 11 with oliguria point to magnesium excess.'),
 ('Opioid induced respiratory depression', False, 'Opioids slow breathing but do not abolish deep tendon reflexes.')],
('ld08', 1): [
 ('Stop the magnesium infusion now', True, 'First step.'),
 ('Calcium gluconate 1 g IV (10 mL of 10%) over 2 to 3 minutes', True, 'Antidote (ACOG).'),
 ('Support breathing and call OB and anesthesia', True, 'Airway first.'),
 ('Lower the rate to 1 g/h and recheck in an hour', False, '1 g/h is the renal impairment starting maintenance, not a response to toxicity with RR 11.'),
 ('Calcium gluconate 3 g IV over 10 minutes', False, '3 g is the calcium gluconate dose in massive transfusion or some hyperkalemia protocols, not the magnesium antidote dose.')],
('ld08', 2): [
 ('Reflexes fade above about 4 mEq/L; respiratory paralysis risk near 10 mEq/L', True, 'Label: reflexes diminish above 4 and may be absent at 10, when respiratory paralysis is a hazard.'),
 ('Reflexes and breathing both fail at about 10 mEq/L', False, 'Reflexes are lost first, which is why they are the early warning.'),
 ('Breathing fails near 4 mEq/L; reflexes near 10 mEq/L', False, 'Reversed.'),
 ('Reflexes fade only above the 2.5 to 5 mEq/L target range at 12 mEq/L', False, '2.5 to 5 is the target range; reflexes begin to fade just above 4.')],
('ld08', 3): [
 ('STAT serum magnesium and creatinine', True, 'Confirms the level and the kidney cause.'),
 ('STAT ionized calcium only', False, 'Calcium is the antidote, but the magnesium level and kidney function are what you need.'),
 ('Platelets and liver enzymes only', False, 'Part of the HELLP workup, not the toxicity workup.'),
 ('Serum potassium only', False, 'Not the cause of these findings.')],
('ld09', 0): [
 ('Load 4 g, then 1 g/h, max 20 g per 48 h, with frequent levels', True, 'Label for severe renal impairment or oliguria.'),
 ('Load 6 g, then 2 g/h, with levels every 24 hours', False, '6 g then 2 g/h is a normal kidney regimen (also the neuroprotection regimen); too much here.'),
 ('Load 2 to 4 g, then hold maintenance until delivery', False, '2 to 4 g is the extra dose for a seizure on magnesium; holding all maintenance removes prophylaxis.'),
 ('Load 4 g, then 1 g/h, max 30 to 40 g per 24 h', False, '30 to 40 g per 24 h is the general label daily maximum, not the renal limit of 20 g per 48 h.')],
('ld09', 1): [
 ('2.5 to 5 mEq/L (3 to 6 mg/dL)', True, 'Label target for seizure control.'),
 ('1.5 to 2.5 mEq/L (1.8 to 3 mg/dL)', False, 'That is about the normal serum magnesium range, too low for seizure prophylaxis.'),
 ('5 to 8 mEq/L (6 to 10 mg/dL)', False, 'Above 4 reflexes start to fade; this range overlaps toxicity.'),
 ('10 to 12 mEq/L (12 to 15 mg/dL)', False, 'At 10 respiratory paralysis is a hazard.')],
('ld10', 0): [
 ('Extra 2 to 4 g IV over 5 minutes', True, 'ACOG PB 222 for a seizure on magnesium.'),
 ('A new 4 to 6 g load over 20 minutes', False, '4 to 6 g over 15 to 30 minutes is the initial load, not the rescue dose, and 20 minutes is too slow during a seizure.'),
 ('Lorazepam 2 to 4 mg IV instead of more magnesium', False, 'Lorazepam is the ACOG checklist option when magnesium fails or cannot be used, not the first step here.'),
 ('Increase maintenance to 3 g/h', False, '3 g/h exceeds the 1 to 2 g/h maintenance range and does not treat the active seizure.')],
('ld10', 1): [
 ('Airway and safety, severe BP treatment, and a toxicity check before more doses', True, 'Treat the whole patient: seizure, BP and magnesium level.'),
 ('Phenytoin 15 to 20 mg/kg as the routine next step', False, 'Phenytoin is an ACOG checklist alternative only when magnesium fails or is contraindicated.'),
 ('Emergency cesarean during the seizure', False, 'Stabilize the mother first; delivery planning follows stabilization.'),
 ('Stop magnesium because it failed', False, 'Magnesium is still the best agent; give the extra dose and continue.')],
('ld11', 0): [
 ('It blocks neuromuscular transmission and can trigger myasthenic crisis', True, 'Label contraindication: myasthenia gravis.'),
 ('It reduces pyridostigmine absorption from the gut', False, 'Not the mechanism of harm; IV magnesium acts at the neuromuscular junction.'),
 ('It causes heart block in myasthenia', False, 'Heart block is a separate label contraindication, not the myasthenia risk.'),
 ('It is safe at the renal dose of 1 g/h', False, 'Dose lowering does not make it safe; myasthenia is a contraindication.')],
('ld11', 1): [
 ('Ask OB and neurology to choose another seizure plan, such as levetiracetam', True, 'ACOG checklist alternatives include levetiracetam 500 mg IV or PO and benzodiazepines; phenytoin can also worsen myasthenia.'),
 ('Verify magnesium at 1 g/h with hourly reflexes', False, 'The renal dose does not remove the myasthenia risk.'),
 ('Give magnesium IM instead of IV', False, 'The route does not change neuromuscular blockade.'),
 ('Substitute phenytoin 15 to 20 mg/kg as standard', False, 'Phenytoin is an option, but it can worsen myasthenia, so it is not the automatic choice.')],
('ld12', 0): [
 ('Lower the risk of cerebral palsy before 32 weeks', True, 'ACOG CO 455.'),
 ('Stop contractions for 48 hours', False, 'That describes tocolysis (for example indomethacin before 32 weeks for up to 48 hours).'),
 ('Prevent maternal seizures', False, 'She has no preeclampsia; this order is for the baby.'),
 ('Speed fetal lung maturity', False, 'That is the job of antenatal corticosteroids (betamethasone).')],
('ld12', 1): [
 ('6 g over 20 to 30 minutes, then 2 g/h for up to 12 hours', True, 'BEAM based protocol (MAHEC).'),
 ('4 to 6 g over 15 to 20 minutes, then 1 to 2 g/h until 24 hours postpartum', False, 'That is the preeclampsia seizure prophylaxis regimen.'),
 ('2 to 4 g over 5 minutes, repeated as needed', False, 'That is the rescue dose for a seizure on magnesium.'),
 ('4 g load, then 1 g/h for 5 to 7 days', False, '5 to 7 days is the label warning limit (fetal bone problems), never a planned course.')],
('ld13', 0): [
 ('Beyond 5 to 7 days: fetal low calcium and bone problems', True, 'FDA label warning (2013).'),
 ('Beyond 24 hours: maternal kidney failure', False, '24 hours is the usual postpartum prophylaxis duration, not a toxicity limit.'),
 ('Beyond 48 hours: fetal ductus closure', False, '48 hours is the indomethacin tocolysis limit (ductal constriction).'),
 ('Beyond 12 hours: loss of neuroprotective benefit', False, '12 hours is the maximum duration of the neuroprotection protocol, not a safety warning.')],
('ld13', 1): [
 ('Flag the duration to the OB and ask the goal of therapy', True, 'Long term magnesium tocolysis is not recommended.'),
 ('Continue to 10 days as long as reflexes are present', False, 'Reflexes guide toxicity, not the fetal bone risk.'),
 ('Switch to indomethacin for another 2 weeks', False, 'Indomethacin is limited to 48 hours and before 32 weeks.'),
 ('Lower the rate to 1 g/h and continue', False, '1 g/h is the renal dose; it does not address duration risk.')],
('ld14', 0): [
 ('Tachysystole: lower or stop oxytocin', True, 'More than 5 contractions in 10 minutes (averaged over 30 minutes) with a worrying tracing.'),
 ('Normal active labor: continue the current rate', False, 'Six in 10 minutes with fetal heart concerns is not normal.'),
 ('Placental abruption: give TXA 1 g', False, 'Abruption is possible but TXA is a postpartum hemorrhage drug, not the first move for tachysystole.'),
 ('Uterine atony: give methylergonovine', False, 'Atony is the opposite problem (too little contraction), after delivery.')],
('ld14', 1): [
 ('One standard concentration in the pump library', True, 'ISMP.'),
 ('Separate storage and labels from magnesium bags', True, 'Known mix up.'),
 ('Watch fluids and sodium on long, high dose infusions', True, 'Oxytocin acts like ADH (water intoxication).'),
 ('Run it through the same line as magnesium to limit IV sites', False, 'Mixing high alert L&D drugs on one channel increases error risk.'),
 ('Use custom concentrations to fit each patient\'s fluid needs', False, 'Custom concentrations defeat the smart pump safety net.')],
('ld15', 0): [
 ('Oxytocin 10 to 40 units in 500 to 1,000 mL IV (or 10 units IM)', True, 'ACOG PB 183 first line for atony.'),
 ('Methylergonovine 0.2 mg IM', False, 'Second line, after oxytocin, and contraindicated with hypertension.'),
 ('Carboprost 250 mcg IM', False, 'Second line; contraindicated in asthma.'),
 ('Misoprostol 600 to 1,000 mcg', False, 'Second line; useful when the others are contraindicated.')],
('ld15', 1): [
 ('Contracting muscle squeezes the open placental vessels shut', True, 'The "living ligature."'),
 ('It raises platelet counts', False, 'No.'),
 ('It blocks breakdown of clots', False, 'That is how TXA works.'),
 ('It constricts arteries throughout the body', False, 'That is methylergonovine, which is why it raises BP.')],
('ld16', 0): [
 ('No: contraindicated with hypertension and preeclampsia', True, 'ACOG PB 183.'),
 ('Yes, at half the usual dose (0.1 mg)', False, 'No dose makes it safe with preeclampsia.'),
 ('Yes, if given IM instead of IV', False, 'Both routes constrict blood vessels.'),
 ('Yes, if her BP is below 160/110', False, '160/110 is the severe range treatment threshold, not a methylergonovine cutoff.')],
('ld16', 1): [
 ('Carboprost 250 mcg IM (no asthma)', True, ''),
 ('Misoprostol 600 to 1,000 mcg once', True, ''),
 ('TXA 1 g IV over 10 minutes, within 3 hours of birth', True, ''),
 ('Methylergonovine 0.2 mg IM after BP is treated', False, 'Still contraindicated with preeclampsia.'),
 ('Oxytocin 10 units IV push', False, 'Oxytocin is given as an infusion or IM; rapid undiluted IV push can cause hypotension.')],
('ld16', 2): [
 ('Strong CYP3A4 inhibitors (protease inhibitors, clarithromycin, azoles)', True, 'Boxed warning: vasospasm and ischemia.'),
 ('P-gp inducers such as rifampin', False, 'That interaction class matters for DOACs, not the methylergonovine boxed warning.'),
 ('Serotonergic drugs such as SSRIs', False, 'That is the linezolid warning.'),
 ('QT prolonging drugs such as ondansetron', False, 'QT stacking matters for many drugs, but it is not this boxed warning.')],
('ld17', 0): [
 ('Carboprost', True, 'Bronchospasm in asthma.'),
 ('Methylergonovine', False, 'Avoided with hypertension, not asthma; BP is normal here.'),
 ('Misoprostol', False, 'Safe in asthma.'),
 ('Tranexamic acid', False, 'Safe in asthma.')],
('ld17', 1): [
 ('250 mcg IM every 15 to 90 minutes, max 8 doses (2 mg)', True, 'ACOG PB 183.'),
 ('0.2 mg IM every 2 to 4 hours', False, 'That is methylergonovine.'),
 ('250 mcg IM every 4 hours, max 3 doses', False, 'The carboprost interval can be as short as 15 minutes.'),
 ('1 g IV over 10 minutes, repeat once after 30 minutes', False, 'That is TXA.')],
('ld18', 0): [
 ('Misoprostol 600 to 1,000 mcg', True, 'Safe with asthma and hypertension.'),
 ('TXA 1 g IV over 10 minutes (if within 3 hours)', True, 'Antifibrinolytic, not a uterotonic; 90 minutes after birth is inside the window.'),
 ('Methylergonovine 0.2 mg IM', False, 'Contraindicated with preeclampsia.'),
 ('Carboprost 250 mcg IM', False, 'Contraindicated with asthma.')],
('ld18', 1): [
 ('Fever and shivering', True, 'Common with misoprostol, especially higher doses.'),
 ('Bronchospasm', False, 'Carboprost.'),
 ('Severe hypertension', False, 'Methylergonovine.'),
 ('Water intoxication', False, 'Long high dose oxytocin.')],
('ld19', 0): [
 ('1 g IV over 10 minutes; a second 1 g if bleeding continues after 30 minutes', True, 'WOMAN trial and ACOG PB 183.'),
 ('1 g IV over 10 minutes, then 1 g over 8 hours', False, 'That is the CRASH-2 trauma regimen.'),
 ('1 g IV push over 1 minute, repeat in 5 minutes', False, 'Rapid push raises hypotension risk; the PPH dose is over 10 minutes.'),
 ('10 mg/kg IV over 10 minutes, then 1 mg/kg/h', False, 'Weight based TXA regimens are used in cardiac surgery, not PPH.')],
('ld19', 1): [
 ('Mortality benefit was seen when given within 3 hours of birth', True, 'WOMAN trial.'),
 ('It only works within 1 hour of birth', False, 'Earlier is better, but the window used is 3 hours.'),
 ('It works best after 6 hours, once clots form', False, 'Benefit fades with time.'),
 ('Timing matters only in trauma, not PPH', False, 'Time matters in both (CRASH-2 and WOMAN).')],
('ld19', 2): [
 ('Blocks clot breakdown (antifibrinolytic), so new clots stay in place', True, ''),
 ('Contracts the uterus', False, 'Uterotonics do that (oxytocin, methylergonovine, carboprost, misoprostol).'),
 ('Replaces clotting factors', False, 'That is 4F-PCC or plasma.'),
 ('Activates platelets', False, 'Desmopressin has some platelet effect; TXA does not.')],
('ld20', 0): [
 ('Look alike vials mixed up with spinal anesthetics; intrathecal TXA is a neurotoxin', True, 'ISMP 2024; about 50% mortality in reported cases.'),
 ('It causes seizures at normal IV doses', False, 'Seizures occur mainly with high doses; that was not the reason for the listing.'),
 ('It interacts with oxytocin', False, 'No.'),
 ('It is often given after the 3 hour window', False, 'A dosing issue, not the reason for the high alert listing.')],
('ld20', 1): [
 ('Store TXA away from neuraxial anesthetics', True, ''),
 ('Label TXA syringes "IV only"', True, ''),
 ('Use premixed IV bags when possible', True, ''),
 ('Store TXA in the epidural kit for fast access', False, 'Exactly the setup that caused the errors.'),
 ('Draw TXA into an unlabeled syringe next to bupivacaine', False, 'Unlabeled syringes are a never event.')],
}

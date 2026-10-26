# Balancing fixes (m01, m04, m05) and Module 6 (ID) rewrites.
R = {
('ld35', 2): [
 ('Acetaminophen', True, ''),
 ('Naproxen sodium', False, 'Another NSAID.'),
 ('Celecoxib', False, 'Still an NSAID.'),
 ('Ketorolac', False, 'Still an NSAID.')],
('po06', 0): [
 ('Feeds bind it; hold feeds around each dose', True, 'Often 1 to 2 hours before and after; monitor levels.'),
 ('Feeds speed up phenytoin metabolism', False, 'Binding, not metabolism.'),
 ('Feeds have no effect on phenytoin', False, 'Well known interaction.'),
 ('Feeds raise phenytoin blood levels', False, 'They lower absorption.')],
('po07', 2): [
 ('Platelets and counts after 2 weeks', True, 'Myelosuppression.'),
 ('INR weekly during the course', False, 'Warfarin monitoring.'),
 ('Serum potassium every day', False, 'Not a linezolid issue.'),
 ('TSH once a month', False, 'Not a linezolid issue.')],
('ac01', 0): [
 ('2 of 3: age 80+, weight 60 kg or less, SCr 1.5+', True, 'Eliquis label, AF.'),
 ('CrCl 15 to 50 mL/min by Cockcroft Gault', False, 'The rivaroxaban and edoxaban AF reduction rule.'),
 ('CrCl 15 to 30 mL/min by Cockcroft Gault', False, 'The dabigatran AF reduction rule (75 mg BID).'),
 ('Age 75 or older, with or without other factors', False, 'Age 75 counts in CHA2DS2-VASc, not apixaban dosing.')],
('ac02', 1): [
 ('15 mg BID x 21 days, then 20 mg daily', True, 'With food.'),
 ('10 mg BID x 7 days, then 5 mg BID', False, 'That is apixaban.'),
 ('15 mg daily x 21 days, then 20 mg daily', False, 'The first phase is twice daily.'),
 ('20 mg daily from the first day onward', False, 'Skips the 21 day twice daily phase.')],
('ac05', 1): [
 ('Triple positive antiphospholipid syndrome', True, 'More clots on DOACs.'),
 ('First DVT after a knee replacement', False, 'DOACs are fine.'),
 ('Cancer associated VTE on chemotherapy', False, 'DOACs or LMWH are used.'),
 ('Atrial fibrillation with CrCl 60 mL/min', False, 'DOACs preferred.')],
('ac06', 0): [
 ('Apixaban 2.5 mg BID, reviewed at least yearly', True, 'CHEST 2021 (or rivaroxaban 10 mg daily).'),
 ('Stop at 6 months for all unprovoked VTE', False, 'High recurrence after stopping.'),
 ('Apixaban 10 mg BID long term for protection', False, '10 mg BID is the first 7 days only.'),
 ('Apixaban 5 mg BID for exactly 12 more months', False, 'No set stop date; reduced dose suggested.')],
('ac06', 1): [
 ('VTE provoked by surgery (major transient risk)', True, 'Treat 3 months, then stop.'),
 ('Unprovoked VTE with a low bleeding risk', False, 'The group that benefits.'),
 ('VTE with active cancer under treatment', False, 'Usually continued.'),
 ('A second unprovoked VTE event', False, 'Strong reason to continue.')],
('ac07', 1): [
 ('Hold warfarin and recheck the INR', True, 'Crowther 2009: vitamin K usually not needed at INR 4.5 to 10.'),
 ('Oral vitamin K 2.5 to 5 mg now', False, 'For INR above 10 without bleeding.'),
 ('Vitamin K 10 mg IV now, slowly', False, 'For major bleeding.'),
 ('4F-PCC 25 units/kg now', False, 'For major bleeding or urgent surgery.')],
('ac08', 1): [
 ('Vitamin K 10 mg IV, slowly', True, 'Prevents INR rebound.'),
 ('Vitamin K 2.5 mg by mouth', False, 'For INR above 10 without bleeding.'),
 ('Protamine 50 mg IV slowly', False, 'Reverses heparin.'),
 ('Tranexamic acid 1 g IV', False, 'Not the required partner.')],
('ac09', 0): [
 ('4F-PCC per protocol', True, 'Often 50 units/kg or a fixed dose; andexanet withdrawn December 2025.'),
 ('Andexanet alfa, high dose', False, 'Withdrawn from the US market.'),
 ('Vitamin K 10 mg IV', False, 'Warfarin only.'),
 ('Protamine 50 mg IV', False, 'Heparin only.')],
('ac09', 1): [
 ('Idarucizumab 5 g IV', True, 'Two 2.5 g vials.'),
 ('4F-PCC 50 units/kg', False, 'Idarucizumab is the specific agent.'),
 ('Idarucizumab 2.5 g IV', False, 'The dose is 5 g.'),
 ('Hemodialysis alone', False, 'Second line.')],
('ac09', 2): [
 ('About 140; not below 130', True, 'ICH 2022.'),
 ('Below 185/110 mmHg', False, 'The gate before thrombolysis.'),
 ('Below 180/105 mmHg', False, 'The post thrombolysis limit.'),
 ('About 110 to 120 mmHg', False, 'Too low.')],
('ac11', 0): [
 ('4Ts: size of fall, timing, clot, other causes', True, 'A fall over 50%, day 5 to 10.'),
 ('Platelets below 100,000 on any day', False, 'HIT is about the size of the fall.'),
 ('Platelets below 50,000 on any day', False, 'Most HIT counts stay above that.'),
 ('Any drop of 10,000 from the baseline', False, 'Too sensitive.')],
('ac12', 2): [
 ('Kidney disease, pregnancy, weight extremes', True, 'Peak about 4 hours after a dose at steady state.'),
 ('Every patient, 6 hours after each dose', False, '6 hours is UFH timing.'),
 ('Every patient, as a trough before doses', False, 'Peaks are used in special populations.'),
 ('Never; anti Xa cannot measure enoxaparin', False, 'Anti Xa is the LMWH test.')],
('ac14', 1): [
 ('Mechanical mitral valve or recent clot', True, 'Clot within 3 months; decided with cardiology or hematology.'),
 ('Anyone over 75 years old on warfarin', False, 'Age alone does not decide.'),
 ('Anyone with CHA2DS2-VASc of 3', False, 'This patient; not bridged.'),
 ('Nobody under any circumstances', False, 'Some are bridged.')],
('ac16', 0): [
 ('The bleeding patient on heparin', True, ''),
 ('The apixaban crushing question', False, 'Can wait.'),
 ('The stable INR of 3.4', False, 'Mildly high.'),
 ('Whichever call came in first', False, 'Triage by harm.')],
('ac16', 2): [
 ('Yes: crushed in water, D5W or juice', True, 'Or via NG tube (Eliquis label).'),
 ('No: it must be swallowed whole', False, 'That is dabigatran.'),
 ('Only if dissolved in milk first', False, 'Not a label option.'),
 ('Only the 2.5 mg strength may be', False, 'Both strengths.')],
('id01', 0): [
 ('Within 1 hour (shock is present)', True, 'SSC 2021.'),
 ('Within 3 hours (possible sepsis, no shock)', False, '3 hours is for possible sepsis without shock after rapid assessment.'),
 ('Within 6 hours (old early goal directed window)', False, 'The 6 hour window was the old EGDT resuscitation bundle.'),
 ('After cultures result, to avoid broad coverage', False, 'Never wait for results.')],
('id01', 1): [
 ('Verify first doses STAT and get them moving', True, ''),
 ('Full first doses even with poor kidneys', True, 'Load by weight.'),
 ('Shortest infusion drug first', True, 'Usually the beta lactam before vancomycin.'),
 ('Reduce the first beta lactam dose for CrCl 25', False, 'First doses are not reduced.'),
 ('Hold antibiotics until blood cultures are drawn twice', False, 'Draw cultures if quick; never delay.')],
('id02', 0): [
 ('Prolonged (extended) infusion after the first dose', True, 'SSC 2021 suggestion.'),
 ('Faster 3 to 5 minute push for every dose', False, 'Opposite of the time above MIC goal.'),
 ('Once daily dosing to raise the peak', False, 'That is the aminoglycoside strategy.'),
 ('Continuous infusion only for vancomycin', False, 'A vancomycin option, not the beta lactam suggestion.')],
('id02', 1): [
 ('Beta lactams: time; aminoglycosides: peak', True, 'Time above MIC vs peak/MIC.'),
 ('Both kill by time above the MIC', False, 'Aminoglycosides are concentration dependent.'),
 ('Both kill by peak concentration', False, 'Beta lactams are time dependent.'),
 ('Beta lactams: AUC; aminoglycosides: time', False, 'AUC/MIC describes vancomycin; aminoglycosides are peak driven.')],
('id03', 0): [
 ('Ceftriaxone + azithromycin', True, ''),
 ('Levofloxacin 750 mg or moxifloxacin 400 mg alone', True, ''),
 ('Vancomycin + piperacillin tazobactam', False, 'For MRSA and Pseudomonas risk, which she lacks.'),
 ('Azithromycin alone', False, 'Monotherapy is for outpatients without comorbidities.'),
 ('Ceftriaxone alone', False, 'Needs atypical coverage.')],
('id03', 1): [
 ('At least 5 days and clinically stable', True, 'IDSA/ATS 2019.'),
 ('At least 7 days, as for HAP', False, '7 days is the HAP duration.'),
 ('At least 10 days for inpatients', False, 'Older practice; longer than needed.'),
 ('At least 3 days if afebrile', False, '3 days is the cystitis style course; CAP minimum is 5.')],
('id03', 2): [
 ('No; only for refractory shock per SSC', True, ''),
 ('Yes, dexamethasone for every inpatient', False, 'Not routine.'),
 ('Yes, hydrocortisone for every inpatient', False, 'Only refractory shock.'),
 ('Only for influenza pneumonia', False, 'Steroids are not routine for influenza pneumonia either.')],
('id04', 0): [
 ('Stop vancomycin (nares NPV above 95%)', True, 'IDSA/ATS.'),
 ('Continue vancomycin for 7 days anyway', False, 'No MRSA evidence.'),
 ('Switch vancomycin to linezolid', False, 'No MRSA coverage needed.'),
 ('Repeat the nares PCR in 48 hours', False, 'Not needed.')],
('id05', 0): [
 ('Piperacillin tazobactam 4.5 g q6h', True, ''),
 ('Cefepime 2 g q8h', True, ''),
 ('Levofloxacin 750 mg daily', True, ''),
 ('Ceftriaxone + azithromycin', False, 'A CAP regimen; no Pseudomonas coverage.'),
 ('Vancomycin + meropenem', False, 'For high risk HAP only.')],
('id05', 1): [
 ('Shock, ventilation, IV antibiotics in 90 days', True, 'Or high local resistance.'),
 ('Age over 65 or diabetes', False, 'Not HAP double coverage triggers.'),
 ('Any hospital stay longer than 48 hours', False, 'That defines HAP, not double coverage.'),
 ('Every patient with HAP', False, 'Only with risk factors.')],
('id05', 2): [
 ('7 days', True, 'IDSA/ATS 2016.'),
 ('5 days', False, 'The CAP minimum.'),
 ('14 days', False, 'Longer than needed.'),
 ('21 days', False, 'Far longer than needed.')],
('id06', 0): [
 ('Cefepime neurotoxicity from accumulation', True, 'FDA 2012: mostly kidney impairment without adjustment.'),
 ('Hospital delirium from the infection', False, 'Possible, but jerking with CrCl 25 on full dose points to cefepime.'),
 ('Hypoglycemia from poor oral intake', False, 'Check glucose, but this pattern fits cefepime.'),
 ('Serotonin syndrome', False, 'Cefepime is not serotonergic.')],
('id06', 1): [
 ('Renally adjust or change; EEG if seizures suspected', True, ''),
 ('Add haloperidol and continue the same dose', False, 'Treats the symptom, not the cause.'),
 ('Add levetiracetam and continue the same dose', False, 'Leaves the cause in place.'),
 ('Switch to cefazolin for broader coverage', False, 'Cefazolin is narrower, not broader.')],
('id07', 0): [
 ('Ceftriaxone 2 g IV daily', True, ''),
 ('A fluoroquinolone (none in the past year)', True, ''),
 ('Nitrofurantoin', False, 'No kidney or blood levels.'),
 ('Oral fosfomycin', False, 'Same reason.'),
 ('Amoxicillin alone', False, 'High E. coli resistance.')],
('id07', 1): [
 ('7 days (5 to 7 with a fluoroquinolone)', True, 'Including bacteremia (IDSA 2025).'),
 ('3 days, the same as for cystitis', False, 'Cystitis courses are short; pyelonephritis needs longer.'),
 ('10 to 14 days for every patient', False, 'Longer than needed.'),
 ('14 days because she is bacteremic', False, 'IDSA 2025 supports 7 days with bacteremia.')],
('id07', 2): [
 ('Oral step down by susceptibility', True, 'For example TMP SMX DS BID, levofloxacin, cephalexin 1 g TID.'),
 ('Keep IV for the whole 7 days', False, 'Oral step down is supported.'),
 ('Nitrofurantoin to finish the course', False, 'Not for pyelonephritis.'),
 ('Stop antibiotics once afebrile', False, 'Finish the course.')],
('id08', 0): [
 ('Asymptomatic bacteriuria: do not treat', True, 'IDSA 2019.'),
 ('UTI causing delirium: treat 7 days', False, 'Confusion alone is not a reason to treat.'),
 ('Cystitis: treat 3 days', False, 'No urinary symptoms.'),
 ('Pyelonephritis: treat 7 days', False, 'No fever or flank pain.')],
('id08', 1): [
 ('Pregnancy (4 to 7 days)', True, ''),
 ('Before urologic procedures with mucosal trauma', True, ''),
 ('Older adults with a urinary catheter', False, 'No screening or treatment.'),
 ('Diabetes', False, 'No screening or treatment.'),
 ('Before orthopedic joint surgery', False, 'Not recommended.')],
('id09', 0): [
 ('Cephalexin 500 mg QID for about 5 days', True, 'Strep coverage.'),
 ('TMP SMX DS BID for about 5 days', False, 'Weak strep coverage; for purulent infections.'),
 ('Doxycycline 100 mg BID for about 5 days', False, 'Purulent (MRSA) option.'),
 ('Clindamycin for 14 days', False, 'Longer than needed; resistance and C. diff risk.')],
('id09', 1): [
 ('Drain it, then TMP SMX DS or doxycycline', True, 'Over 2 cm.'),
 ('Antibiotics only; skip the drainage', False, 'Drainage is the key step.'),
 ('Cephalexin only, after drainage', False, 'Purulent infections need MRSA coverage.'),
 ('IV vancomycin for 7 days', False, 'Not needed for a simple abscess.')],
('id10', 0): [
 ('Vancomycin + ceftriaxone 2 g every 12 hours', True, ''),
 ('Vancomycin + ceftriaxone 2 g every 24 hours', False, 'Daily dosing is for pneumonia or pyelonephritis; meningitis is every 12 hours.'),
 ('Ceftriaxone 2 g every 12 hours alone', False, 'Misses resistant pneumococcus.'),
 ('Vancomycin + cefazolin 2 g every 8 hours', False, 'Cefazolin does not reach the CSF well.')],
('id10', 1): [
 ('10 to 20 minutes before or with dose 1', True, '0.15 mg/kg every 6 hours for 2 to 4 days; continue only if pneumococcal.'),
 ('6 hours after the first antibiotic dose', False, 'Not after antibiotics start.'),
 ('Only once CSF culture confirms pneumococcus', False, 'Start empirically, stop if not pneumococcal.'),
 ('Only if the patient is in septic shock', False, 'That is hydrocortisone in septic shock.')],
('id10', 2): [
 ('Ampicillin 2 g every 4 hours', True, 'Listeria.'),
 ('Ampicillin 2 g every 6 hours', False, 'The intraamniotic infection dose.'),
 ('Cefepime 2 g every 8 hours', False, 'Cephalosporins never cover Listeria.'),
 ('Acyclovir 10 mg/kg every 8 hours', False, 'For suspected HSV, not Listeria.')],
('id11', 0): [
 ('Switch to cefazolin or nafcillin/oxacillin', True, 'Better than vancomycin for MSSA.'),
 ('Continue vancomycin; it covers MSSA', False, 'Worse outcomes.'),
 ('Switch to ceftriaxone 2 g daily', False, 'Less reliable than cefazolin for MSSA bacteremia.'),
 ('Add rifampin to vancomycin', False, 'Not routine.')],
('id11', 1): [
 ('Repeat blood cultures', True, ''),
 ('ID consult and echocardiogram', True, ''),
 ('14 days or more of IV therapy if uncomplicated', True, 'From the first negative culture.'),
 ('7 days total, like gram negative bacteremia', False, '7 days applies to uncomplicated gram negative bacteremia.'),
 ('Oral step down on day 2', False, 'Not for S. aureus.')],
('id12', 0): [
 ('Change to a carbapenem', True, 'MERINO.'),
 ('Continue pip tazo because it tested susceptible', False, 'MERINO showed higher mortality.'),
 ('Change to ceftriaxone 2 g daily', False, 'Resistant.'),
 ('Change to cefepime 2 g every 8 hours', False, 'Not reliable for ESBL bacteremia.')],
('id13', 0): [
 ('Cefazolin shares no side chain with other US beta lactams', True, ''),
 ('About 10% cross reactivity with all cephalosporins', False, 'An outdated estimate.'),
 ('Cross reactivity follows the beta lactam ring', False, 'It follows the R1 side chain.'),
 ('Cefazolin shares a side chain with amoxicillin', False, 'Cephalexin and cefadroxil do; cefazolin does not.')],
('id13', 1): [
 ('Give cefazolin; it beats vancomycin for prophylaxis', True, '2022 practice parameter.'),
 ('Vancomycin for any penicillin allergy label', False, 'Worse outcomes.'),
 ('Clindamycin as the standard alternative', False, 'For confirmed severe beta lactam allergy.'),
 ('Skin test before any cephalosporin', False, 'Not needed for non anaphylactic history.')],
('id13', 2): [
 ('2 g (3 g if 120 kg+) within 60 min; redose every 4 h', True, ''),
 ('2 g within 120 minutes; redose every 6 hours', False, '120 minutes is the vancomycin and fluoroquinolone window.'),
 ('1 g within 60 minutes; redose every 8 hours', False, 'Underdosed.'),
 ('2 g after closure, then every 8 hours for 3 days', False, 'Prophylaxis must be on board at incision.')],
('id14', 0): [
 ('Duplicate anaerobic coverage', True, 'Pip tazo already covers anaerobes.'),
 ('Duplicate gram negative coverage', False, 'Metronidazole has no gram negative aerobic activity.'),
 ('Missing MRSA coverage', False, 'Not indicated without risk.'),
 ('Missing enterococcal coverage', False, 'Pip tazo covers E. faecalis.')],
('id15', 0): [
 ('Cultures back: can we narrow?', True, ''),
 ('Can we switch to oral?', True, ''),
 ('Is there a stop date matching guidelines?', True, ''),
 ('Can we add coverage just in case?', False, 'Opposite of stewardship.'),
 ('Can we extend to 14 days to be safe?', False, 'Shorter is supported.')],
('id16', 0): [
 ('Meningitis first doses and dexamethasone', True, ''),
 ('The MSSA switch to cefazolin', False, 'Second.'),
 ('The cephalexin discharge question', False, 'Last.'),
 ('Writing the stewardship note', False, 'After care.')],
('id16', 1): [
 ('Recommend cefazolin for the MSSA patient', True, ''),
 ('Answer the cephalexin discharge question', False, 'Last.'),
 ('Order a vancomycin trough for the MSSA patient', False, 'Vancomycin should be stopped.'),
 ('Repeat the meningitis patient\'s CT', False, 'Not a pharmacy task.')],
}

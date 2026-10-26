# Module 9 (Stroke) rewrites.
R = {
('st01', 0): [
 ('Not yet: BP must be below 185/110 first', True, 'AHA/ASA 2026.'),
 ('Not yet: BP must be below 180/105 first', False, '180/105 is the limit after thrombolysis, for 24 hours.'),
 ('Not yet: BP must be below 140/90 first', False, 'Too strict; delays treatment.'),
 ('Yes: BP limits apply only to alteplase', False, 'Same limit for tenecteplase.')],
('st01', 1): [
 ('Labetalol 10 to 20 mg IV over 1 to 2 min, may repeat', True, ''),
 ('Nicardipine 5 mg/h, up 2.5 mg/h every 5 to 15 min', True, 'Max 15 mg/h.'),
 ('Clevidipine 1 to 2 mg/h, titrate to max 21 mg/h', True, ''),
 ('Nifedipine 10 mg sublingual, may repeat once', False, 'Unpredictable, sudden drops; avoid.'),
 ('Hydralazine 20 mg IV every 20 min as first line', False, 'Not a listed first line agent; unpredictable.')],
('st01', 2): [
 ('Glucose below 50 can mimic a stroke', True, 'Correct it first; above 400 also mimics.'),
 ('Glucose above 140 forbids thrombolysis', False, 'Hyperglycemia is treated, not a contraindication.'),
 ('Glucose sets the thrombolytic dose', False, 'Dose is by weight.'),
 ('Glucose must be below 180 to treat', False, 'Not a gate.')],
('st02', 0): [
 ('0.25 mg/kg bolus, max 25 mg: 20.5 mg', True, 'Over 5 seconds.'),
 ('0.5 mg/kg bolus, max 50 mg: 41 mg', False, 'The STEMI (cardiac) dose.'),
 ('0.4 mg/kg bolus, max 40 mg: 32.8 mg', False, 'Studied in EXTEND IA TNK part 2; no benefit over 0.25.'),
 ('0.9 mg/kg, max 90 mg: 73.8 mg', False, 'The alteplase dose.')],
('st02', 1): [
 ('Either agent, within the 4.5 hour window', True, 'AHA/ASA 2026.'),
 ('Alteplase only; tenecteplase is off label', False, 'Guideline endorses either.'),
 ('Tenecteplase only after 3 hours', False, 'Either agent in 0 to 4.5 hours.'),
 ('Tenecteplase only with an LVO', False, 'Either agent for eligible patients.')],
('st02', 2): [
 ('Double check drug and dose; waste the excess', True, 'Tenecteplase and alteplase names look alike.'),
 ('Reconstitute with D5W and shake well', False, 'Use the supplied diluent; swirl gently.'),
 ('Draw up the full 50 mg vial to save time', False, 'Overdose risk; waste the excess.'),
 ('Give over 1 minute, followed by an infusion', False, 'That is alteplase; tenecteplase is one bolus.')],
('st03', 0): [
 ('63 mg total; 6.3 mg bolus; 56.7 mg over 60 min', True, '0.9 mg/kg, 10% bolus over 1 minute.'),
 ('90 mg total; 9 mg bolus; 81 mg over 60 min', False, '90 mg is the max, for 100 kg or more.'),
 ('63 mg total; 15 mg bolus; 48 mg over 60 min', False, 'A 15 mg bolus is the STEMI regimen.'),
 ('70 mg total; 7 mg bolus; 63 mg over 60 min', False, 'Uses 1 mg/kg.')],
('st03', 1): [
 ('Remove and waste it before hanging the bag', True, 'Prevents giving more than the calculated dose.'),
 ('Infuse the vial remainder after the dose', False, 'Overdose.'),
 ('Return the vial to the stroke box', False, 'Reconstituted; must be wasted.'),
 ('Save it for a repeat bolus at 24 hours', False, 'No repeat dosing.')],
('st04', 0): [
 ('Apixaban taken 3 hours ago', True, 'DOAC within 48 hours.'),
 ('Platelets 72,000', True, 'Below 100,000.'),
 ('INR 2.4 on warfarin', True, 'INR above 1.7.'),
 ('Mild, nondisabling symptoms', True, 'PRISMS, ARAMIS: no benefit.'),
 ('LKW 2 h, BP 170/90, disabling deficit', False, 'A candidate.'),
 ('Glucose 220 that is being treated', False, 'Not a contraindication.')],
('st04', 1): [
 ('Yes, with advanced imaging, up to about 9 h', True, 'DWI FLAIR or perfusion mismatch (2026 guideline).'),
 ('Yes, if it is less than 24 hours since bedtime', False, 'Needs imaging selection; 24 h is a thrombectomy window.'),
 ('No; unknown onset is always excluded', False, 'Imaging selected patients may be treated.'),
 ('Yes, if NIHSS is above 25', False, 'Severity does not define eligibility here.')],
('st05', 0): [
 ('Orolingual angioedema: more bradykinin', True, 'Plasmin raises bradykinin; ACE inhibitors block its breakdown.'),
 ('A histamine allergy to the alteplase', False, 'Mostly bradykinin, not histamine.'),
 ('An allergy to the saline diluent', False, 'Not plausible.'),
 ('Hemorrhage into the tongue', False, 'Swelling is angioedema.')],
('st05', 1): [
 ('Stop it; steroid, H1 and H2 blockers; epi if worse', True, 'Icatibant or C1 esterase inhibitor may be considered; protect the airway.'),
 ('Continue the infusion; give diphenhydramine', False, 'Stop the infusion.'),
 ('Stop it and give FFP and cryoprecipitate', False, 'For bleeding, not angioedema.'),
 ('Stop it and give tranexamic acid 1 g IV', False, 'For bleeding, not angioedema.')],
('st06', 0): [
 ('No antithrombotics for 24 h after thrombolysis', True, 'Usually until a repeat scan.'),
 ('Aspirin is fine; only hold enoxaparin', False, 'Both wait 24 hours.'),
 ('Enoxaparin is fine; only hold aspirin', False, 'Both wait 24 hours.'),
 ('Aspirin dose should be 81 mg, not 325', False, 'The timing is the problem.')],
('st06', 1): [
 ('Below 180/105', True, 'For 24 hours after thrombolysis.'),
 ('Below 185/110', False, 'The gate before thrombolysis.'),
 ('Below 140/90', False, 'Not the post thrombolysis goal.'),
 ('Below 220/120', False, 'The permissive goal without thrombolysis.')],
('st07', 0): [
 ('Aspirin + clopidogrel 21 days, then one agent', True, 'Clopidogrel 300 to 600 mg load, then 75 mg (CHANCE, POINT).'),
 ('Aspirin + clopidogrel for 12 months', False, '12 months is an ACS duration; more bleeding.'),
 ('Aspirin + clopidogrel for 90 days', False, 'POINT used 90 days; most benefit was early, bleeding later.'),
 ('Apixaban 5 mg BID for secondary prevention', False, 'No atrial fibrillation; antiplatelets are used.')],
('st07', 1): [
 ('High intensity statin', True, ''),
 ('Glucose 140 to 180 in hospital', True, ''),
 ('VTE prophylaxis once safe', True, ''),
 ('Routine seizure prophylaxis', False, 'Not recommended.'),
 ('Glucose 80 to 110 in hospital', False, 'Too tight.')],
('st08', 0): [
 ('4F-PCC per protocol (often 50 units/kg)', True, 'Andexanet withdrawn from the US in 2025.'),
 ('Andexanet alfa, low dose regimen', False, 'Withdrawn from the US market.'),
 ('Idarucizumab 5 g IV', False, 'Dabigatran only.'),
 ('Vitamin K 10 mg IV slowly', False, 'Warfarin only.')],
('st08', 1): [
 ('SBP about 140; avoid below 130', True, 'AHA/ASA ICH 2022.'),
 ('SBP below 185 mmHg', False, 'The ischemic stroke pre thrombolysis gate.'),
 ('SBP below 160 mmHg', False, 'Older, looser target.'),
 ('SBP below 110 mmHg', False, 'Too low; harm below 130.')],
('st08', 2): [
 ('No, unless she goes to neurosurgery', True, 'PATCH: harm with platelet transfusion.'),
 ('Yes, 1 unit for every aspirin user', False, 'PATCH showed harm.'),
 ('Yes, if platelets are below 150,000', False, 'Not the reason to transfuse.'),
 ('Desmopressin 0.4 mcg/kg is required', False, 'May be considered; not required.')],
('st09', 0): [
 ('4F-PCC 25 units/kg (2,250 units) + vitamin K 10 mg', True, 'INR 2 to below 4; Kcentra label.'),
 ('4F-PCC 35 units/kg (3,150 units) + vitamin K 10 mg', False, 'The INR 4 to 6 dose.'),
 ('4F-PCC 50 units/kg (4,500 units) + vitamin K 10 mg', False, 'The INR above 6 dose (max 5,000 units).'),
 ('FFP 2 units with vitamin K 10 mg IV', False, 'Slower, volume heavy; PCC preferred.')],
('st09', 1): [
 ('About 42 mg (1 mg per 100 units, last 2 to 3 h)', True, '4,200 units; max 50 mg per dose.'),
 ('About 14 mg (1 mg per 100 units, last hour)', False, 'Counts only one hour.'),
 ('About 84 mg (1 mg per 50 units, last 3 h)', False, 'Double; above the 50 mg max.'),
 ('A fixed 100 mg dose for all patients', False, 'Above the max; excess protamine is an anticoagulant.')],
('st10', 0): [
 ('60 mg every 4 h for 21 days (30 mg q2h if BP drops)', True, 'Nimodipine label.'),
 ('60 mg every 6 h for 14 days', False, 'Wrong interval and duration.'),
 ('30 mg every 8 h for 21 days', False, 'Too low.'),
 ('IV nimodipine infusion for 21 days', False, 'No IV product in the US.')],
('st10', 1): [
 ('Use an oral syringe that cannot connect to IV', True, 'Label it "for oral use only"; IV nimodipine deaths occurred.'),
 ('Use a luer lock syringe with a red cap', False, 'Luer lock fits IV lines.'),
 ('Use a standard syringe and flush the line', False, 'Same risk.'),
 ('Ask the nurse to give it slowly IV', False, 'Fatal.')],
}

# Module 3/4 balancing fixes and Module 5 (anticoagulation) rewrites.
R = {
('iv14', 1): [
 ('Central concentration; peripheral max about 10 mEq/h', True, '40 mEq/100 mL.'),
 ('It needs a 1.2 micron in line filter added', False, 'Filter choice is not the problem.'),
 ('KCl must be mixed in D5W rather than NS', False, 'Diluent is not the problem.'),
 ('Nothing; the label wording is cosmetic', False, 'Route mismatch is dangerous.')],
('po03', 1): [
 ('500 to 750 mg PO every 12 hours', True, 'About 70% absorbed.'),
 ('400 mg PO every 12 hours (1:1)', False, '1:1 is the levofloxacin rule, not ciprofloxacin.'),
 ('750 mg PO once daily', False, 'That is levofloxacin dosing.'),
 ('250 mg PO every 12 hours', False, 'Too low for serious infection.')],
('po03', 3): [
 ('IV is lower: about 50 to 75% of oral', True, 'Label relative bioavailability about 48 to 74%.'),
 ('IV equals oral, microgram for microgram', False, 'Overdoses with IV.'),
 ('IV is about double the oral dose', False, 'Reversed.'),
 ('IV is about 25% of the oral dose', False, 'Too low.')],
('po06', 0): [
 ('Feeds bind it; hold feeds 1 to 2 h around doses', True, 'Monitor levels closely.'),
 ('Feeds speed up phenytoin metabolism', False, 'Binding, not metabolism.'),
 ('Feeds have no effect on phenytoin', False, 'Well known interaction.'),
 ('Feeds raise phenytoin blood levels', False, 'They lower absorption.')],
('po06', 1): [
 ('Capsules 92% phenytoin (sodium); liquid 100% (acid)', True, ''),
 ('Capsules 100% (acid); liquid 92% (sodium)', False, 'Reversed.'),
 ('Both forms are phenytoin acid at 100%', False, 'Capsules are the sodium salt.'),
 ('Only IV phenytoin is the sodium salt', False, 'Extended capsules are too.')],
('po07', 1): [
 ('Serotonin syndrome (weak MAO inhibition)', True, ''),
 ('QT prolongation with sertraline', False, 'The key issue is serotonin.'),
 ('Linezolid lowers sertraline levels', False, 'Not the interaction.'),
 ('Bleeding from combined platelet effects', False, 'Not the classic warning.')],
('po07', 2): [
 ('Platelets and counts after about 2 weeks', True, 'Myelosuppression.'),
 ('INR weekly during the course', False, 'Warfarin monitoring.'),
 ('Serum potassium every day', False, 'Not a linezolid issue.'),
 ('TSH once a month', False, 'Not a linezolid issue.')],
('ac01', 0): [
 ('Any 2 of 3: age 80+, weight 60 kg or less, SCr 1.5+', True, 'Eliquis label, AF.'),
 ('CrCl 15 to 50 mL/min', False, 'That is the rivaroxaban and edoxaban AF reduction rule.'),
 ('CrCl 15 to 30 mL/min', False, 'That is the dabigatran AF reduction rule (75 mg BID).'),
 ('Age 75 or older alone', False, 'Age 75 counts in CHA2DS2-VASc, not apixaban dosing.')],
('ac01', 1): [
 ('One: age 82 only', True, '64 kg is above 60; SCr 1.2 is below 1.5.'),
 ('Two: age 82 and weight 64 kg', False, 'The weight criterion is 60 kg or less.'),
 ('Two: age 82 and SCr 1.2', False, 'The SCr criterion is 1.5 or higher.'),
 ('Three: age, weight and SCr all qualify', False, 'Only age qualifies.')],
('ac01', 2): [
 ('Less stroke protection, no proven bleeding benefit', True, 'Off label underdosing is a common error.'),
 ('Lower doses always mean fewer strokes', False, 'Underdosing raises stroke risk.'),
 ('It matters only for VTE, not AF', False, 'It matters most in AF.'),
 ('2.5 mg BID is the standard dose over age 80', False, 'Only with a second criterion.')],
('ac02', 0): [
 ('15 and 20 mg tablets must be taken with food', True, 'Fasting lowers absorption a lot.'),
 ('Rivaroxaban must be taken fasting', False, 'Reversed.'),
 ('Only the 10 mg tablet must be taken with food', False, '10 mg can be taken with or without food.'),
 ('Food matters only for dabigatran', False, 'Dabigatran can be taken with or without food.')],
('ac02', 1): [
 ('15 mg BID x 21 days, then 20 mg daily (with food)', True, ''),
 ('10 mg BID x 7 days, then 5 mg BID', False, 'That is apixaban.'),
 ('15 mg daily x 21 days, then 20 mg daily', False, 'The first phase is twice daily.'),
 ('10 mg daily from the start', False, '10 mg daily is extended prevention after 6 months.')],
('ac03', 0): [
 ('No: opening raises exposure about 75%', True, 'Dabigatran label.'),
 ('Yes: pellets may be sprinkled on applesauce', False, 'That applies to some other capsules, not dabigatran.'),
 ('Yes: mix pellets in 30 mL of water via NG', False, 'Not allowed.'),
 ('Yes, if the dose is lowered to 75 mg BID', False, 'Dose reduction is for CrCl 15 to 30, not for opening.')],
('ac03', 1): [
 ('Switch to a tube friendly agent after team review', True, 'For example crushed apixaban or rivaroxaban per label, or a heparin.'),
 ('Hold anticoagulation until the tube comes out', False, 'Leaves the patient unprotected.'),
 ('Give dabigatran capsules whole down the tube', False, 'Will not pass or will open.'),
 ('Change to warfarin with no bridging', False, 'Warfarin takes days; not the simple fix.')],
('ac04', 0): [
 ('In AF, avoid edoxaban when CrCl is above 95', True, 'Boxed warning: less effective.'),
 ('Reduce to 30 mg when CrCl is above 95', False, '30 mg is the reduction for CrCl 15 to 50.'),
 ('Avoid edoxaban when CrCl is below 15 only', False, 'The low end also matters, but this patient\'s issue is high CrCl.'),
 ('No limit: higher CrCl is always better', False, 'Boxed warning.')],
('ac05', 0): [
 ('DOACs are not recommended with mechanical valves', True, 'Warfarin is standard.'),
 ('Apixaban is fine at 5 mg BID with a mechanical valve', False, 'Not recommended.'),
 ('DOACs are fine if aspirin is added', False, 'Adding aspirin does not make it safe.'),
 ('Dabigatran is the only DOAC approved for valves', False, 'Dabigatran caused more clots and bleeding in mechanical valves.')],
('ac05', 1): [
 ('High risk (triple positive) antiphospholipid syndrome', True, 'More clots on DOACs.'),
 ('First DVT after knee surgery', False, 'DOACs are fine.'),
 ('Cancer associated VTE', False, 'DOACs (for example apixaban) or LMWH are used.'),
 ('Atrial fibrillation with CrCl 60', False, 'DOACs preferred.')],
('ac06', 0): [
 ('Apixaban 2.5 mg BID (or rivaroxaban 10 mg daily), review yearly', True, 'CHEST 2021.'),
 ('Stop at 6 months for all unprovoked VTE', False, 'High recurrence after stopping.'),
 ('Apixaban 10 mg BID long term', False, '10 mg BID is only for the first 7 days.'),
 ('Apixaban 5 mg BID for exactly 12 more months', False, 'No set stop date; reduced dose is suggested.')],
('ac06', 1): [
 ('VTE from a major transient risk such as surgery', True, 'Treat 3 months, then stop.'),
 ('Unprovoked VTE with low bleeding risk', False, 'The group that benefits.'),
 ('VTE with active cancer', False, 'Usually continued.'),
 ('Recurrent unprovoked VTE', False, 'Strong reason to continue.')],
('ac07', 0): [
 ('TMP SMX inhibits CYP2C9 and raises INR', True, ''),
 ('TMP SMX induces CYP3A4 and lowers INR', False, 'Wrong direction and enzyme.'),
 ('TMP SMX causes vitamin K deficiency only', False, 'Gut flora effects contribute, but CYP2C9 inhibition is the main mechanism.'),
 ('A lab error; repeat the INR first', False, 'Possible, but the interaction explains it.')],
('ac07', 1): [
 ('Hold warfarin and recheck; vitamin K usually not needed', True, 'Crowther 2009 (INR 4.5 to 10).'),
 ('Oral vitamin K 2.5 to 5 mg now', False, 'That is for INR above 10 without bleeding.'),
 ('Vitamin K 10 mg IV now', False, 'For major bleeding; causes warfarin resistance.'),
 ('4F-PCC 25 units/kg', False, 'For major bleeding or urgent surgery.')],
('ac07', 2): [
 ('Fluoroquinolones, metronidazole, fluconazole, amiodarone', True, 'Raise INR.'),
 ('Rifampin and carbamazepine', True, 'Lower INR.'),
 ('Amoxicillin as a strong CYP2C9 inhibitor', False, 'Not a strong inhibitor (small effects via gut flora).'),
 ('Pantoprazole as a strong inducer', False, 'Not a meaningful inducer.')],
('ac08', 0): [
 ('35 units/kg: 2,450 units', True, 'INR 4 to 6 band.'),
 ('25 units/kg: 1,750 units', False, 'INR 2 to below 4 band.'),
 ('50 units/kg: 3,500 units', False, 'INR above 6 band (also the common Xa inhibitor dose).'),
 ('35 units/kg capped at 2,500 units', False, '2,500 is the cap for the 25 units/kg band; the 35 band caps at 3,500.')],
('ac08', 1): [
 ('Vitamin K 10 mg IV by slow infusion', True, 'Prevents INR rebound.'),
 ('Vitamin K 2.5 mg orally', False, 'For INR above 10 without bleeding.'),
 ('Protamine 50 mg IV', False, 'Reverses heparin.'),
 ('Tranexamic acid 1 g IV', False, 'An adjunct in some bleeds, not the required partner.')],
('ac08', 2): [
 ('Known HIT (it contains heparin)', True, 'Kcentra label contraindication; DIC too.'),
 ('Penicillin allergy', False, 'Unrelated.'),
 ('Prior DVT more than a year ago', False, 'A clot risk to weigh, not a contraindication.'),
 ('Kidney failure', False, 'Not a contraindication.')],
('ac09', 0): [
 ('4F-PCC (often 50 units/kg or a fixed dose)', True, 'Andexanet withdrawn December 2025.'),
 ('Andexanet alfa high dose', False, 'Withdrawn from the US market.'),
 ('Vitamin K 10 mg IV', False, 'Warfarin only.'),
 ('Protamine 1 mg per 100 units', False, 'Heparin only.')],
('ac09', 1): [
 ('Idarucizumab 5 g IV (two 2.5 g vials)', True, ''),
 ('4F-PCC 50 units/kg first', False, 'Idarucizumab is the specific agent.'),
 ('Idarucizumab 2.5 g IV once', False, 'The dose is 5 g.'),
 ('Hemodialysis only', False, 'Can remove dabigatran, but idarucizumab is first.')],
('ac09', 2): [
 ('About 140; avoid going below 130', True, 'ICH 2022.'),
 ('Below 185/110', False, 'That is the gate before thrombolysis in ischemic stroke.'),
 ('Below 180/105', False, 'That is the post thrombolysis limit.'),
 ('About 110 to 120', False, 'Too low; may harm brain perfusion.')],
('ac10', 0): [
 ('80 units/kg bolus, then 18 units/kg/h', True, '7,200 units; 1,620 units/h.'),
 ('60 units/kg bolus (max 4,000), then 12 units/kg/h', False, 'That is the ACS regimen.'),
 ('5,000 units SC every 8 hours', False, 'Prophylaxis.'),
 ('70 units/kg bolus, then 15 units/kg/h', False, 'Not a standard nomogram.')],
('ac10', 1): [
 ('6 hours after the bolus and after each change', True, 'Steady state in about 6 hours.'),
 ('1 hour after starting', False, 'Too early.'),
 ('24 hours after starting', False, 'Too late to adjust safely.'),
 ('4 hours after the bolus, like enoxaparin anti Xa', False, '4 hours is the LMWH peak timing.')],
('ac10', 2): [
 ('Recent enoxaparin or DOAC doses on the MAR', True, ''),
 ('Baseline platelets and hemoglobin', True, ''),
 ('A baseline INR to set the heparin rate', False, 'INR does not set heparin dosing.'),
 ('A baseline troponin', False, 'Not needed for a PE nomogram.')],
('ac11', 0): [
 ('4Ts: fall over 50%, day 5 to 10, clot, other causes', True, ''),
 ('Platelets below 100,000', False, 'HIT is about the size of the fall.'),
 ('Platelets below 50,000', False, 'Most HIT counts stay above 20,000 to 50,000.'),
 ('Any drop of 10,000 from baseline', False, 'Too sensitive.')],
('ac11', 1): [
 ('Stop all heparin, including flushes', True, 'ASH 2018.'),
 ('Start argatroban 2 mcg/kg/min (0.5 if hepatic impairment)', True, ''),
 ('Switch to enoxaparin', False, 'Cross reacts.'),
 ('Transfuse platelets', False, 'Not routine; may worsen clotting.'),
 ('Start warfarin today', False, 'Venous limb gangrene risk.')],
('ac11', 2): [
 ('After platelets recover; overlap 5 days or more', True, 'Usually 150,000 or more.'),
 ('Today, together with argatroban', False, 'Too early.'),
 ('When platelets reach 100,000', False, 'Usually wait for about 150,000.'),
 ('After 48 hours of argatroban, regardless of count', False, 'Platelet recovery is the gate.')],
('ac12', 0): [
 ('1 mg/kg once daily (75 mg every 24 hours)', True, 'CrCl below 30.'),
 ('0.5 mg/kg every 12 hours', False, 'Same daily total, but not the label method.'),
 ('1.5 mg/kg once daily', False, 'The inpatient once daily option for normal kidneys.'),
 ('No change; enoxaparin is liver cleared', False, 'It is renally cleared.')],
('ac12', 1): [
 ('30 mg once daily', True, 'CrCl below 30.'),
 ('30 mg every 12 hours', False, 'Orthopedic or trauma prophylaxis with normal kidneys.'),
 ('40 mg once daily', False, 'Normal kidney prophylaxis.'),
 ('20 mg once daily', False, 'Not a label dose.')],
('ac12', 2): [
 ('Kidney disease, pregnancy, weight extremes; peak 4 h post dose', True, 'At steady state.'),
 ('Every patient, 6 hours after each dose', False, '6 hours is the UFH timing; not routine for all.'),
 ('Trough before every dose', False, 'Peaks are used.'),
 ('Never; anti Xa does not measure enoxaparin', False, 'Anti Xa is the test for LMWH.')],
('ac13', 0): [
 ('Tuesday (skip Wednesday, Thursday and Friday)', True, 'PAUSE high bleed risk.'),
 ('Wednesday (skip only Thursday and Friday)', False, 'That is the low bleed risk schedule.'),
 ('Thursday evening', False, 'Too close.'),
 ('Sunday (5 days off, like warfarin)', False, '5 days is the warfarin rule.')],
('ac13', 1): [
 ('No: DOACs are not bridged', True, 'PAUSE; CHEST 2022.'),
 ('Yes: enoxaparin 1 mg/kg every 12 hours', False, 'Bridging adds bleeding.'),
 ('Yes: heparin infusion until 4 hours before', False, 'Not for DOACs.'),
 ('Only if CHA2DS2-VASc is 4 or more', False, 'Not a DOAC rule.')],
('ac13', 2): [
 ('About 48 to 72 hours after surgery', True, 'High bleed risk.'),
 ('About 24 hours after surgery', False, 'Low bleed risk timing.'),
 ('2 hours after surgery', False, 'Too early.'),
 ('7 days after surgery', False, 'Too late.')],
('ac14', 0): [
 ('CHEST 2022: do not bridge in AF (BRIDGE)', True, 'No difference in clots; more bleeding (3.2% vs 1.3%).'),
 ('Bridge every patient with CHA2DS2-VASc 3 or more', False, 'Old practice.'),
 ('Bridge only with heparin, never enoxaparin', False, 'Not the guidance.'),
 ('Bridge for 24 hours before the procedure only', False, 'Not the guidance.')],
('ac14', 1): [
 ('Mechanical mitral valve or clot in the last 3 months', True, 'With cardiology or hematology.'),
 ('Anyone over 75 years old', False, 'Age alone does not decide.'),
 ('Anyone with CHA2DS2-VASc 3', False, 'This patient; not bridged.'),
 ('Nobody under any circumstances', False, 'Some very high risk patients are bridged.')],
('ac15', 0): [
 ('Three anticoagulants active at once', True, ''),
 ('Two, because SC heparin is just a flush', False, '5,000 units SC is prophylaxis.'),
 ('One, because orders replace each other automatically', False, 'They do not.'),
 ('Normal overlap during a transfer', False, 'Never normal.')],
('ac15', 1): [
 ('Start apixaban when the drip stops; stop SC heparin', True, 'Per labels.'),
 ('Overlap the drip and apixaban for 24 hours', False, 'Bleeding risk.'),
 ('Start apixaban 6 hours after the drip stops', False, 'Not needed; heparin wears off quickly.'),
 ('Give apixaban 10 mg BID loading on top', False, 'Loading applies only to new VTE treatment.')],
('ac16', 0): [
 ('The bleeding patient on the heparin drip', True, ''),
 ('The apixaban crushing question', False, 'Can wait.'),
 ('The INR of 3.4', False, 'Mildly high, stable.'),
 ('Whichever call came in first', False, 'Triage by harm.')],
('ac16', 1): [
 ('Hold the drip, call, check Hgb; protamine if serious', True, '1 mg per 100 units in the last 2 to 3 hours, max 50 mg.'),
 ('Lower the rate by 2 units/kg/h and recheck in 6 h', False, 'A nomogram step for high aPTT without bleeding.'),
 ('Give vitamin K 10 mg IV', False, 'Warfarin reversal.'),
 ('Give 4F-PCC 25 units/kg', False, 'Not for heparin.')],
('ac16', 2): [
 ('Yes: crushed in water, D5W or apple juice, or via NG', True, 'Eliquis label.'),
 ('No: apixaban must be swallowed whole', False, 'That is dabigatran.'),
 ('Only if dissolved in milk', False, 'Not a label option.'),
 ('Only the 2.5 mg tablet may be crushed', False, 'Both strengths.')],
}

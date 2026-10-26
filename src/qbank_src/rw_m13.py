# Module 12 balancing and Module 13 (Med Safety and Florida Law) rewrites.
R = {
('pi06', 0): [
 ('Ketamine 1 to 2 mg/kg (12 to 24 mg)', True, 'Preserves blood pressure.'),
 ('Propofol 3 mg/kg IV (36 mg total)', False, 'Drops BP in shock.'),
 ('Etomidate 3 mg/kg IV (36 mg total)', False, 'Ten times (usual 0.3 mg/kg); also debated in sepsis.'),
 ('Ketamine 10 mg/kg IV (120 mg total)', False, 'Ten times.')],
('pi07', 0): [
 ('Opioid and benzodiazepine withdrawal', True, 'Iatrogenic; expected after 5 or more days of infusions.'),
 ('A new infection; start antibiotics', False, 'Pattern fits withdrawal; check the WAT 1 score.'),
 ('Serotonin syndrome from fentanyl', False, 'Withdrawal pattern after stopping infusions.'),
 ('ICU delirium; give haloperidol', False, 'Treat withdrawal first.')],
('ms01', 0): [
 ('Insulin', True, ''),
 ('Heparin and other anticoagulants', True, ''),
 ('Concentrated KCl and potassium phosphate injection', True, ''),
 ('Tranexamic acid injection (added 2024)', True, 'Wrong route (intrathecal) errors.'),
 ('Oral amoxicillin suspension', False, 'Not high alert.'),
 ('Ondansetron injection', False, 'Not on the list.')],
('ms01', 1): [
 ('Standard concentrations, smart pumps, premixes', True, 'And removing concentrated electrolytes from units.'),
 ('Retraining staff after each error', False, 'Education alone is a weak fix (ISMP hierarchy).'),
 ('Warning stickers on high alert vials', False, 'Weak; people stop seeing them.'),
 ('A new policy that staff must sign', False, 'Rules and policies are weak fixes.')],
('ms02', 0): [
 ('Tall man lettering (hydrOXYzine, hydrALAZINE)', True, ''),
 ('Include the indication on orders', True, ''),
 ('Separate storage and barcode scanning', True, ''),
 ('Store them alphabetically side by side', False, 'Promotes picking errors.'),
 ('Use brand names only on orders', False, 'Brand names also look and sound alike (Celebrex vs Celexa).')],
('ms03', 0): [
 ('MSO4 reads as magnesium sulfate: write morphine', True, ''),
 ('Trailing zero: 2.0 can be read as 20', True, ''),
 ('"U" can read as 0 or 4; "QD" as QID', True, ''),
 ('"PRN" is on the Do Not Use list', False, 'PRN is acceptable.'),
 ('"q4h" must be written "every 4 hours"', False, 'Acceptable, though spelling out is safest.')],
('ms04', 0): [
 ('RA methotrexate is weekly; daily has killed', True, 'ISMP.'),
 ('15 mg is above the RA maximum of 7.5 mg', False, 'RA doses often reach 15 to 25 mg weekly.'),
 ('Methotrexate needs folinic acid daily', False, 'Folic acid is given; the frequency is the danger.'),
 ('Nothing; daily is fine for RA', False, 'Fatal errors.')],
('ms04', 1): [
 ('Confirm, then enter weekly with the day', True, 'Check with the patient and outpatient pharmacy.'),
 ('Verify as daily, as written at home', False, 'Fatal risk.'),
 ('Change to 2.5 mg daily to be safe', False, 'Still daily; confirm the real regimen.'),
 ('Hold it and discharge without it', False, 'Clarify; do not drop the therapy.')],
('ms05', 0): [
 ('14 National Performance Goals', True, 'Existing requirements reorganized (TJC, January 2026).'),
 ('Nothing; NPSGs continue unchanged', False, 'Replaced in January 2026.'),
 ('A new set of 20 NPSGs for hospitals', False, 'Not the change.'),
 ('CMS Conditions of Participation alone', False, 'TJC standards still apply.')],
('ms05', 1): [
 ('Labeling all medications on and off the sterile field', True, ''),
 ('Reducing harm from anticoagulants', True, ''),
 ('Order review, override review, standard concentrations', True, ''),
 ('Antimicrobial stewardship', True, ''),
 ('Hand hygiene compliance audits', False, 'Infection prevention, not medication management.'),
 ('Two patient identifiers before care', False, 'Patient identification goal.')],
('ms06', 0): [
 ('Fix it, then report the near miss', True, 'In St. Mary\'s reporting system.'),
 ('Fix it and say nothing; no harm', False, 'Near misses reveal system gaps.'),
 ('Report only if the dose reached the patient', False, 'Near misses are reported too.'),
 ('Tell the nurse to report it instead', False, 'Your verification; you report it.')],
('ms06', 1): [
 ('Console a slip; coach at risk; act on reckless', True, 'Just culture.'),
 ('Punish every error to deter others', False, 'Drives errors underground.'),
 ('Ignore all errors to protect morale', False, 'At risk and reckless behavior need action.'),
 ('Suspend after a second human slip', False, 'Slips are consoled and the system fixed.')],
('ms07', 0): [
 ('Possible diversion: report per policy now', True, 'To the pharmacy manager or diversion team; do not investigate alone or confront.'),
 ('Adjust the count and move on', False, 'Ignores diversion signals.'),
 ('Confront the nurse directly today', False, 'Follow policy; do not confront.'),
 ('Wait for a third discrepancy first', False, 'Report now.')],
('ms07', 1): [
 ('DEA in writing within 1 business day; Form 106', True, '21 CFR 1301.76.'),
 ('DEA Form 106 within 30 days only', False, 'Initial written notice is within 1 business day.'),
 ('DEA Form 41 within 1 business day', False, 'Form 41 is for destruction.'),
 ('Board of Pharmacy only, within 7 days', False, 'Federal law requires DEA notice.')],
('ms07', 2): [
 ('Witnessed waste, documented in real time', True, 'By a second licensed person.'),
 ('Waste later, when it is convenient', False, 'Diversion risk.'),
 ('Waste alone, then document the amount', False, 'Needs a witness.'),
 ('Waste in the sharps container unwitnessed', False, 'Needs a witness.')],
('ms08', 0): [
 ('Every 2 years; 30 hours per renewal', True, 'Florida Board of Pharmacy.'),
 ('Every year; 15 hours per renewal', False, 'Florida is biennial.'),
 ('Every 2 years; 24 hours per renewal', False, '24 extra hours apply to consultant pharmacists.'),
 ('Every 3 years; 45 hours per renewal', False, 'Not Florida.')],
('ms08', 1): [
 ('2 h medication errors, 2 h controlled substances', True, 'Board approved.'),
 ('5 h pain management and 2 h ethics', False, 'Not the Florida required topics.'),
 ('1 h HIV/AIDS and 2 h ethics', False, 'Not the current required pair.'),
 ('3 h immunization for every pharmacist', False, 'Only if certified to immunize.')],
('ms08', 2): [
 ('3 hours every 2 years if certified to immunize', True, ''),
 ('24 extra hours for consultant pharmacists', True, ''),
 ('A practical exam each renewal', False, 'Not required.'),
 ('An MPJE retake every 6 years', False, 'Not required.'),
 ('A new background check each renewal', False, 'Not a renewal requirement.')],
('ms09', 0): [
 ('Report to E-FORCSE by close of next business day', True, 'Florida PDMP.'),
 ('Report to E-FORCSE within 7 days', False, 'The older Florida deadline.'),
 ('Report to the DEA within 1 business day', False, 'DEA notice is for theft or loss.'),
 ('No reporting for hospital discharges', False, 'Outpatient dispensing is reported.')],
('ms09', 1): [
 ('Spot overlaps, many prescribers, high doses', True, 'Multiple pharmacies too.'),
 ('It is only for law enforcement use', False, 'A clinical safety tool.'),
 ('To confirm insurance coverage', False, 'Not its purpose.'),
 ('To check the prescriber\'s DEA renewal', False, 'Not its purpose.')],
('ms10', 0): [
 ('Each home drug: continue, change or stop', True, 'For example whether and when warfarin restarts.'),
 ('Duplicates: omeprazole and pantoprazole', True, ''),
 ('Follow up labs (INR) and who manages them', True, ''),
 ('Restart all home drugs as before', False, 'Aspirin and warfarin after a GI bleed need decisions.'),
 ('Nothing; discharge is the doctor\'s job', False, 'Reconciliation is a pharmacist role.')],
}

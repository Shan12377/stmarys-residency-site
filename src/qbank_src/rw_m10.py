# Module 9 balancing and Module 10 (Trauma) rewrites.
R = {
('st08', 1): [
 ('SBP about 140 mmHg', True, 'AHA/ASA ICH 2022; avoid below 130.'),
 ('SBP below 185 mmHg', False, 'The ischemic stroke pre thrombolysis gate.'),
 ('SBP below 160 mmHg', False, 'Older, looser target.'),
 ('SBP below 110 mmHg', False, 'Too low; harm below 130.')],
('st10', 0): [
 ('60 mg every 4 h for 21 days', True, '30 mg every 2 hours if BP drops (nimodipine label).'),
 ('60 mg every 6 h for 14 days', False, 'Wrong interval and duration.'),
 ('30 mg every 8 h for 21 days', False, 'Too low.'),
 ('IV infusion for 21 days', False, 'No IV product in the US.')],
('tr01', 0): [
 ('1 g IV over 10 min, then 1 g over 8 hours', True, 'CRASH-2.'),
 ('1 g IV over 10 min, then 1 g over 24 hours', False, 'The second gram runs over 8 hours.'),
 ('1 g IV over 10 min only, no infusion', False, 'Missing the 8 hour infusion (except some prehospital bolus protocols).'),
 ('10 mg/kg IV, then 1 mg/kg/h for 24 hours', False, 'A cardiac surgery style regimen.')],
('tr01', 1): [
 ('Within 3 hours of injury; later may harm', True, 'CRASH-2: benefit greatest early; harm after 3 hours.'),
 ('Within 3 hours of hospital arrival', False, 'The clock starts at injury, not arrival.'),
 ('Within 6 hours of injury', False, 'Bleeding deaths rose when started after 3 hours.'),
 ('Within 24 hours if still bleeding', False, 'Late use may harm.')],
('tr01', 2): [
 ('Injury time and any TXA given', True, 'Prevents a late start or a duplicate dose.'),
 ('The patient\'s home medication list', False, 'Useful later; TXA timing first.'),
 ('Whether a tourniquet was placed', False, 'A surgical team question.'),
 ('The blood alcohol level', False, 'Not a TXA decision.')],
('tr02', 0): [
 ('Citrate in stored blood binds calcium', True, ''),
 ('Kidney failure lowers calcium', False, 'Not acute in trauma.'),
 ('Low albumin from bleeding', False, 'Ionized calcium is already corrected for albumin.'),
 ('Magnesium excess from transfusion', False, 'Not the mechanism.')],
('tr02', 1): [
 ('CaCl 1 g IV (central) or gluconate 3 g IV', True, 'Guided by ionized calcium.'),
 ('Calcium gluconate 1 g IV once only', False, 'One third of the calcium in 1 g chloride; usually too little.'),
 ('Calcium chloride 1 g IM', False, 'Never IM; tissue necrosis.'),
 ('Wait until transfusion ends to treat', False, 'Low calcium worsens bleeding and shock now.')],
('tr02', 2): [
 ('Near 1:1:1 plasma, platelets, RBC', True, 'PROPPR.'),
 ('1:1:2 plasma, platelets, red cells', False, 'PROPPR arm with no mortality benefit at 24 h and 30 d.'),
 ('Red cells only until labs return', False, 'Causes coagulopathy.'),
 ('Crystalloid 2 L before any blood', False, 'Large crystalloid volumes worsen trauma outcomes.')],
('tr03', 0): [
 ('Ketamine 1 to 2 mg/kg (85 to 170 mg)', True, ''),
 ('Etomidate 0.3 mg/kg (about 25 mg)', True, ''),
 ('Propofol 2.5 mg/kg (about 210 mg)', False, 'Drops blood pressure; at most a much reduced dose.'),
 ('Midazolam 0.3 mg/kg (about 25 mg)', False, 'Slow onset and hypotension.'),
 ('Ketamine 10 mg/kg (850 mg)', False, 'Ten times the dose.')],
('tr03', 1): [
 ('Rocuronium 1 to 1.2 mg/kg; lasts 45 to 60 min', True, ''),
 ('Rocuronium 0.6 mg/kg; lasts 5 to 10 min', False, '0.6 mg/kg is the non RSI dose; it lasts about 30 to 40 minutes.'),
 ('Succinylcholine 1.5 mg/kg in a 3 day old crush', False, 'Hyperkalemia risk after 48 to 72 hours in crush and burns.'),
 ('Vecuronium 0.01 mg/kg; lasts 5 to 10 min', False, 'A priming dose; not an RSI dose.')],
('tr03', 2): [
 ('Analgesia and sedation, as BP allows', True, 'Rocuronium outlasts the induction drug: awake paralysis risk.'),
 ('Nothing until the patient moves', False, 'Paralysis hides awareness.'),
 ('A second rocuronium dose now', False, 'Paralysis without sedation.'),
 ('Haloperidol 5 mg IV for agitation', False, 'Not sedation for intubation.')],
('tr04', 0): [
 ('Identify the anticoagulant and last dose time', True, ''),
 ('Give vitamin K 10 mg IV to every patient', False, 'Only warfarin.'),
 ('Give protamine 50 mg IV empirically', False, 'Only heparins.'),
 ('Order an anti Xa level and wait', False, 'Do not delay reversal planning.')],
('tr04', 1): [
 ('4F-PCC per protocol', True, 'Often 50 units/kg or a fixed dose; andexanet withdrawn from the US in 2025.'),
 ('Protamine 1 mg per 100 units', False, 'Heparin only.'),
 ('Idarucizumab 5 g IV push', False, 'Dabigatran only.'),
 ('Vitamin K 10 mg IV slowly', False, 'Warfarin only.')],
('tr05', 0): [
 ('Mannitol 0.25 to 1 g/kg IV (20 to 80 g)', True, ''),
 ('3% saline 250 mL, or 23.4% 30 mL central only', True, ''),
 ('Dexamethasone 10 mg IV every 6 hours', False, 'CRASH: steroids increased death in TBI.'),
 ('23.4% saline 30 mL through a peripheral IV', False, 'Central line only.'),
 ('Mannitol 2 g/kg IV (160 g)', False, 'Above the usual range.')],
('tr05', 1): [
 ('For the first 7 days', True, 'Brain Trauma Foundation 4th edition: phenytoin; levetiracetam widely used.'),
 ('For 30 days after discharge', False, 'Prophylaxis does not prevent late seizures.'),
 ('For life after any severe TBI', False, 'Not supported.'),
 ('Not used in severe TBI', False, 'Recommended for early seizures.')],
('tr05', 2): [
 ('CRASH-3: helps mild to moderate TBI within 3 h', True, ''),
 ('CRASH-3: helps severe TBI at any time', False, 'No clear benefit in severe TBI.'),
 ('CRASH-3: helps all TBI within 8 hours', False, 'Benefit within 3 hours.'),
 ('CRASH-3: TXA raised seizures and deaths', False, 'No increase in vascular events or seizures.')],
('tr06', 0): [
 ('Cefazolin 3 g IV within 1 hour', True, '120 kg or more.'),
 ('Cefazolin 2 g IV within 1 hour', False, 'The dose under 120 kg.'),
 ('Cefazolin 1 g IV within 1 hour', False, 'Underdosed.'),
 ('Vancomycin 1 g IV within 2 hours', False, 'Not first line; weight based if used.')],
('tr06', 1): [
 ('Add gram negative coverage per protocol', True, 'For example ceftriaxone or gentamicin.'),
 ('Add penicillin for soil contamination', True, 'Clostridium; per protocol.'),
 ('Add vancomycin for every type III', False, 'Only with MRSA risk.'),
 ('Add metronidazole for every type III', False, 'Not routine.'),
 ('Add fluconazole for soil exposure', False, 'Not routine.')],
('tr07', 0): [
 ('Tdap (or Td) now', True, ''),
 ('Tetanus immune globulin 250 units IM', True, 'Unknown history and a dirty wound.'),
 ('Tetanus immune globulin 3,000 units IM', False, 'A treatment dose for clinical tetanus.'),
 ('Tetanus immune globulin in the same syringe as Tdap', False, 'Separate syringes and sites.'),
 ('Nothing if he feels fine', False, 'Tetanus has a long incubation.')],
('tr07', 1): [
 ('No; booster only if over 10 years for clean wounds', True, 'CDC.'),
 ('Yes; booster if over 5 years for any wound', False, '5 years applies to dirty wounds.'),
 ('Yes; plus tetanus immune globulin', False, 'TIG only for unknown or fewer than 3 doses with dirty wounds.'),
 ('Yes; every ER visit needs a booster', False, 'Not needed.')],
('tr08', 0): [
 ('Enoxaparin per protocol once bleeding allows', True, 'Often 30 mg q12h or 40 mg daily, adjusted by weight and anti Xa.'),
 ('Warfarin to INR 2 to 3, starting today', False, 'Slow, hard to reverse; not trauma prophylaxis.'),
 ('Hold all prophylaxis for 7 days', False, 'Delay raises VTE.'),
 ('Heparin 5,000 units every 24 hours', False, 'Subtherapeutic interval.')],
('tr08', 1): [
 ('Multimodal: APAP, blocks, ketamine', True, 'NSAIDs if safe; opioids as needed.'),
 ('Opioids alone, around the clock', False, 'More respiratory compromise.'),
 ('Scheduled NSAIDs alone, no opioids', False, 'Bleeding risk; often not enough.'),
 ('Gabapentin alone as first line', False, 'An adjunct only.')],
('tr09', 0): [
 ('4 x 80 x 40 = 12,800 mL LR in 24 h', True, 'Parkland; ABA now suggests starting at 2 to 4 mL/kg/%TBSA.'),
 ('2 x 80 x 40 = 6,400 mL LR in 24 h', False, 'The lower ABA start; Parkland uses 4.'),
 ('4 x 80 x 40 = 1,280 mL LR in 24 h', False, 'Decimal error.'),
 ('4 x 80 x 40 = 12,800 mL NS in 8 h', False, 'Wrong fluid and time.')],
('tr09', 1): [
 ('6,400 mL over the next 6 hours', True, 'Half by hour 8 after the burn; 2 hours have passed.'),
 ('6,400 mL over 8 hours from arrival', False, 'Clock starts at the burn.'),
 ('3,200 mL over the next 8 hours', False, 'Half of the total goes in the first 8 hours from the burn.'),
 ('12,800 mL over the next 8 hours', False, 'Only half.')],
('tr10', 0): [
 ('GSW: TXA, RSI drugs, calcium', True, ''),
 ('The late cefazolin first', False, 'Second.'),
 ('The CIWA question first', False, 'Last.'),
 ('Whichever call came in first', False, 'Triage by harm.')],
('tr10', 1): [
 ('Get the late cefazolin given', True, ''),
 ('Answer the CIWA question', False, 'Last.'),
 ('Write the trauma code note', False, 'After care.'),
 ('Restock the trauma bay', False, 'Later.')],
('tr10', 2): [
 ('Thiamine', True, 'Prevents Wernicke encephalopathy.'),
 ('Folic acid', False, 'Given, but not the step before glucose.'),
 ('Magnesium', False, 'Often replaced, but thiamine first.'),
 ('Phenobarbital', False, 'Treats withdrawal, not glucose timing.')],
}

# Module 11 (NICU) rewrites.
R = {
('nc01', 0): [
 ('32 weeks (GA 30 + 2 weeks PNA)', True, 'PMA = GA + PNA.'),
 ('30 weeks (GA alone at birth)', False, 'GA stays fixed; PMA moves forward.'),
 ('2 weeks (postnatal age only)', False, 'PNA is chronologic age, not PMA.'),
 ('34 weeks (GA + 4 weeks PNA)', False, '14 days is 2 weeks, not 4.')],
('nc01', 1): [
 ('Neofax or Lexicomp Pediatric, per unit charts', True, 'Whichever St. Mary\'s uses.'),
 ('Adult Lexicomp, scaled down by weight', False, 'Neonatal kinetics differ (kidneys, body water).'),
 ('Pediatric doses for a 1 year old by weight', False, 'Infant intervals do not fit preterm neonates.'),
 ('Harriet Lane only, without unit charts', False, 'Use the unit\'s chosen reference and charts.')],
('nc01', 2): [
 ('A decimal slip in a tiny weight is 10 fold', True, 'And weight changes in the first week.'),
 ('Neonatal weights rarely change', False, 'They drop the first week, then rise.'),
 ('Doses round to whole mL anyway', False, 'Small volumes are measured precisely.'),
 ('Weight only matters for fluids', False, 'Every dose is weight based.')],
('nc02', 0): [
 ('0.42 mg/kg: about 4 to 8x the usual range', True, 'And exactly 10x 0.05 mg: a classic decimal slip.'),
 ('0.042 mg/kg: within the usual range', False, 'Decimal error in the check itself.'),
 ('0.6 mg/kg: about 6 to 12x the usual range', False, 'Multiplied by weight instead of dividing.'),
 ('0.1 mg/kg: the top of the usual range', False, 'Wrong math; 0.5 / 1.2 = 0.42.')],
('nc02', 1): [
 ('Always a leading zero (0.05 mg); never trailing (5.0)', True, 'ISMP.'),
 ('Check mg/kg/dose vs mg/kg/day on every order', True, ''),
 ('Use a trailing zero to show precision (5.0 mg)', False, '5.0 can be misread as 50.'),
 ('Round all doses to whole numbers', False, 'Neonatal doses are fractions of a mg.'),
 ('Write "u" for units to save space', False, '"U" is misread as 0 or 4.')],
('nc03', 0): [
 ('Effective ventilation', True, 'NRP: most neonatal arrests are respiratory.'),
 ('Epinephrine before ventilation', False, 'Ventilation comes first.'),
 ('Sodium bicarbonate 2 mEq/kg', False, 'Not routine in NRP.'),
 ('Atropine 0.02 mg/kg', False, 'Not an NRP drug.')],
('nc03', 1): [
 ('0.02 mg/kg IV: 0.06 mg (0.6 mL of 0.1 mg/mL)', True, 'Range 0.01 to 0.03; every 3 to 5 minutes (NRP).'),
 ('0.1 mg/kg IV: 0.3 mg (3 mL of 0.1 mg/mL)', False, '0.1 mg/kg is the endotracheal dose; IV is 0.01 to 0.03.'),
 ('0.01 mg/kg IV: 0.03 mg (0.03 mL of 1 mg/mL)', False, 'Right range but wrong concentration; use 0.1 mg/mL.'),
 ('1 mg IV: 10 mL of 0.1 mg/mL', False, 'The adult arrest dose.')],
('nc03', 2): [
 ('NS 10 mL/kg (30 mL) over 5 to 10 min', True, 'NRP.'),
 ('NS 20 mL/kg (60 mL) IV push', False, 'The pediatric shock bolus, not NRP.'),
 ('D10W 2 mL/kg (6 mL) bolus', False, 'For hypoglycemia, not volume.'),
 ('Albumin 25% 10 mL/kg', False, 'Not an NRP volume choice.')],
('nc04', 0): [
 ('Vitamin K 0.5 to 1 mg IM once', True, ''),
 ('Erythromycin 0.5% eye ointment, both eyes', True, ''),
 ('Hep B vaccine + HBIG within 12 hours', True, 'HBsAg positive mother (CDC).'),
 ('Hep B vaccine alone, HBIG at 1 month', False, 'HBIG within 12 hours.'),
 ('Vitamin K 0.5 to 1 mg by mouth', False, 'IM is the standard.')],
('nc05', 0): [
 ('Ampicillin + gentamicin', True, ''),
 ('Ceftriaxone + gentamicin', False, 'No Listeria coverage; ceftriaxone risks in neonates.'),
 ('Vancomycin + gentamicin', False, 'Not the empiric early onset sepsis regimen; no MRSA risk here.'),
 ('Ampicillin + azithromycin', False, 'Misses gram negatives.')],
('nc05', 1): [
 ('Cephalosporins never cover Listeria', True, ''),
 ('Ampicillin covers E. coli more reliably', False, 'E. coli is often ampicillin resistant; that is why gentamicin is added.'),
 ('Cephalosporins do not cover GBS', False, 'They do.'),
 ('Ampicillin penetrates CSF better', False, 'Not the reason.')],
('nc05', 2): [
 ('By GA/PMA and PNA chart (term: ~4 mg/kg q24h)', True, 'Preterm often every 36 to 48 hours.'),
 ('Hartford 7 mg/kg every 24 hours', False, 'The adult extended interval nomogram.'),
 ('2.5 mg/kg every 8 hours for all', False, 'Older traditional dosing; not chart based.'),
 ('4 mg/kg every 12 hours for all', False, 'Too frequent for immature kidneys.')],
('nc06', 0): [
 ('No ceftriaxone with IV calcium in neonates', True, 'Fatal precipitates.'),
 ('Ceftriaxone displaces bilirubin from albumin', True, 'Kernicterus risk.'),
 ('Ceftriaxone needs a gentamicin partner here', False, 'Not the problem.'),
 ('Ceftriaxone must be given IM only', False, 'Not the problem.'),
 ('Nothing; it is fine at 10 days old', False, 'Both problems apply.')],
('nc06', 1): [
 ('Cefepime or ceftazidime with ampicillin', True, 'Cefotaxime is no longer marketed in the US.'),
 ('Cefotaxime with ampicillin', False, 'No longer available in the US.'),
 ('Ceftriaxone with a separate line', False, 'Still contraindicated with any IV calcium in neonates.'),
 ('Cefazolin with ampicillin', False, 'Poor CSF penetration.')],
('nc07', 0): [
 ('Yes: 20 mg/kg load, 5 mg/kg daily (citrate)', True, 'Maintenance 5 to 10 mg/kg/day.'),
 ('No: load should be 10 mg/kg citrate', False, '10 mg/kg is a base load (= 20 citrate).'),
 ('No: maintenance should be 20 mg/kg daily', False, 'That is the load.'),
 ('No: maintenance should be every 8 hours', False, 'Long half life; once daily.')],
('nc07', 1): [
 ('Citrate 2 mg = base 1 mg; base order doubles it', True, ''),
 ('Citrate 1 mg = base 2 mg; base order halves it', False, 'Reversed.'),
 ('Citrate and base are equal by weight', False, 'Twofold difference.'),
 ('Base is only an oral form; same dose', False, 'Salt vs base, not route.')],
('nc08', 0): [
 ('Look alike vials (10 vs 10,000 units/mL)', True, 'Infant deaths have occurred.'),
 ('Heparin flushes bind calcium in TPN', False, 'Not the risk.'),
 ('Heparin 10 units/mL needs dilution', False, 'Already the flush strength.'),
 ('Heparin should never be used in NICU', False, 'Low dose flushes are used.')],
('nc08', 1): [
 ('Concentration, preservative free, volume', True, 'Count flush volume in total fluids.'),
 ('Only the drug name and the expiration', False, 'Concentration is the killer.'),
 ('Only the lot number', False, 'Not enough.'),
 ('Only that the color of the cap matches', False, 'Caps are not reliable.')],
('nc09', 0): [
 ('D10W 2 mL/kg (6.4 mL, 200 mg/kg), then infusion', True, ''),
 ('D25W 2 mL/kg (6.4 mL), then infusion', False, 'Too concentrated for neonates.'),
 ('D50W 1 mL/kg (3.2 mL) IV push', False, 'Adult concentration; injures veins and causes rebound.'),
 ('D10W 20 mL/kg (64 mL) as a bolus', False, 'Ten times; that is a fluid bolus volume.')],
('nc10', 0): [
 ('Use the solubility curve; phosphate early, calcium late', True, 'Cysteine lowers pH and helps.'),
 ('Add calcium and phosphate first, together', False, 'Classic precipitate.'),
 ('Raise the pH with bicarbonate', False, 'Higher pH promotes precipitate.'),
 ('Switch to calcium chloride for solubility', False, 'Chloride is less soluble with phosphate.')],
('nc10', 1): [
 ('Every neonatal TPN gets an independent double check', True, ''),
 ('One pharmacist, if experienced', False, 'High alert; independent check required.'),
 ('Only the compounding technician', False, 'Needs pharmacist verification.'),
 ('Only if the TPN has a dose change', False, 'Every bag.')],
}

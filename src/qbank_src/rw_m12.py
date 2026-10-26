# Module 11 balancing and Module 12 (PICU) rewrites.
R = {
('nc01', 2): [
 ('A decimal slip is a 10 fold error', True, 'Tiny weights; weight also changes in the first week.'),
 ('Neonatal weights rarely change early', False, 'They drop the first week, then rise.'),
 ('Doses get rounded to whole mL anyway', False, 'Small volumes are measured precisely.'),
 ('Weight only matters for fluid orders', False, 'Every dose is weight based.')],
('nc03', 2): [
 ('NS 10 mL/kg (30 mL) over 5 to 10 min', True, 'NRP.'),
 ('NS 20 mL/kg (60 mL) as rapid IV push', False, 'The pediatric shock bolus, not NRP.'),
 ('D10W 2 mL/kg (6 mL) as a bolus', False, 'For hypoglycemia, not volume.'),
 ('Albumin 25% 10 mL/kg over 1 hour', False, 'Not an NRP volume choice.')],
('nc05', 2): [
 ('By GA/PMA and PNA on the unit chart', True, 'A term neonate is often about 4 mg/kg every 24 hours; preterm every 36 to 48 hours.'),
 ('Hartford nomogram, 7 mg/kg every 24 h', False, 'The adult extended interval nomogram.'),
 ('2.5 mg/kg every 8 h for every neonate', False, 'Older traditional dosing; not chart based.'),
 ('4 mg/kg every 12 h for every neonate', False, 'Too frequent for immature kidneys.')],
('nc09', 0): [
 ('D10W 2 mL/kg (6.4 mL), then infusion', True, '200 mg/kg of dextrose.'),
 ('D25W 2 mL/kg (6.4 mL), then infusion', False, 'Too concentrated for neonates.'),
 ('D50W 1 mL/kg (3.2 mL) by IV push', False, 'Adult concentration; injures veins and causes rebound.'),
 ('D10W 20 mL/kg (64 mL) as one bolus', False, 'Ten times; that is a fluid bolus volume.')],
('nc10', 0): [
 ('Solubility curve; phosphate early, calcium last', True, 'Cysteine lowers pH and helps.'),
 ('Add calcium and phosphate first, together', False, 'Classic precipitate.'),
 ('Raise the pH by adding bicarbonate', False, 'Higher pH promotes precipitate.'),
 ('Switch to calcium chloride for solubility', False, 'Chloride is less soluble with phosphate.')],
('nc10', 1): [
 ('An independent double check, every bag', True, ''),
 ('One pharmacist, if experienced', False, 'High alert; independent check required.'),
 ('Only the compounding technician', False, 'Needs pharmacist verification.'),
 ('Only when the TPN has a dose change', False, 'Every bag.')],
('pi01', 0): [
 ('Never above the adult dose: cap 1,000 mg', True, 'And 4 g per day.'),
 ('Fine: 15 mg/kg applies at any weight', False, 'Weight based doses are capped at the adult dose.'),
 ('Use 10 mg/kg instead: 820 mg', False, 'Not the fix; use the adult cap.'),
 ('Cap at 650 mg, the pediatric maximum', False, '650 mg is a common adult tablet dose, not the cap.')],
('pi01', 1): [
 ('Measured weight in kg; actual vs ideal per drug', True, ''),
 ('Standard concentration and a measurable volume', True, ''),
 ('mg/kg/dose vs mg/kg/day', True, ''),
 ('Weight in pounds as reported by the parent', False, 'Always measured kg.'),
 ('Age in years alone to pick the dose', False, 'Weight based.')],
('pi02', 0): [
 ('0.01 mg/kg = 0.2 mg = 2 mL of 0.1 mg/mL', True, 'Every 3 to 5 minutes, max 1 mg (PALS).'),
 ('0.1 mg/kg = 2 mg = 2 mL of 1 mg/mL', False, 'The endotracheal dose; IV/IO is 0.01 mg/kg.'),
 ('0.01 mg/kg = 0.2 mg = 2 mL of 1 mg/mL', False, 'Right dose but 10x volume with the 1 mg/mL product.'),
 ('1 mg = 10 mL of 0.1 mg/mL', False, 'The adult dose.')],
('pi02', 1): [
 ('5 mg/kg = 100 mg, repeat to 15 mg/kg', True, 'PALS.'),
 ('300 mg IV push, then 150 mg', False, 'The adult dose.'),
 ('1 mg/kg = 20 mg, repeat to 3 mg/kg', False, 'That is lidocaine dosing.'),
 ('15 mg/kg = 300 mg as a single dose', False, '15 mg/kg is the total, not one dose.')],
('pi03', 0): [
 ('0.1 mg/kg = 1.5 mg (max 6), then 0.2 mg/kg', True, 'Rapid push with flush; second dose max 12 mg.'),
 ('6 mg rapid push, then 12 mg', False, 'The adult dose.'),
 ('0.2 mg/kg = 3 mg first, then 0.4 mg/kg', False, 'Starts with the second dose.'),
 ('0.01 mg/kg = 0.15 mg, then 0.02 mg/kg', False, 'Ten times too low.')],
('pi03', 1): [
 ('0.02 mg/kg = 0.2 mg IV (max single 0.5 mg)', True, 'PALS.'),
 ('1 mg IV, repeat to 3 mg', False, 'The adult dose.'),
 ('0.2 mg/kg = 2 mg IV (max single 3 mg)', False, 'Ten times.'),
 ('0.01 mg/kg = 0.1 mg IV (max single 1 mg)', False, 'Confused with the epinephrine dose.')],
('pi04', 0): [
 ('Midazolam IM 5 mg (13 to 40 kg), once', True, 'RAMPART; 10 mg above 40 kg.'),
 ('Midazolam IM 10 mg (above 13 kg), once', False, '10 mg is for above 40 kg.'),
 ('Lorazepam IM 4 mg, once', False, 'Slow, erratic IM absorption.'),
 ('Diazepam IM 10 mg, once', False, 'Erratic IM absorption; rectal or IV used instead.')],
('pi04', 1): [
 ('0.1 mg/kg = 2.5 mg IV (max 4 mg), repeat once', True, ''),
 ('4 mg IV, because that is the maximum dose', False, 'The cap, not the dose; 0.1 mg/kg here.'),
 ('0.05 mg/kg = 1.25 mg IV, repeat every 5 min', False, 'Underdosed; limited repeats.'),
 ('0.2 mg/kg = 5 mg IV, max 8 mg', False, 'Above the max.')],
('pi04', 2): [
 ('Levetiracetam 60 mg/kg (1,500 mg, max 4,500)', True, ''),
 ('Fosphenytoin 20 mg PE/kg (500 mg PE, max 1,500)', True, ''),
 ('Valproate 40 mg/kg (1,000 mg, max 3,000)', True, 'Avoid in mitochondrial or liver disease.'),
 ('A third dose of benzodiazepine', False, 'Move to second line after two doses.'),
 ('Levetiracetam 20 mg/kg (500 mg)', False, 'Underdosed for status (ESETT used 60).')],
('pi05', 0): [
 ('0.05 to 0.1 units/kg/h, no bolus, after hour 1', True, '1.5 to 3 units/h; start after the first hour of fluids (ISPAD).'),
 ('0.1 units/kg bolus, then 0.1 units/kg/h', False, 'Boluses raise cerebral edema risk in children.'),
 ('0.14 units/kg/h, no bolus, start at once', False, 'An adult no bolus rate; start after initial fluids.'),
 ('1 unit/kg/h IV, no bolus, after hour 1', False, 'Ten times.')],
('pi05', 1): [
 ('Cerebral edema: mannitol or 3% saline ready', True, 'Mannitol 0.5 to 1 g/kg or 3% 2.5 to 5 mL/kg.'),
 ('Hypoglycemia: D50 at the bedside', False, 'Glucose is watched, but cerebral edema is the killer.'),
 ('Hyperkalemia: calcium at the bedside', False, 'Potassium falls with insulin.'),
 ('Anaphylaxis to insulin', False, 'Rare.')],
('pi05', 2): [
 ('Adult: K 3.5+; child: per protocol (often 3.3)', True, 'Follow St. Mary\'s pediatric protocol.'),
 ('They are identical: 3.5 in both', False, 'Pediatric protocols differ.'),
 ('Children: start insulin at any potassium', False, 'Low K must be replaced first.'),
 ('Adults: K 3.3+; child: K 4.0+', False, 'Not the cutoffs.')],
('pi06', 0): [
 ('Ketamine 1 to 2 mg/kg (12 to 24 mg)', True, ''),
 ('Propofol 3 mg/kg (36 mg)', False, 'Drops BP in shock.'),
 ('Etomidate 3 mg/kg (36 mg)', False, 'Ten times; and debated in sepsis.'),
 ('Ketamine 10 mg/kg (120 mg)', False, 'Ten times.')],
('pi06', 1): [
 ('Rocuronium 1 to 1.2 mg/kg (12 to 14 mg)', True, ''),
 ('Succinylcholine with suspected dystrophy', False, 'Hyperkalemic arrest risk.'),
 ('Rocuronium 0.1 mg/kg (1.2 mg)', False, 'Ten times too low.'),
 ('Vecuronium 0.01 mg/kg (0.12 mg)', False, 'A priming dose only.')],
('pi07', 0): [
 ('Iatrogenic opioid and benzodiazepine withdrawal', True, 'Expected after 5 or more days of infusions.'),
 ('New infection only; start antibiotics', False, 'Pattern fits withdrawal; check WAT 1 score.'),
 ('Serotonin syndrome from fentanyl', False, 'Withdrawal pattern after stopping infusions.'),
 ('Delirium; give haloperidol', False, 'Treat withdrawal first.')],
('pi07', 1): [
 ('Wean plan (methadone, lorazepam), taper by scores', True, 'WAT 1 guided.'),
 ('Stop everything at once', False, 'Causes this.'),
 ('Restart the fentanyl infusion at full rate', False, 'Not a plan.'),
 ('Clonidine alone, no taper', False, 'An adjunct only.')],
('pi08', 0): [
 ('60 mL/h: 40 for first 10 kg + 20 for next 10', True, '4/2/1 rule.'),
 ('80 mL/h: 4 mL/kg/h for all 20 kg', False, '4 mL/kg/h applies to the first 10 kg only.'),
 ('50 mL/h: 40 for first 10 kg + 10 for next 10', False, '2 mL/kg/h for kg 11 to 20.'),
 ('20 mL/h: 1 mL/kg/h for all 20 kg', False, '1 mL/kg/h applies beyond 20 kg.')],
('pi08', 1): [
 ('Isotonic fluid with potassium and dextrose', True, 'AAP 2018: reduces hyponatremia.'),
 ('Hypotonic 0.2% saline with dextrose', False, 'Hyponatremia risk.'),
 ('Hypotonic 0.45% saline for all ages', False, 'AAP 2018 recommends isotonic.'),
 ('D5W alone with no sodium', False, 'Severe hyponatremia.')],
('pi08', 2): [
 ('APAP 300 mg q6h; ibuprofen 200 mg q6 to 8h', True, '15 mg/kg and 10 mg/kg.'),
 ('APAP 200 mg q6h; ibuprofen 300 mg q6 to 8h', False, 'Doses swapped.'),
 ('APAP 600 mg q6h; ibuprofen 400 mg q6 to 8h', False, 'Double.'),
 ('APAP 1,000 mg q6h; ibuprofen 600 mg q6h', False, 'Adult doses.')],
('pi09', 0): [
 ('Octreotide', True, 'Blocks insulin release.'),
 ('Glucagon', False, 'Raises glucose briefly; can provoke more insulin release.'),
 ('Naloxone', False, 'Opioids.'),
 ('Flumazenil', False, 'Benzodiazepines.')],
('pi09', 1): [
 ('Poison Control: 1 800 222 1222', True, ''),
 ('The drug manufacturer hotline', False, 'Poison Control first.'),
 ('FDA MedWatch', False, 'For reporting, not treatment.'),
 ('ISMP error reporting', False, 'Not a treatment line.')],
}

# Module 7 length balancing.
R = {
('cc02', 0): [
 ('Phentolamine 5 to 10 mg, infiltrated locally', True, 'Diluted in 10 to 15 mL NS, as soon as possible (norepinephrine label).'),
 ('Hyaluronidase 150 units, infiltrated locally', False, 'For non vasopressor extravasation such as hyperosmolar fluids.'),
 ('Phentolamine 5 to 10 mg given IV push', False, 'Given locally, not systemically.'),
 ('Dexrazoxane 1,000 mg/m2 given IV', False, 'For anthracycline extravasation.')],
('cc04', 2): [
 ('Triglycerides, CK and lipase', True, 'And count lipid calories (1.1 kcal/mL) in nutrition.'),
 ('Serum sodium and osmolality', False, 'Not a propofol issue.'),
 ('TSH and free T4 weekly', False, 'Not a propofol issue.'),
 ('Serum propofol drug levels', False, 'Not available or useful clinically.')],
('cc05', 2): [
 ('A binder (SZC or patiromer) plus dialysis', True, 'SZC 10 g or patiromer 8.4 g. Calcium, insulin and albuterol do not remove potassium.'),
 ('Calcium gluconate repeated every hour', False, 'Calcium stabilizes, does not remove.'),
 ('Albuterol 10 to 20 mg by nebulizer', False, 'Shifts potassium into cells.'),
 ('Insulin infusion until potassium is 4', False, 'Shifts potassium into cells.')],
('cc06', 0): [
 ('3% saline 100 to 150 mL bolus, up to 3 times', True, 'Over 10 to 20 minutes each; aim for a 4 to 6 mmol/L rise.'),
 ('3% saline 500 mL as one bolus over 1 hour', False, 'Too much too fast; overcorrection risk.'),
 ('Normal saline 1 L given over 8 hours', False, 'Too slow for a seizure; may worsen SIADH.'),
 ('Fluid restriction to 1 L per day', False, 'For chronic, asymptomatic SIADH.')],
('cc06', 1): [
 ('About 10 in 24 h (8 if high risk)', True, 'High risk: alcohol use, low K, malnutrition, liver disease.'),
 ('About 12 in 24 h and 18 in 48 h', False, 'An older, higher limit.'),
 ('About 4 in 24 h for all patients', False, 'That is the initial emergency goal, not the limit.'),
 ('About 20 in 24 h if symptomatic', False, 'Causes osmotic demyelination.')],
('cc06', 2): [
 ('Stop 3% saline; give D5W ± desmopressin', True, 'Relower per protocol.'),
 ('Continue 3% saline at a slower rate', False, 'Already past the limit.'),
 ('Switch to normal saline 100 mL/h', False, 'Still raises sodium.'),
 ('Start tolvaptan 15 mg by mouth', False, 'Raises sodium further.')],
('cc08', 2): [
 ('Add D5 or D10; lower insulin to 0.05/kg/h', True, 'Keep insulin until ketones clear.'),
 ('Stop insulin; restart when glucose is 300', False, 'Ketones keep building.'),
 ('Keep 0.1 units/kg/h and add no dextrose', False, 'Hypoglycemia risk.'),
 ('Switch now to sliding scale SC insulin', False, 'DKA is not resolved.')],
('cc08', 3): [
 ('DKA resolved, SC basal given 1 to 2 h before', True, 'BHB below 0.6 and pH 7.3+ or bicarbonate 18+.'),
 ('Glucose below 200 mg/dL on two checks', False, 'Glucose falls before ketones clear.'),
 ('Anion gap below 20 mEq/L once', False, 'Use the consensus resolution criteria.'),
 ('After 24 hours on the drip', False, 'Time alone does not decide.')],
('cc09', 0): [
 ('40 mEq/h; peripheral limit is 10 mEq/h', True, 'Usual peripheral limit; check local policy.'),
 ('KCl must be mixed in D5W only', False, 'Diluent is not the issue.'),
 ('Nothing; 40 mEq/h suits K of 2.9', False, 'Unsafe peripherally.'),
 ('It should be 40 mEq IV push instead', False, 'Never push KCl.')],
('cc10', 1): [
 ('When the risk resolves or at transfer', True, 'Avoid continuing at discharge.'),
 ('At hospital discharge, not before', False, 'Often continued by mistake.'),
 ('After 6 weeks of treatment total', False, 'Not a prophylaxis duration.'),
 ('Never; continue it lifelong', False, 'Long term PPI risks.')],
}

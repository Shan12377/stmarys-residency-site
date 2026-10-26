# Module 13 balancing and Module 14 (Practice Advancement) rewrites.
R = {
('ms01', 1): [
 ('Smart pump libraries and premixes', True, 'Standard concentrations matched to pumps; remove concentrated electrolytes from units.'),
 ('Retraining staff after each error', False, 'Education alone is a weak fix (ISMP hierarchy).'),
 ('Warning stickers on high alert vials', False, 'Weak; people stop seeing them.'),
 ('A new policy that staff must sign', False, 'Rules and policies are weak fixes.')],
('ms06', 1): [
 ('Console the person; fix the system', True, 'Just culture: console a slip, coach at risk behavior, act on reckless behavior.'),
 ('Punish every error to deter others', False, 'Drives errors underground.'),
 ('Ignore all errors to protect morale', False, 'At risk and reckless behavior need action.'),
 ('Suspend after a second human slip', False, 'Slips are consoled and the system fixed.')],
('ms08', 1): [
 ('2 h med errors, 2 h controlled drugs', True, 'Board approved courses.'),
 ('5 h pain management and 2 h ethics', False, 'Not the Florida required topics.'),
 ('1 h HIV/AIDS and 2 h ethics', False, 'Not the current required pair.'),
 ('3 h immunization for every pharmacist', False, 'Only if certified to immunize.')],
('pa01', 0): [
 ('High alert, high risk, high cost or high volume', True, 'Or a drug with a new safety alert.'),
 ('Criteria from a label or guideline; small sample', True, 'Small enough to review by hand.'),
 ('Whatever is easiest to publish, no leadership input', False, 'Align with hospital priorities.'),
 ('A rarely used drug with no clear criteria', False, 'Too few cases and nothing to measure against.'),
 ('Every drug on formulary at once', False, 'Too broad to finish.')],
('pa01', 1): [
 ('Hard wired: order sets, pump limits, defaults', True, 'Forcing functions beat education.'),
 ('Reminder emails to every prescriber', False, 'Weak; fades quickly.'),
 ('A one time staff in service', False, 'Education alone is weak.'),
 ('A new policy document on the intranet', False, 'Rules alone are weak.')],
('pa02', 0): [
 ('Usually QI; ask the IRB before collecting data', True, 'If you plan to present or publish.'),
 ('Research; a full IRB protocol is always needed', False, 'Local QI usually is not research.'),
 ('QI; posters never need IRB input', False, 'Ask for a determination before presenting.'),
 ('Ask the IRB after the poster is accepted', False, 'Too late; ask before collecting data.')],
('pa02', 1): [
 ('Inside St. Mary\'s systems; de identified to present', True, 'HIPAA.'),
 ('A personal laptop, if password protected', False, 'Never on personal devices.'),
 ('Personal email to work on at home', False, 'Never.'),
 ('A public cloud folder shared with the team', False, 'Never.')],
('pa03', 0): [
 ('What are we trying to accomplish?', True, 'IHI Model for Improvement.'),
 ('How will we know a change is better?', False, 'The second question.'),
 ('What change will result in improvement?', False, 'The third question.'),
 ('Who caused the documentation gap?', False, 'Not a QI question.')],
('pa03', 1): [
 ('A small PDSA: one unit or shift, measure, adjust', True, ''),
 ('Roll it out hospital wide on day one', False, 'Test small first.'),
 ('Run a randomized trial for 12 months', False, 'Research design; QI tests rapidly.'),
 ('Wait for next year\'s MUE to recheck', False, 'Too slow.')],
('pa04', 0): [
 ('2.6 percentage points (27.5 minus 24.9)', True, ''),
 ('10.4% (2.6 divided by 24.9)', False, 'That is the relative risk increase.'),
 ('27.5 percentage points', False, 'The event rate, not the difference.'),
 ('1.1 (27.5 divided by 24.9)', False, 'That is the relative risk.')],
('pa04', 1): [
 ('About 38 (1 / 0.026)', True, ''),
 ('About 26 (1 / 0.038)', False, 'Inverted digits.'),
 ('About 10 (1 / 0.104)', False, 'Uses the relative increase.'),
 ('About 4 (1 / 0.26)', False, 'Decimal error.')],
('pa05', 0): [
 ('ARR 7.1 points; NNT about 14 for 12 months', True, ''),
 ('ARR 81%; NNT about 1', False, '81% is the relative reduction.'),
 ('ARR 7.1 points; NNT about 71', False, 'NNT = 1 / 0.071.'),
 ('ARR 1.7 points; NNT about 59', False, 'Uses the apixaban rate alone.')],
('pa05', 1): [
 ('About 53 (1 / 0.019)', True, ''),
 ('About 31 (1 / 0.032)', False, 'Uses the bridging rate alone.'),
 ('About 77 (1 / 0.013)', False, 'Uses the no bridging rate alone.'),
 ('About 2 (3.2 / 1.3)', False, 'That is the relative risk.')],
('pa06', 0): [
 ('It did not prove reduced dose is not worse', True, 'It does not prove it is worse either.'),
 ('It proved reduced dose is worse', False, 'Failure to show noninferiority is not proof of inferiority.'),
 ('It proved both doses are equal', False, 'Not shown.'),
 ('It proved reduced dose is superior', False, 'Not tested that way.')],
('pa06', 1): [
 ('Weigh less bleeding vs uncertain protection', True, 'For each patient, alongside CHEST 2021.'),
 ('Use full dose for every patient', False, 'Ignores the bleeding difference.'),
 ('Use reduced dose for every patient', False, 'Ignores the uncertainty.'),
 ('Ignore it; it failed its endpoint', False, 'Still informative.')],
('pa07', 0): [
 ('Interventions by category, no identifiers', True, 'Renal dose, allergy, IV to PO, duplicates, errors caught.'),
 ('Nothing; it is all in memory', False, 'Untracked work is invisible.'),
 ('Patient names and MRNs in a notebook', False, 'Never keep identifiers.'),
 ('Only the hours worked each shift', False, 'Does not show value.')],
('pa08', 0): [
 ('Why, what nurses see first, numbers, antidote, case', True, 'Reflexes before breathing; end with 3 questions.'),
 ('Forty slides of pharmacokinetics', False, 'Too much for 15 minutes.'),
 ('A handout and no discussion', False, 'Less retention.'),
 ('Read the package insert aloud', False, 'Not focused on nurse actions.')],
}

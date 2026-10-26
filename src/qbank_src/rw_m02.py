# Module 0 balancing fixes and Module 2 rewrites.
R = {
('h02', 2): [
 ('Obesity, very low weight, or an unlikely weight', True, 'Choose actual, ideal or adjusted weight per protocol.'),
 ('Only when the patient is over 65 years old', False, 'Age is already in the formula.'),
 ('Only when SCr is above 2.0 mg/dL', False, 'SCr does not decide which weight to use.'),
 ('Only for drugs that are dosed in mg/kg', False, 'Weight choice affects CrCl for every renally dosed drug.')],
('h07', 2): [
 ('ISMP Do Not Crush list and the exact product', True, 'Extended release and enteric coated products are classic no crush.'),
 ('Trissel\'s IV compatibility for the tablet', False, 'Trissel\'s covers IV compatibility, not crushing.'),
 ('LactMed entry for the drug being crushed', False, 'Breastfeeding reference.'),
 ('The pregnancy and lactation label section', False, 'Unrelated to crushing.')],
('h08', 0): [
 ('Which drug, its concentration, and what else runs', True, 'Compatibility depends on all three.'),
 ('How long the heparin drip has been running', False, 'Not the compatibility question.'),
 ('The patient\'s weight and kidney function', False, 'Dosing, not compatibility.'),
 ('Whether the line is peripheral or central', False, 'Line type matters for some drugs, but you need the drugs and concentrations.')],
('h08', 1): [
 ('Trissel\'s or the King Guide (or free Stabilis)', True, ''),
 ('LactMed (NIH) drug compatibility pages', False, 'LactMed covers breastfeeding only.'),
 ('The ISMP Do Not Crush list for IV drugs', False, 'Oral dosage forms only.'),
 ('NeoFax neonatal dosing monographs only', False, 'Dosing reference; some compatibility, not the primary source.')],
('pk01', 0): [
 ('AUC24 of 400 to 600 (assuming MIC 1)', True, 'Rybak 2020, Recommendation 1.'),
 ('Trough of 15 to 20 mcg/mL', False, 'The 2009 trough target; no longer recommended for serious MRSA because it overshoots AUC and raises kidney injury.'),
 ('Trough of 10 to 15 mcg/mL', False, 'Older target for less serious infections; troughs are no longer the dosing goal.'),
 ('AUC24 of 600 to 800 (assuming MIC 1)', False, 'Above 600 is where kidney injury risk climbs.')],
('pk01', 1): [
 ('Bayesian software with one or two levels', True, 'Preferred.'),
 ('Two levels (peak and trough) with first order equations', True, 'Acceptable alternative.'),
 ('A single trough compared with 15 to 20 mcg/mL', False, 'Trough only monitoring is no longer recommended.'),
 ('A single peak 1 hour after the infusion', False, 'A peak alone cannot estimate AUC without a model.')],
('pk01', 2): [
 ('Within the first 24 to 48 hours', True, 'Rybak 2020, Recommendation 3.'),
 ('Within the first 72 to 96 hours', False, 'Too slow for bacteremia.'),
 ('At the third or fourth dose, at steady state only', False, 'Steady state helps two level math, but Bayesian tools let you dose earlier.'),
 ('Within 7 days, before the first weekly review', False, 'Far too late.')],
('pk02', 0): [
 ('No: the load depends on body size, not kidneys', True, 'Load by weight, maintain by kidneys.'),
 ('Yes: cut the load in half when CrCl is under 50', False, 'Halving is a maintenance adjustment idea, never for the load.'),
 ('Yes: give 15 mg/kg instead of 25 mg/kg', False, '15 mg/kg is a maintenance dose size, not a reduced load.'),
 ('No load: start maintenance every 24 hours', False, 'Critically ill patients benefit most from a load.')],
('pk02', 1): [
 ('20 to 35 mg/kg actual weight, max 3,000 mg', True, 'Rybak 2020, Recommendation 10.'),
 ('20 to 25 mg/kg actual weight, max 3,000 mg', False, 'That narrower range is the obesity recommendation.'),
 ('15 to 20 mg/kg actual weight, max 2,000 mg', False, '15 to 20 mg/kg is the maintenance dose and the continuous infusion load.'),
 ('25 mg/kg actual weight, then 7.5 to 10 mg/kg', False, 'That is the hemodialysis load and maintenance.')],
('pk02', 2): [
 ('200 minutes (3 hours 20 minutes)', True, '2,000 mg / 10 mg/min.'),
 ('120 minutes (2 hours)', False, 'That follows a 1 g per hour policy, not the 10 mg/min label rate.'),
 ('60 minutes (1 hour)', False, '60 minutes is the label minimum for doses up to about 600 mg at 10 mg/min.'),
 ('100 minutes (1 hour 40 minutes)', False, 'That is 1,000 mg at 10 mg/min.')],
('pk03', 0): [
 ('About 82 mL/min', True, '(140 minus 58) x 72 / (72 x 1.0).'),
 ('About 70 mL/min', False, 'That applies the 0.85 female factor to a man.'),
 ('About 58 mL/min', False, 'That subtracts age from 116 instead of 140.'),
 ('About 98 mL/min', False, 'That uses an SCr of about 0.8.')],
('pk03', 1): [
 ('1,250 mg every 12 hours (about 17 mg/kg)', True, 'Inside 15 to 20 mg/kg every 8 to 12 hours.'),
 ('1,250 mg every 24 hours (about 17 mg/kg)', False, 'Every 24 hours fits reduced kidney function, not CrCl 82.'),
 ('1,750 mg every 12 hours (about 24 mg/kg)', False, 'Above the 20 mg/kg maintenance range; 25 mg/kg is a loading dose size.'),
 ('750 mg every 12 hours (about 10 mg/kg)', False, '10 mg/kg is the high flux dialysis maintenance size.')],
('pk03', 2): [
 ('Early, so AUC is known within 24 to 48 hours', True, 'Serious infection and a long course need AUC monitoring.'),
 ('Only if creatinine rises during treatment', False, 'Waiting for injury is too late.'),
 ('Weekly, starting at the end of week one', False, 'Weekly pre dialysis levels apply to hemodialysis, not here.'),
 ('Never, because his kidneys are normal', False, 'Long serious courses need monitoring.')],
('pk04', 0): [
 ('ln(30/10) / 9.5 h = 0.116 per hour', True, 'Time between draws: 11.5 minus 2 = 9.5 hours.'),
 ('ln(30/10) / 12 h = 0.092 per hour', False, 'Uses the dosing interval instead of the time between the two draws.'),
 ('(30 minus 10) / 9.5 h = 2.1 per hour', False, 'Elimination is exponential; you need the natural log of the ratio.'),
 ('log10(30/10) / 9.5 h = 0.050 per hour', False, 'ke uses the natural log, not log base 10.')],
('pk04', 1): [
 ('About 33.7 mcg/mL', True, '30 x e^(0.116 x 1).'),
 ('30 mcg/mL (as drawn)', False, 'The draw was 1 hour after the infusion ended; the true end of infusion peak is higher.'),
 ('About 37.8 mcg/mL', False, 'Extrapolates back 2 hours (to the start of the infusion) instead of 1.'),
 ('About 26.7 mcg/mL', False, 'Extrapolates in the wrong direction (forward in time).')],
('pk04', 2): [
 ('About 9.4 mcg/mL', True, '10 x e^(minus 0.116 x 0.5).'),
 ('10 mcg/mL (as drawn)', False, 'The draw was 30 minutes before the end of the interval.'),
 ('About 8.9 mcg/mL', False, 'Extrapolates forward 1 hour instead of 30 minutes.'),
 ('About 10.6 mcg/mL', False, 'Extrapolates in the wrong direction.')],
('pk04', 3): [
 ('About 462 (231 per dose x 2)', True, 'Infusion part 21.6 + elimination part 209.6 = 231 per 12 hours.'),
 ('About 231 (one dose only)', False, 'That is one interval; multiply by 24/12.'),
 ('About 384 (drawn levels, no extrapolation)', False, 'Using the drawn 30 and 10 underestimates the true area.'),
 ('About 924 (231 x 4)', False, 'Multiplied by 4 doses; every 12 hours is 2 doses per day.')],
('pk04', 4): [
 ('Continue the regimen; keep watching kidney function', True, '462 is inside 400 to 600.'),
 ('Increase the dose: the trough of 10 is below 15', False, 'Trough thinking; the AUC is on target.'),
 ('Decrease the dose: AUC above 400 raises kidney risk', False, 'Risk climbs above 600, not 400.'),
 ('Change to every 8 hours to raise the trough', False, 'Same trough error; AUC is on target.')],
('pk05', 0): [
 ('1,500 mg every 12 hours (predicted AUC about 480)', True, '1,000 x 500/320 = 1,560, rounded to 1,500.'),
 ('1,250 mg every 12 hours (predicted AUC about 400)', False, 'Lands on the bottom edge of the range, below the 500 goal.'),
 ('2,000 mg every 12 hours (predicted AUC about 640)', False, 'Above 600: kidney injury risk.'),
 ('1,500 mg every 24 hours (predicted AUC about 240)', False, 'Halves the daily exposure.')],
('pk05', 1): [
 ('Near new steady state (sooner with Bayesian) and with kidney changes', True, ''),
 ('Only at the end of the planned course', False, 'Too late to adjust.'),
 ('Every day for the whole course', False, 'More often than needed when stable.'),
 ('Never: one AUC estimate covers the whole course', False, 'Kidney function changes during illness.')],
('pk06', 0): [
 ('AUC above 600 with early kidney injury', True, 'SCr up about 67%.'),
 ('Expected creatinine rise from piperacillin tazobactam alone', False, 'The combination is linked to AKI, but the AUC of 780 is the fixable part.'),
 ('Contrast nephropathy from a recent scan', False, 'Possible contributor; nothing in the case suggests contrast.'),
 ('Lab variation; repeat the SCr in a week', False, 'A 67% rise meets the AKI definition.')],
('pk06', 1): [
 ('Hold the next dose, recheck a level, restart lower by AUC', True, ''),
 ('Ask whether MRSA coverage is still needed', True, 'Stopping vancomycin is the best kidney protection.'),
 ('Ask about changing pip tazo (for example to cefepime)', True, 'The combination is linked to more AKI in observational studies.'),
 ('Add furosemide to flush the kidneys', False, 'Loop diuretics do not protect kidneys and add ototoxicity with aminoglycosides.'),
 ('Switch to a continuous infusion at the same daily dose', False, 'Same daily exposure, same AUC.')],
('pk06', 2): [
 ('Mostly observational; reported to raise the risk', True, 'Rybak 2020 language.'),
 ('Proven by several large randomized trials', False, 'No large RCT proves it.'),
 ('Disproven; the creatinine rise is only a lab effect', False, 'Debated, not disproven.'),
 ('Shown only in children, not adults', False, 'Signals exist in both.')],
('pk07', 0): [
 ('Vancomycin infusion reaction from a fast infusion', True, 'Histamine release, rate related.'),
 ('IgE mediated anaphylaxis', False, 'No hypotension, wheeze or airway swelling.'),
 ('DRESS syndrome', False, 'Appears days to weeks into therapy with fever, rash and organ involvement.'),
 ('Linear IgA bullous dermatosis', False, 'A rare blistering reaction days into therapy.')],
('pk07', 1): [
 ('Pause, antihistamine if ordered, restart slower', True, ''),
 ('Document as infusion reaction, not allergy; longer infusion next time', True, ''),
 ('Stop vancomycin permanently and switch to daptomycin', False, 'Not needed for an infusion reaction.'),
 ('Give epinephrine 0.5 mg IM now', False, 'That is the anaphylaxis treatment.')],
('pk08', 0): [
 ('20 to 25 mg/kg actual weight, max 3,000 mg', True, 'Rybak 2020, Recommendation 12.'),
 ('20 to 35 mg/kg actual weight, max 3,000 mg', False, 'That is the general critical illness range.'),
 ('25 mg/kg ideal body weight, no maximum', False, 'Loading uses actual weight, and the cap is 3,000 mg.'),
 ('25 mg/kg adjusted body weight, max 2,000 mg', False, 'Adjusted weight is an aminoglycoside concept.')],
('pk08', 1): [
 ('Usually 4,500 mg/day or less to start', True, 'Then AUC guides changes.'),
 ('Usually 3,000 mg/day or less to start', False, '3,000 mg is the single loading dose cap.'),
 ('20 mg/kg every 8 hours by actual weight (9,600 mg/day)', False, 'Clearance does not rise with weight in proportion.'),
 ('Usually 2,000 mg/day or less to start', False, 'Underdoses most obese patients with normal kidneys.')],
('pk09', 0): [
 ('25 mg/kg after the session (about 1,750 mg)', True, 'Rybak 2020, Recommendation 13.'),
 ('35 mg/kg during the session (high permeability)', False, 'Intradialytic loading is 30 to 35 mg/kg; this dose is given after dialysis.'),
 ('15 mg/kg after the session', False, '15 mg/kg is a typical maintenance dose size.'),
 ('5 mg/kg because the kidneys do not work', False, 'The load fills volume regardless of kidneys.')],
('pk09', 1): [
 ('About 10 mg/kg after each session; pre HD level weekly', True, 'Pre dialysis levels of 15 to 20 likely reach the AUC target.'),
 ('About 7.5 mg/kg after each session; pre HD level weekly', False, '7.5 mg/kg is for low permeability dialyzers.'),
 ('About 15 mg/kg daily with daily troughs', False, 'Dosing follows the dialysis schedule.'),
 ('About 25 mg/kg after each session, no levels', False, '25 mg/kg is the load.')],
('pk10', 0): [
 ('Load 15 to 20 mg/kg, then 30 to 40 mg/kg/day', True, 'Rybak 2020, Recommendation 7 (up to 60 mg/kg/day).'),
 ('Load 20 to 35 mg/kg, then 15 to 20 mg/kg every 12 h', False, 'Intermittent dosing.'),
 ('No load, then 60 to 80 mg/kg/day', False, '60 to 80 mg/kg/day is the pediatric range.'),
 ('Load 25 mg/kg, then 10 mg/kg/day', False, 'Close to hemodialysis dosing.')],
('pk10', 1): [
 ('About 528 (22 x 24)', True, 'Continuous infusion: AUC24 = Css x 24.'),
 ('About 264 (22 x 12)', False, 'Multiplies by 12 hours instead of 24.'),
 ('About 22 (the level itself)', False, 'The level is not the AUC.'),
 ('About 1,056 (22 x 48)', False, 'Multiplies by 48 hours.')],
('pk10', 2): [
 ('Y site compatibility with every drug sharing the line', True, 'It runs all day; check Trissel\'s or use a dedicated lumen.'),
 ('Light protection of the bag and tubing', False, 'Not required for vancomycin.'),
 ('PVC free tubing to prevent adsorption', False, 'That matters for nitroglycerin and insulin.'),
 ('An in line 0.22 micron filter', False, 'Needed for phenytoin and some others, not routine for vancomycin.')],
('pk11', 0): [
 ('60 to 80 mg/kg/day divided every 6 to 8 hours', True, 'Children 3 months and older (Rybak 2020).'),
 ('45 to 60 mg/kg/day divided every 6 to 8 hours', False, 'Older empiric dosing the guideline says may be insufficient.'),
 ('15 to 20 mg/kg every 8 to 12 hours', False, 'Adult maintenance.'),
 ('30 to 40 mg/kg/day as a continuous infusion', False, 'Adult continuous infusion maintenance.')],
('pk11', 1): [
 ('300 mg every 6 hours', True, '60 x 20 = 1,200 mg/day / 4.'),
 ('400 mg every 6 hours', False, 'That is 80 mg/kg/day, the top of the range, not 60.'),
 ('1,200 mg every 6 hours', False, 'The whole day\'s dose given four times.'),
 ('400 mg every 8 hours', False, 'That is 60 mg/kg/day divided every 8 hours, not every 6.')],
('pk11', 2): [
 ('A pediatric reference and St. Mary\'s pediatric protocol', True, 'Lexicomp Pediatric or Harriet Lane.'),
 ('The adult Lexicomp monograph, scaled by weight', False, 'Adult doses do not scale safely.'),
 ('NeoFax, since it covers all children', False, 'NeoFax is for neonates.'),
 ('The FDA label adult section', False, 'Use the pediatric section or a pediatric reference.')],
('pk12', 0): [
 ('IV vancomycin does not reach the colon', True, 'C. difficile needs oral therapy.'),
 ('The IV dose is too low; use 1.5 g every 12 hours', False, 'Raising the IV dose still does not reach the colon.'),
 ('IV vancomycin is fine but needs an AUC target', False, 'AUC dosing is for systemic infections.'),
 ('C. difficile requires IV metronidazole only', False, 'Metronidazole is a fallback; the preferred agents are oral.')],
('pk12', 1): [
 ('Fidaxomicin 200 mg BID x 10 days; oral vanc 125 mg QID x 10 days alternative', True, 'IDSA/SHEA 2021.'),
 ('Oral vancomycin 500 mg QID x 10 days first line', False, '500 mg QID is for fulminant C. difficile.'),
 ('Metronidazole 500 mg TID x 10 days first line', False, 'Only for nonsevere disease when the others are unavailable.'),
 ('Fidaxomicin 200 mg BID x 5 days, then every other day', False, 'Extended pulsed fidaxomicin is a recurrence option.')],
('pk13', 0): [
 ('Concentration dependent with a post antibiotic effect', True, ''),
 ('Time dependent, like beta lactams', False, 'Beta lactams depend on time above MIC.'),
 ('AUC dependent with no post antibiotic effect', False, 'AUC/MIC describes vancomycin.'),
 ('Bacteriostatic, needing constant levels', False, 'Aminoglycosides are bactericidal.')],
('pk13', 1): [
 ('Kidney injury (usually reversible)', True, ''),
 ('Ototoxicity (often irreversible)', True, ''),
 ('Neuromuscular blockade', True, ''),
 ('Vancomycin infusion reaction', False, 'Vancomycin only.'),
 ('QT prolongation', False, 'A fluoroquinolone and macrolide concern.')],
('pk13', 2): [
 ('Loop diuretics (ears)', True, ''),
 ('Vancomycin, amphotericin B, contrast, NSAIDs (kidneys)', True, ''),
 ('Rifampin (induces aminoglycoside metabolism)', False, 'Aminoglycosides are not metabolized; they are cleared unchanged by the kidneys.'),
 ('Proton pump inhibitors (reduce absorption)', False, 'IV aminoglycosides are not absorbed from the gut anyway.')],
('pk14', 0): [
 ('73 kg', True, '50 + 2.3 x 10.'),
 ('68.5 kg', False, 'Female formula (45.5 base).'),
 ('87.8 kg', False, 'That is his adjusted body weight.'),
 ('77.9 kg', False, 'Uses 2.54 (cm per inch) instead of 2.3 kg per inch.')],
('pk14', 1): [
 ('Adjusted: 73 + 0.4 x 37 = about 88 kg', True, 'Above about 120% of ideal.'),
 ('Actual: 110 kg', False, 'Overdoses obese patients.'),
 ('Ideal: 73 kg', False, 'Underdoses; some extra body water comes with extra weight.'),
 ('Adjusted: 73 + 0.25 x 37 = about 82 kg', False, '0.25 is a factor some protocols use for other drugs; aminoglycosides use 0.4.')],
('pk14', 2): [
 ('About 615 mg (7 x 87.8)', True, 'Round per protocol.'),
 ('About 770 mg (7 x 110)', False, 'Actual weight.'),
 ('About 511 mg (7 x 73)', False, 'Ideal weight.'),
 ('About 439 mg (5 x 87.8)', False, '5 mg/kg is the once daily intraamniotic infection dose.')],
('pk15', 0): [
 ('Yes: 10 hours after the start, inside 6 to 14 hours', True, 'Nicolau 1995.'),
 ('No: it must be a trough just before the next dose', False, 'Traditional dosing uses troughs; Hartford uses one random level.'),
 ('No: it must be drawn 1 to 2 hours after the start', False, 'That is a peak (for vancomycin two level AUC).'),
 ('No: it must be drawn 18 to 24 hours after the start', False, 'Outside the nomogram window.')],
('pk15', 1): [
 ('Every 36 hours (the longer interval)', True, ''),
 ('Every 24 hours (the shorter interval)', False, 'On a line choose the longer.'),
 ('Every 48 hours, to be safe', False, 'Skips a zone.'),
 ('Repeat the level before choosing', False, 'Not needed; the rule decides.')],
('pk15', 2): [
 ('Hold scheduled doses; redose when below 1 mcg/mL', True, 'Clearance too slow for this method.'),
 ('Give the next dose in 48 hours anyway', False, 'Too much drug still on board.'),
 ('Give 3.5 mg/kg every 48 hours instead', False, 'Not a Hartford step.'),
 ('Switch to 1 mg/kg every 8 hours now', False, '1 mg/kg every 8 hours is synergy dosing.')],
('pk15', 3): [
 ('Pregnancy, burns over 20%, ascites, CrCl below 20 or dialysis', True, 'Original exclusions.'),
 ('Endocarditis synergy, cystic fibrosis, children', True, ''),
 ('Adults over 65 with normal kidney function', False, 'Age alone was not an exclusion.'),
 ('Adults with obesity using adjusted weight', False, 'Obese adults can use Hartford with a dosing weight per protocol.')],
('pk16', 0): [
 ('Peak 30 min after a 30 min infusion; trough before next dose', True, ''),
 ('Peak 1 to 2 hours after the infusion; trough at random', False, 'The 1 to 2 hour peak is the vancomycin AUC draw.'),
 ('One random level 6 to 14 hours after the start', False, 'That is Hartford.'),
 ('Trough only, 30 minutes before the next dose', False, 'Traditional dosing needs both.')],
('pk16', 1): [
 ('Avoid peaks above 12 and troughs above 2 mcg/mL', True, 'Gentamicin label.'),
 ('Avoid peaks above 35 and troughs above 10 mcg/mL', False, 'Those are amikacin label limits.'),
 ('Keep troughs at 15 to 20 mcg/mL', False, 'The old vancomycin trough target.'),
 ('Keep peaks at 3 to 4 and troughs below 1 mcg/mL', False, 'Synergy targets for endocarditis.')],
('pk16', 2): [
 ('About 2.75 hours', True, 'ke = ln(7/1.2)/7 = 0.252; 0.693/0.252.'),
 ('About 3.15 hours', False, 'Uses 8 hours (the interval) instead of 7 hours between draws.'),
 ('About 6.4 hours', False, 'Uses log base 10 instead of the natural log.'),
 ('About 0.25 hours', False, 'That number is ke, not the half life.')],
('pk17', 0): [
 ('About 1 mg/kg every 8 hours; peak 3 to 4, trough below 1', True, 'AHA 2015.'),
 ('7 mg/kg once daily by the Hartford nomogram', False, 'Endocarditis is a Hartford exclusion.'),
 ('5 mg/kg once daily by levels', False, 'Gram negative extended interval dosing.'),
 ('2 mg/kg load, then 1.5 mg/kg every 8 hours', False, 'The intraamniotic infection regimen.')],
('pk17', 1): [
 ('Ampicillin plus ceftriaxone', True, 'AHA 2015.'),
 ('Vancomycin plus gentamicin', False, 'Keeps the aminoglycoside and adds vancomycin kidney risk.'),
 ('Daptomycin alone', False, 'An option for resistant enterococci, not the standard alternative here.'),
 ('Ampicillin plus cefazolin', False, 'Cefazolin lacks the PBP binding that gives ceftriaxone synergy.')],
('pk18', 0): [
 ('Aminoglycoside ototoxicity, worsened by furosemide', True, 'Cochlear and vestibular.'),
 ('Benign positional vertigo unrelated to drugs', False, 'Never assume with an aminoglycoside.'),
 ('Furosemide alone; gentamicin does not affect the ear', False, 'Both are ototoxic.'),
 ('Vancomycin ototoxicity', False, 'She is not on vancomycin.')],
('pk18', 1): [
 ('Tell the team today; switch if cultures allow', True, ''),
 ('Check levels and kidney function; review furosemide', True, ''),
 ('Suggest an audiology evaluation', True, ''),
 ('Lower the dose by 25% and continue', False, 'Damage may be permanent; stopping beats lowering.')],
('pk19', 0): [
 ('Order and send the septic patient\'s vancomycin load', True, 'Time to antibiotics drives survival.'),
 ('Plot the gentamicin level first, since it is ready', False, 'The next dose is hours away.'),
 ('Document the AUC of 455 first', False, 'On target; routine.'),
 ('Call the stable patient\'s team about the AUC', False, 'Not needed now.')],
('pk19', 1): [
 ('Plot the gentamicin level and set the next dose time', True, ''),
 ('Write the AUC note for the stable patient', False, 'Last.'),
 ('Recheck the septic patient\'s CrCl', False, 'Maintenance can wait for labs.'),
 ('Order a vancomycin trough for the septic patient', False, 'Too early.')],
('pk19', 2): [
 ('2,000 to 2,250 mg (about 22 to 25 mg/kg)', True, 'Within 20 to 35 mg/kg, under 3,000 mg.'),
 ('1,000 mg, in case her kidneys are poor', False, 'Loads are not reduced for kidneys.'),
 ('3,150 mg (35 mg/kg)', False, 'Above the 3,000 mg cap.'),
 ('1,350 mg (15 mg/kg)', False, '15 mg/kg is a maintenance dose.')],
}

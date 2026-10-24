# Vancomycin and aminoglycoside drug cards.
def card(title, sections, sources): return {'title': title, 'sections': sections, 'sources': sources}
def s(t, url, mark='✅'): return {'t': t, 'url': url, 'mark': mark}
RYBAK = s('Rybak MJ, et al. Vancomycin consensus guideline (ASHP/IDSA/PIDS/SIDP). Am J Health Syst Pharm 2020;77:835-864', 'https://doi.org/10.1093/ajhp/zxaa036', '✅✅')
VANC = s('Vancomycin injection prescribing information (DailyMed)', 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=vancomycin+injection')
CDI = s('IDSA/SHEA 2021 C. difficile update. Clin Infect Dis 2021;73:e1029-e1044', 'https://doi.org/10.1093/cid/ciab549')
NIC = s('Nicolau DP, et al. Once daily aminoglycoside program (Hartford). Antimicrob Agents Chemother 1995;39:650-655', 'https://doi.org/10.1128/AAC.39.3.650')
GENT = s('Gentamicin injection prescribing information (DailyMed)', 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=gentamicin+injection')
AHA = s('AHA 2015 infective endocarditis. Circulation 2015;132:1435-1486', 'https://doi.org/10.1161/CIR.0000000000000296')
LOCAL = {'t': "St. Mary's pharmacy to dose vancomycin and aminoglycoside protocol (verify locally)", 'url': '', 'mark': '⚠️'}

PK = {
'vancomycin': card('Vancomycin IV (and oral)', [
  ('What it is for', 'Serious gram positive infections, especially MRSA (bacteremia, pneumonia, osteomyelitis, meningitis), and empiric coverage when MRSA is likely. **Oral** vancomycin only treats C. difficile ✅✅ [Rybak; IDSA 2021].'),
  ('How it works', 'Binds the D-Ala-D-Ala end of cell wall building blocks; too big to cross gram negative outer membranes. Kills slowly; total exposure (AUC) predicts success.'),
  ('Target', 'AUC over 24 hours **400 to 600** (assuming MIC 1), by Bayesian software (preferred) or two levels; trough only dosing to 15 to 20 is no longer recommended for serious MRSA ✅ [Rybak].'),
  ('Dose and weight', '**Load:** 20 to 35 mg/kg **actual** body weight, max 3,000 mg; obese 20 to 25 mg/kg, max 3,000 mg. **Maintenance:** 15 to 20 mg/kg every 8 to 12 hours with normal kidneys; obese usually 4,500 mg/day or less to start. **Children 3 months+:** 60 to 80 mg/kg/day divided every 6 to 8 hours. **Continuous infusion:** load 15 to 20 mg/kg, then 30 to 40 mg/kg/day (up to 60), target level 20 to 25. **Hemodialysis (after session):** load 25 mg/kg, then 7.5 mg/kg (low permeability) or 10 mg/kg (high permeability) after each session, pre dialysis levels at least weekly ✅ [Rybak].'),
  ('Show the math (two levels)', '1. ke = ln(C1 / C2) / hours between draws. 2. Half life = 0.693 / ke. 3. Back extrapolate the true peak to the end of the infusion: Cmax = C1 x e^(ke x t). 4. Forward extrapolate the true trough to the end of the interval. 5. AUC per dose = infusion time x (Cmax + Cmin) / 2 + (Cmax minus Cmin) / ke. 6. AUC24 = AUC per dose x doses per day. 7. New dose = old dose x target AUC / current AUC (linear).'),
  ('Rate', 'Label: at least 60 minutes and no faster than 10 mg/min, whichever is longer (1,500 mg = 150 minutes). Many hospitals use a 1 g per hour policy ⚠️ [St. Mary\'s]. Too fast causes the **vancomycin infusion reaction** (flushing, itching, low BP): a rate reaction, not an allergy.'),
  ('Kidneys and toxicity', 'Cleared by the kidneys. Kidney injury rises with AUC above 600, long courses, and other nephrotoxins (contrast, loop diuretics, aminoglycosides; piperacillin tazobactam has been reported to raise risk, mostly observational data) ✅ [Rybak]. Ototoxicity is rare.'),
  ('Monitoring', 'SCr at least daily early, urine output, AUC within 24 to 48 hours for serious infection, and again when kidney function or the dose changes ✅ [Rybak].'),
  ('What if...', '**Kidneys failing?** Same load; longer interval or smaller dose; level based dosing. **Flushing?** Pause, antihistamine, restart slower. **MRSA nares negative in pneumonia?** Consider stopping. **MSSA in blood?** Switch to cefazolin or nafcillin.'),
  ('Alternatives', 'Linezolid (pneumonia, skin; watch platelets and serotonergic drugs), daptomycin (not for pneumonia), ceftaroline. For C. diff: fidaxomicin or oral vancomycin 125 mg four times daily for 10 days ✅ [IDSA 2021].'),
], [RYBAK, VANC, CDI, LOCAL]),

'aminoglycoside': card('Gentamicin and tobramycin (aminoglycosides)', [
  ('What they are for', 'Serious gram negative infections, often combined with a beta lactam; low dose gentamicin for gram positive synergy (enterococcal endocarditis).'),
  ('How they work', 'Bind the 30S ribosome; uptake needs oxygen, so no anaerobic activity. **Concentration dependent killing with a post antibiotic effect**: high peak, then a drug free gap.'),
  ('Dosing weight', 'Ideal body weight (men 50 kg, women 45.5 kg, + 2.3 kg per inch over 5 feet). If actual is more than about 120% of ideal, use adjusted = IBW + 0.4 x (actual minus IBW). If actual is below ideal, use actual ⚠️ [protocol].'),
  ('Extended interval (Hartford)', '7 mg/kg once; one random level 6 to 14 hours after the start; plot for every 24, 36 or 48 hours; on a line pick the longer; above the q48h zone stop scheduled doses and redose when below 1 mcg/mL ✅ [Nicolau 1995]. **Not for:** pregnancy, burns over 20%, ascites, CrCl below 20 or dialysis, endocarditis synergy, cystic fibrosis, children ✅ [Nicolau].'),
  ('Traditional', 'Label: 3 mg/kg/day divided every 8 hours (up to 5 mg/kg/day for life threatening infection). Peak 30 minutes after the end of a 30 minute infusion; trough just before the next dose. Avoid peaks above 12 and troughs above 2 mcg/mL ✅ [label].'),
  ('Synergy (endocarditis)', 'About 3 mg/kg/day divided (for example 1 mg/kg every 8 hours), peak 3 to 4, trough below 1 ✅ [AHA 2015]. For E. faecalis, ampicillin plus ceftriaxone avoids aminoglycoside toxicity ✅ [AHA 2015].'),
  ('Toxicity (boxed warning)', 'Kidney injury (usually reversible), ototoxicity (hearing and balance, often permanent), neuromuscular blockade ✅ [label]. Ask about ringing ears and dizziness every day.'),
  ('Interactions', 'Loop diuretics (ears), vancomycin, amphotericin, contrast, NSAIDs (kidneys), neuromuscular blockers and magnesium (paralysis).'),
  ('What if...', '**Rising creatinine?** Get a level, lengthen the interval or stop. **Ringing ears?** Call today; switch if cultures allow. **Obese?** Adjusted weight. **Neonate?** Unit chart by GA or PMA and PNA, never Hartford.'),
  ('Alternatives', 'A beta lactam alone when susceptible; fluoroquinolones; for synergy in E. faecalis endocarditis, ampicillin plus ceftriaxone.'),
], [NIC, GENT, AHA, LOCAL]),
}

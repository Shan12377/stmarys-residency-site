import sys; sys.path.insert(0, sys.path[0])
from qb import O, S, C, src, write

MG = src('Magnesium Sulfate in 5% Dextrose label (MedLibrary)', 'https://medlibrary.org/lib/rx/meds/magnesium-sulfate-in-dextrose/', '✅✅')
CO712 = src('ACOG Committee Opinion 712: intrapartum management of intraamniotic infection. Obstet Gynecol 2017', 'https://doi.org/10.1097/AOG.0000000000002236')
GENT = src('Gentamicin injection prescribing information (DailyMed)', 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=gentamicin+injection')
SSC = src('Surviving Sepsis Campaign 2021. Crit Care Med 2021;49:e1063-e1143', 'https://doi.org/10.1097/CCM.0000000000005337', '✅✅')
RYBAK = src('Rybak MJ, et al. Vancomycin consensus guideline. Am J Health Syst Pharm 2020;77:835-864', 'https://doi.org/10.1093/ajhp/zxaa036')
CEFEPIME = src('FDA safety alert: cefepime and nonconvulsive status epilepticus (2012)', 'https://www.drugs.com/fda-alerts/544-0.html')
SUP = src('SCCM/ASHP 2024 stress ulcer prophylaxis guideline', 'https://www.sccm.org/clinical-resources/guidelines/guidelines/sccm-ashp-guideline-prevention-of-ugib')
ICH = src('2022 AHA/ASA guideline for spontaneous intracerebral hemorrhage. Stroke 2022;53:e282-e361', 'https://doi.org/10.1161/STR.0000000000000407', '✅✅')
KCEN = src('Kcentra prescribing information, DailyMed', 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=kcentra')
KDIGO = src('KDIGO dyskalemia conference. Kidney Int 2020;97:42-61', 'https://doi.org/10.1016/j.kint.2019.09.018')
DKA = src('Umpierrez GE, et al. Hyperglycemic crises consensus. Diabetes Care 2024;47:1257-1275', 'https://doi.org/10.2337/dci24-0032', '✅✅')
CAP = src('ATS/IDSA CAP guideline. Am J Respir Crit Care Med 2019;200:e45-e67', 'https://doi.org/10.1164/rccm.201908-1581ST')
LACT = src('LactMed (NIH): warfarin, enoxaparin, enalapril, codeine', 'https://www.ncbi.nlm.nih.gov/books/NBK501922/', '✅')
ELIQ = src('Eliquis prescribing information (lactation section), Pfizer', 'https://labeling.pfizer.com/ShowLabeling.aspx?id=14028')
FDACOD = src('FDA: codeine and tramadol in breastfeeding (2017)', 'https://www.fda.gov/Drugs/DrugSafety/ucm549679.htm')
ACC = src('ACC: antihypertensive medications in pregnancy and lactation (2026)', 'https://www.acc.org/latest-in-cardiology/articles/2026/07/02/15/04/antihypertensive-medications-in-pregnancy-and-lactation')
ASH = src('ASH 2018 HIT guideline. Blood Adv 2018;2:3360-3392', 'https://doi.org/10.1182/bloodadvances.2018024489')
DM = src('DailyMed prescribing information (linezolid, sertraline)', 'https://dailymed.nlm.nih.gov/dailymed/', '✅')
LOCAL = {'t': "St. Mary's protocols for each step (verify locally)", 'url': '', 'mark': '⚠️'}

CASES = [
C('mx01', 'Magnesium, fever and falling urine', 'L&D · 0200 · preeclampsia with severe features', ['L&D', 'ID', 'Aminoglycosides', 'Renal'],
  'On magnesium 2 g/h for 10 hours. Now temperature 39 °C, fetal tachycardia: intraamniotic infection. Urine output 20 mL/h for 3 hours, SCr up from 0.6 to 1.3. Weight 90 kg. No allergies.',
  [S('Before any antibiotic, what do you do about the magnesium?',
     [O('Check reflexes, breathing and a serum magnesium level now; ask the team to lower the rate (label: 1 g/h maintenance in severe renal impairment or oliguria, max 20 g per 48 h)', True, 'Low urine output means magnesium is building up.'),
      O('Nothing, magnesium does not depend on the kidneys', False, 'Magnesium is cleared by the kidneys.')],
     kind='Renal'),
   S('Antibiotics for intraamniotic infection?',
     [O('Ampicillin 2 g IV every 6 hours plus gentamicin', True, 'ACOG CO 712.'),
      O('Vancomycin alone', False, 'Misses gram negatives.')],
     kind='Regimen'),
   S('How do falling kidney function and magnesium change your gentamicin thinking?',
     [O('Kidney function is changing, so avoid assuming normal clearance: use levels and dose by kinetics; and know magnesium plus aminoglycosides both cause neuromuscular blockade', True, 'Gentamicin label warns about neuromuscular blockade with other blocking drugs. Watch breathing closely.'),
      O('Give 7 mg/kg by the Hartford nomogram', False, 'Pregnancy and unstable kidney function are Hartford exclusions.')],
     kind='Top 10%')],
  call='**S/B:** On magnesium 2 g/h, new intraamniotic infection, urine 20 mL/h, SCr 0.6 to 1.3. **A:** Magnesium is accumulating, and gentamicin adds kidney and neuromuscular risk. **R:** Magnesium level and reflex check now, lower magnesium to 1 g/h per label, start ampicillin 2 g q6h plus gentamicin with levels guided dosing, and I will follow her kidney function.',
  pearl='**One patient, three risks: magnesium build up, aminoglycoside kidney injury, and stacked neuromuscular blockade.**',
  sources=[MG, CO712, GENT, LOCAL]),

C('mx02', 'Septic shock with failing kidneys', 'ICU · 2300 · new admission', ['Sepsis', 'Vancomycin', 'Renal', 'ICU'],
  'Septic shock from a pneumonia, 80 kg, CrCl 25 mL/min. Norepinephrine 0.3 mcg/kg/min for 5 hours. Orders: vancomycin 1,000 mg, cefepime 2 g every 8 hours, pantoprazole.',
  [S('Vancomycin first dose?',
     [O('Load 20 to 35 mg/kg actual weight (for example 2,000 mg), not reduced for kidneys; then choose maintenance by kidneys and levels', True, ''),
      O('1,000 mg because of the kidneys', False, 'Underdosed load.')],
     kind='Load'),
   S('Cefepime?',
     [O('Give the full first dose now, then adjust maintenance for CrCl 25 to avoid neurotoxicity', True, 'FDA alert: neurotoxicity mostly with kidney impairment and no adjustment.'),
      O('2 g every 8 hours continued', False, 'Accumulates.')],
     kind='Renal'),
   S('Other bundle items?',
     [O('Hydrocortisone 200 mg/day (pressor 0.25 or more for over 4 hours)', True, ''),
      O('Add vasopressin rather than raising norepinephrine', True, ''),
      O('Stress ulcer prophylaxis is indicated (shock)', True, ''),
      O('Tight glucose 80 to 110', False, '140 to 180.')],
     multi=True, kind='Bundle')],
  pearl='**Septic shock + bad kidneys: full loads, adjust maintenance, steroids, vasopressin, SUP.**',
  sources=[SSC, RYBAK, CEFEPIME, SUP]),

C('mx03', 'The fall, the bleed, and what comes next', 'ED to neuro ICU · elderly woman', ['Stroke', 'Anticoagulation', 'Safety'],
  '84 years old, 58 kg, fell at home. ICH on CT. Apixaban 5 mg BID for AF (SCr 1.6). SBP 188.',
  [S('Reversal and BP?',
     [O('4F-PCC per protocol, SBP target about 140 (not below 130)', True, ''),
      O('Vitamin K and SBP below 110', False, ''),
      O('Andexanet', False, 'Withdrawn from the US market in 2025.')],
     kind='Acute'),
   S('Looking back at her home dose, what do you notice?',
     [O('She meets 3 of 3 apixaban reduction criteria (age 80+, weight 60 kg or less, SCr 1.5+), so her dose should have been 2.5 mg BID', True, 'An overdose contributed to bleeding risk. Report it and fix it before any restart.'),
      O('Her dose was correct', False, 'Check the criteria.')],
     kind='Top 10%'),
   S('When can VTE prophylaxis start?',
     [O('Heparin or enoxaparin prophylaxis is reasonable 24 to 48 hours after the bleed is stable', True, 'ICH 2022.'),
      O('Never', False, 'Immobile patients clot.')],
     kind='Later')],
  pearl='**Reverse, control BP, then find the error that set it up (wrong apixaban dose).**',
  sources=[ICH, KCEN, ELIQ, LOCAL]),

C('mx04', 'Crush injury, day 3', 'Trauma ICU · 0400', ['Trauma', 'Electrolytes', 'Airway', 'Aminoglycosides'],
  'Crush injury 3 days ago. CK 48,000, K 6.8 with peaked T waves, urine output falling. On gentamicin for an open fracture. Now needs reintubation.',
  [S('Hyperkalemia plan?',
     [O('Calcium first, then insulin and dextrose (consider 5 units with kidney injury), then remove potassium (binder, dialysis)', True, ''),
      O('Calcium lowers potassium, so that is enough', False, 'Calcium only protects the heart.')],
     kind='Electrolytes'),
   S('Paralytic for the reintubation?',
     [O('Rocuronium; avoid succinylcholine (crush injury after 24 to 48 hours and K 6.8)', True, 'Succinylcholine can cause a hyperkalemic arrest.'),
      O('Succinylcholine', False, 'Dangerous here.')],
     kind='Airway'),
   S('What about the gentamicin?',
     [O('Rhabdomyolysis and falling urine output: ask whether a non nephrotoxic option covers the fracture, and check levels if it continues', True, 'Stacked kidney risks.'),
      O('Continue without change', False, '')],
     kind='Top 10%')],
  pearl='**Crush day 3: no succinylcholine, treat K in 3 steps, and rethink nephrotoxins.**',
  sources=[KDIGO, GENT, LOCAL]),

C('mx05', 'DKA with pneumonia', 'ICU · new DKA and fever', ['DKA', 'ID', 'Electrolytes', 'QT'],
  'DKA, K 3.1, Mg 1.4, QTc 510. Chest X ray: lobar pneumonia, not severe. Orders: insulin drip, ceftriaxone, azithromycin, ondansetron.',
  [S('Insulin first?',
     [O('No: replace potassium to 3.5 or more before insulin (2024 consensus); replace magnesium too', True, ''),
      O('Yes', False, '')],
     kind='DKA'),
   S('What is the hidden danger in this order set?',
     [O('QTc 510 with low K and low Mg, plus azithromycin and ondansetron (both prolong QT): torsades risk', True, 'Fix electrolytes and consider a non QT prolonging plan.'),
      O('None', False, '')],
     kind='Top 10%'),
   S('Which CAP option avoids adding QT risk?',
     [O('Ceftriaxone plus doxycycline (the ATS/IDSA alternative when a macrolide should be avoided)', True, 'Fluoroquinolones also prolong QT.'),
      O('Levofloxacin alone', False, 'Also prolongs QT.')],
     kind='Alternative')],
  pearl='**Low K, low Mg, long QT: fix electrolytes, then choose drugs that do not stack QT.**',
  sources=[DKA, CAP, LOCAL]),

C('mx06', 'Postpartum clot while breastfeeding', 'Postpartum unit · day 4', ['L&D', 'Anticoagulation', 'Lactation'],
  'Day 4 after cesarean, new PE. Breastfeeding. BP 158/98 on two readings. Pain orders include acetaminophen with codeine.',
  [S('Which anticoagulants are compatible with breastfeeding?',
     [O('Enoxaparin', True, 'Large molecule, minimal milk transfer, not orally absorbed by the infant.'),
      O('Warfarin', True, 'Compatible per LactMed.'),
      O('Apixaban', False, 'Labels advise against breastfeeding on DOACs (limited data).')],
     multi=True, kind='Anticoagulant'),
   S('BP agent while breastfeeding?',
     [O('Labetalol, nifedipine ER or enalapril', True, 'The pregnancy ban on ACE inhibitors ends at delivery.'),
      O('Lisinopril is contraindicated because she was pregnant', False, 'Not after delivery; enalapril is the studied option.')],
     kind='BP'),
   S('And the codeine?',
     [O('Avoid codeine (and tramadol) while breastfeeding; use scheduled acetaminophen and ibuprofen, short low dose oxycodone if needed', True, 'FDA 2017.'),
      O('Fine', False, '')],
     kind='Pain')],
  pearl='**Breastfeeding: enoxaparin or warfarin, labetalol or nifedipine or enalapril, no codeine.**',
  sources=[LACT, ELIQ, ACC, FDACOD]),

C('mx07', 'Warfarin bleed in a patient with HIT history', 'ED · GI bleed', ['Anticoagulation', 'Reversal', 'HIT'],
  'GI bleed, INR 6.8 on warfarin. Allergy list: "heparin: HIT 2023."',
  [S('Can you give Kcentra (4F-PCC)?',
     [O('No: Kcentra contains heparin and is contraindicated with known HIT', True, 'Kcentra label.'),
      O('Yes', False, 'Check the contraindication.')],
     kind='Catch'),
   S('What do you recommend instead?',
     [O('Vitamin K 10 mg IV plus plasma (FFP), with the team weighing volume, or a heparin free factor product if St. Mary\'s stocks one', True, 'Check what is on formulary.'),
      O('Nothing; wait for vitamin K', False, 'Active bleed.')],
     kind='Alternative'),
   S('Which other heparin exposures do you block for this patient?',
     [O('Heparin flushes and heparin coated catheters', True, 'ASH 2018.'),
      O('Enoxaparin', True, 'Cross reacts.'),
      O('Nothing else', False, '')],
     multi=True, kind='Prevent')],
  pearl='**HIT history: no Kcentra, no heparin flushes, no enoxaparin.**',
  sources=[KCEN, ASH, LOCAL]),

C('mx08', 'Falling platelets on day 15', 'Med surg · VRE infection', ['ID', 'HIT', 'Interactions'],
  'Day 15 of linezolid. On sertraline and heparin 5,000 units SC q8h since admission. Platelets 210,000 to 95,000. No new clot.',
  [S('What are the leading causes?',
     [O('Linezolid myelosuppression (usually after about 2 weeks)', True, ''),
      O('HIT is possible, but the timing (day 15) and another clear cause lower the 4Ts score', True, 'The 4Ts includes "other causes."'),
      O('Lab error only', False, '')],
     multi=True, kind='Differential'),
   S('What else about linezolid and sertraline?',
     [O('Serotonin syndrome risk: monitor and discuss', True, ''),
      O('No interaction', False, '')],
     kind='Interaction'),
   S('Next step?',
     [O('Calculate the 4Ts with the team, consider HIT testing if intermediate, and ask ID about an alternative to linezolid', True, ''),
      O('Transfuse platelets', False, 'Not routine.')],
     kind='Plan')],
  pearl='**Low platelets: list every cause (drug, HIT, sepsis). Linezolid after 2 weeks is a classic.**',
  sources=[DM, ASH, LOCAL]),
]

if __name__ == '__main__':
    write(sys.argv[1], 'm15', 'Module 15 · Mixed Patients (Top 10%)',
          'Real patients cross modules. Each case stacks problems the way a night shift does: magnesium plus infection plus kidneys, sepsis plus renal dosing, a bleed caused by a dosing error, crush injury, DKA with QT risk, postpartum clots while breastfeeding, HIT history and falling platelets.', CASES)

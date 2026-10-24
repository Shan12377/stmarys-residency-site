# Per case "full workup": the drug cards to show, this patient's own math, and case specific what ifs.
W = {
'ld07': {'drugs': ['magnesium_ob'],
  'calc': 'Order: 6 g over 20 min, then 2 g/h. **Approved?** Yes: load 4 to 6 g, maintenance 1 to 2 g/h ✅✅. **Weight based?** No, fixed grams.\nWith a 40 mg/mL bag: load 150 mL at 450 mL/h for 20 min; maintenance 50 mL/h.\n**Kidneys:** SCr 0.7, urine 60 mL/h (240 mL per 4 h, above the 100 mL per 4 h goal) so full maintenance is reasonable.\n**Reflexes 2+:** normal baseline to compare against.\n**Rate:** 6 g over 20 min = 300 mg/min, the accepted obstetric exception to the 150 mg/min general limit.',
  'whatif': [('Urine output 15 mL/h?', 'Give the load, then lower or hold maintenance (label 1 g/h in oliguria), level in a few hours, hourly reflexes and breathing, call OB now.'),
             ('She also needs nifedipine for BP?', 'Allowed by ACOG with close BP and reflex monitoring; the label warns about the combination.'),
             ('She has myasthenia gravis?', 'Do not give magnesium; work with OB and neurology on an alternative such as levetiracetam or a benzodiazepine.'),
             ('IV infiltrates mid load?', 'Restart IV; if delayed, IM 5 g each buttock.')]},
'ld08': {'drugs': ['magnesium_ob'],
  'calc': 'Absent reflexes + RR 11 + urine 15 mL/h for 2 h (30 mL in 2 h, well below 50 mL per 2 h): accumulation. **Antidote:** calcium gluconate 1 g = 10 mL of 10% over 2 to 3 min. Expect a level above about 7 to 10 mEq/L.',
  'whatif': [('Breathing stops?', 'Bag mask ventilation, call anesthesia and the rapid response or code team, repeat calcium as directed.'),
             ('Level comes back 5 mEq/L and reflexes return?', 'Restart only if seizure prophylaxis is still needed, at a lower rate, with frequent levels.')]},
'ld09': {'drugs': ['magnesium_ob'],
  'calc': 'SCr 1.9 and urine 20 mL/h. **Label for severe renal impairment:** 4 g load, then 1 g/h, max 20 g per 48 h, frequent levels. With a 40 mg/mL bag: load 100 mL; maintenance 25 mL/h.',
  'whatif': [('Urine output drops to 10 mL/h?', 'Hold maintenance, level now, call OB; consider an alternative anticonvulsant if renal failure is established.'),
             ('Level 2.0 mEq/L at 6 hours?', 'Below the label target; the team may raise the rate cautiously with repeat levels.')]},
'ld10': {'drugs': ['magnesium_ob'],
  'calc': 'Seizure on 2 g/h: extra **2 to 4 g IV over 5 minutes** (400 to 800 mg/min, the eclampsia exception). With 40 mg/mL: 50 to 100 mL over 5 minutes (600 to 1,200 mL/h). Check reflexes and level before more.',
  'whatif': [('Still seizing after the extra magnesium?', 'Lorazepam 2 to 4 mg IV (ACOG checklist), airway support, check level.')]},
'ld11': {'drugs': ['magnesium_ob'],
  'calc': 'Myasthenia gravis is a **label contraindication**: magnesium blocks the neuromuscular junction and can trigger respiratory failure.',
  'whatif': [('Then what for seizure prevention?', 'Team decision with neurology. ACOG checklist alternatives: levetiracetam 500 mg IV or PO (repeat in 12 h), lorazepam, diazepam or phenytoin. Note: phenytoin can also worsen myasthenia, so levetiracetam is often favored ⚠️.')]},
'ld12': {'drugs': ['magnesium_ob'],
  'calc': 'Neuroprotection protocol: 6 g over 20 to 30 min (with 40 mg/mL: 150 mL at 300 to 450 mL/h), then 2 g/h (50 mL/h) up to 12 hours or until delivery ✅.',
  'whatif': [('Delivery does not happen within 12 hours?', 'Stop; most protocols allow a repeat course only if delivery again looks imminent ⚠️ [VERIFY protocol].')]},
'ld13': {'drugs': ['magnesium_ob'], 'calc': 'Day 6 of continuous magnesium: past the 5 to 7 day label warning (fetal low calcium, bone problems). Ask the goal: magnesium is not recommended as a long term tocolytic.', 'whatif': []},
'ld39': {'drugs': ['magnesium_ob'], 'calc': 'IV magnesium raises milk levels only slightly and is poorly absorbed by the infant: compatible ✅ LactMed.', 'whatif': []},
'ld40': {'drugs': ['magnesium_ob'], 'calc': 'Absent reflexes + RR 10 = toxicity: stop the drip and give calcium gluconate 1 g first, before anything else on your list.', 'whatif': []},
'ld04': {'drugs': ['magnesium_ob'], 'calc': 'Nifedipine IR 10 mg PO, recheck 20 min, then 20 mg, recheck 20 min, then 20 mg; she is on magnesium, so watch BP and reflexes closely.', 'whatif': []},
'mx01': {'drugs': ['magnesium_ob'], 'calc': 'Urine 20 mL/h x 3 h (60 mL in 3 h, goal 75 mL) and SCr doubled: lower to 1 g/h per label, level now. Gentamicin adds kidney and neuromuscular risk.', 'whatif': []},
}

# Drug cards for the remaining L&D cases (cases above keep their own math).
LINK = {
 'ld01': ['labetalol_ob', 'hydralazine_ob', 'nifedipine_ob'], 'ld02': ['labetalol_ob', 'hydralazine_ob'], 'ld03': ['hydralazine_ob', 'labetalol_ob'],
 'ld04': ['nifedipine_ob'], 'ld05': ['ace_pregnancy', 'labetalol_ob', 'nifedipine_ob'], 'ld06': ['labetalol_ob', 'nifedipine_ob', 'ace_pregnancy'],
 'ld14': ['oxytocin'], 'ld15': ['oxytocin'], 'ld16': ['methylergonovine', 'carboprost', 'misoprostol_ob', 'txa_pph'], 'ld17': ['carboprost', 'misoprostol_ob'],
 'ld18': ['misoprostol_ob', 'txa_pph'], 'ld19': ['txa_pph'], 'ld20': ['txa_pph'], 'ld21': ['gbs_abx'], 'ld22': ['gbs_abx'], 'ld23': ['gbs_abx'], 'ld24': ['gbs_abx'],
 'ld25': ['chorio_abx'], 'ld26': ['chorio_abx'], 'ld27': ['antenatal_steroids'], 'ld28': ['antenatal_steroids', 'gdm_insulin'], 'ld29': ['indomethacin_toco', 'nsaid_pregnancy'],
 'ld30': ['rhig'], 'ld31': ['aspirin_ldp'], 'ld32': ['misoprostol_ob'], 'ld33': ['enox_neuraxial'], 'ld34': ['gdm_insulin'], 'ld35': ['nsaid_pregnancy', 'aspirin_ldp'],
 'ld36': ['ob_pain_lactation'], 'ld37': ['ob_pain_lactation'], 'ld38': ['statin_preg'], 'ld40': ['magnesium_ob', 'gbs_abx'],
 'mx06': ['ob_pain_lactation', 'ace_pregnancy', 'labetalol_ob'], 'mx01': ['magnesium_ob', 'chorio_abx'],
}
CALC = {
 'ld02': 'Labetalol so far: 20 + 40 + 80 = **140 mg** in about 30 minutes, BP still severe: switch class (hydralazine 10 mg IV) rather than giving more labetalol. The injection label caps cumulative repeated doses at 300 mg ⚠️.',
 'ld14': 'Tachysystole: more than 5 contractions in 10 minutes. With a 30 units/500 mL bag (60 milliunits/mL), mL/h equals milliunits/min: a rate of 12 mL/h = 12 milliunits/min.',
 'ld19': 'Bleeding started 2 hours after birth: inside the 3 hour window. 1 g in 100 mL over 10 minutes = 600 mL/h for 10 minutes; second 1 g if bleeding continues after 30 minutes.',
 'ld24': 'Vancomycin 20 mg/kg x 72 kg = 1,440 mg (round per protocol, for example 1,500 mg), every 8 hours, max 2 g per dose. Label rate (10 mg/min or slower): at least 150 minutes.',
 'ld25': 'Gentamicin for 80 kg: 2 mg/kg load = **160 mg**, then 1.5 mg/kg = **120 mg every 8 hours**; or 5 mg/kg = **400 mg every 24 hours**. Ampicillin 2 g every 6 hours.',
 'ld27': 'Betamethasone 12 mg IM now and 12 mg IM in 24 hours. Fixed dose, not weight based.',
 'ld30': 'Delivered 20 hours ago: inside 72 hours. One 300 mcg vial covers about 30 mL fetal whole blood; order a screen for larger bleeds.',
}
for cid, drugs in LINK.items():
    W.setdefault(cid, {'drugs': [], 'calc': '', 'whatif': []})
    for d in drugs:
        if d not in W[cid]['drugs']: W[cid]['drugs'].append(d)
    if cid in CALC and not W[cid].get('calc'): W[cid]['calc'] = CALC[cid]

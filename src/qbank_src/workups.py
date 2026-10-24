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

LINK2 = {c: ['vancomycin'] for c in 'pk01 pk02 pk03 pk04 pk05 pk06 pk07 pk08 pk09 pk10 pk11 pk12'.split()}
LINK2.update({c: ['aminoglycoside'] for c in 'pk13 pk14 pk15 pk16 pk17 pk18'.split()})
LINK2['pk19'] = ['vancomycin', 'aminoglycoside']; LINK2['ld24'] = ['gbs_abx', 'vancomycin']; LINK2['ld25'] = ['chorio_abx', 'aminoglycoside']
LINK2['mx01'] = ['magnesium_ob', 'chorio_abx', 'aminoglycoside']; LINK2['mx02'] = ['vancomycin']; LINK2['mx04'] = ['aminoglycoside']
CALC2 = {
 'pk02': 'Load for 80 kg: 20 to 25 mg/kg = 1,600 to 2,000 mg (guideline range 20 to 35, max 3,000). 2,000 mg at 10 mg/min = 200 minutes minimum by label.',
 'pk03': 'CrCl = (140 minus 58) x 72 / (72 x 1.0) = **82 mL/min**. 1,250 mg every 12 hours = 17.4 mg/kg per dose: inside 15 to 20 mg/kg.',
 'pk08': '20 mg/kg x 160 kg = 3,200 mg, so the 3,000 mg cap applies. Maintenance usually 4,500 mg/day or less to start, then AUC.',
 'pk09': '25 mg/kg x 70 kg = **1,750 mg** after dialysis; then 10 mg/kg = **700 mg** after each session (high permeability).',
 'pk10': 'Load 15 to 20 mg/kg x 75 = 1,125 to 1,500 mg; maintenance 30 to 40 mg/kg/day = 2,250 to 3,000 mg/day. AUC24 = level x 24 = 22 x 24 = **528**.',
 'pk11': '60 mg/kg/day x 20 kg = 1,200 mg/day = **300 mg every 6 hours**; 80 mg/kg/day = 400 mg every 6 hours.',
 'pk14': 'IBW = 50 + 2.3 x 10 = 73 kg; 110 / 73 = 151% so use adjusted: 73 + 0.4 x 37 = **87.8 kg**; 7 x 87.8 = **615 mg**.',
 'pk16': 'ke = ln(7 / 1.2) / 7 h = 0.252 per hour; half life = 0.693 / 0.252 = **2.75 hours**.',
 'pk17': 'Synergy for 70 kg: about 1 mg/kg = 70 mg every 8 hours; peak goal 3 to 4, trough below 1.',
}
for cid, drugs in LINK2.items():
    W.setdefault(cid, {'drugs': [], 'calc': '', 'whatif': []})
    for d in drugs:
        if d not in W[cid]['drugs']: W[cid]['drugs'].append(d)
    if cid in CALC2 and not W[cid].get('calc'): W[cid]['calc'] = CALC2[cid]

LINK3 = {'ac01': ['doacs'], 'ac02': ['doacs'], 'ac03': ['doacs'], 'ac04': ['doacs'], 'ac05': ['doacs', 'warfarin'], 'ac06': ['doacs'],
 'ac07': ['warfarin'], 'ac08': ['warfarin', 'kcentra'], 'ac09': ['kcentra', 'doacs'], 'ac10': ['heparin_ufh'], 'ac11': ['heparin_ufh', 'argatroban', 'warfarin'],
 'ac12': ['enoxaparin'], 'ac13': ['doacs'], 'ac14': ['warfarin', 'enoxaparin'], 'ac15': ['heparin_ufh', 'doacs'], 'ac16': ['heparin_ufh', 'doacs'],
 'st04': ['doacs', 'warfarin'], 'st08': ['kcentra', 'doacs'], 'st09': ['kcentra', 'warfarin', 'heparin_ufh'], 'tr04': ['kcentra', 'doacs'],
 'mx03': ['kcentra', 'doacs'], 'mx07': ['kcentra', 'warfarin', 'heparin_ufh'], 'mx08': ['heparin_ufh'], 'ld33': ['enox_neuraxial', 'enoxaparin'], 'mx06': ['enoxaparin', 'warfarin', 'doacs']}
CALC3 = {
 'ac01': 'Age 82 (meets 1), weight 64 kg (not 60 or less), SCr 1.2 (not 1.5 or more): **1 of 3** so **5 mg BID**.',
 'ac08': 'INR 5.4 is in the 4 to 6 band: 35 units/kg x 70 kg = **2,450 units** (under the 3,500 cap) + vitamin K 10 mg IV.',
 'ac10': '80 units/kg x 90 kg = **7,200 units** bolus; 18 units/kg/h x 90 = **1,620 units/h**. With 25,000 units in 250 mL (100 units/mL, check bag ⚠️): 16.2 mL/h.',
 'ac11': 'Platelets 260,000 to 110,000 = **58% fall**, day 7, new DVT: 4Ts intermediate to high. Argatroban 2 mcg/kg/min (no hepatic impairment).',
 'ac12': 'CrCl 24: 1 mg/kg x 75 kg = **75 mg every 24 hours** (not every 12).',
 'ac13': 'Surgery Friday, high bleed risk: no apixaban Wednesday or Thursday or Friday morning; Tuesday is the last dosing day (about 60 to 68 hours off).',
 'st08': '50 units/kg x 80 kg = **4,000 units** 4F-PCC (or St. Mary\'s fixed dose).',
 'st09': 'A: INR 3.1 (2 to below 4): 25 units/kg x 90 = **2,250 units** + vitamin K 10 mg IV. B: 1,400 units/h x 3 h = 4,200 units: protamine **42 mg** (max 50), slowly.',
 'mx03': 'Age 84, weight 58 kg, SCr 1.6: **3 of 3** reduction criteria: her home dose should have been 2.5 mg BID.',
}
for cid, drugs in LINK3.items():
    W.setdefault(cid, {'drugs': [], 'calc': '', 'whatif': []})
    for d in drugs:
        if d not in W[cid]['drugs']: W[cid]['drugs'].append(d)
    if cid in CALC3 and not W[cid].get('calc'): W[cid]['calc'] = CALC3[cid]

LINK4 = {'id01': ['betalactams', 'vancomycin'], 'id02': ['betalactams'], 'id03': ['abx_syndromes', 'betalactams'], 'id04': ['vancomycin', 'abx_syndromes'],
 'id05': ['abx_syndromes', 'betalactams'], 'id06': ['betalactams'], 'id07': ['abx_syndromes'], 'id08': ['abx_syndromes'], 'id09': ['abx_syndromes'],
 'id10': ['abx_syndromes', 'betalactams', 'vancomycin'], 'id11': ['abx_syndromes', 'betalactams', 'vancomycin'], 'id12': ['betalactams'], 'id13': ['betalactams'],
 'id14': ['betalactams'], 'id15': ['abx_syndromes'], 'id16': ['abx_syndromes', 'betalactams'],
 'cc01': ['pressors'], 'cc02': ['pressors'], 'cc03': ['sedation_icu'], 'cc04': ['sedation_icu'], 'cc05': ['hyperk'], 'cc06': ['hyponatremia_tx'],
 'cc07': ['icu_glucose'], 'cc08': ['dka_insulin', 'kcl_iv'], 'cc09': ['kcl_iv'], 'cc10': ['sup'], 'cc11': ['hyperk', 'pressors'],
 'cd01': ['acls_drugs'], 'cd02': ['acls_drugs'], 'cd03': ['acls_drugs', 'hyperk'], 'cd04': ['acls_drugs'], 'cd05': ['acls_drugs'], 'cd06': ['acls_drugs'],
 'cd07': ['acls_drugs'], 'cd08': ['acls_drugs'], 'cd09': ['acls_drugs'], 'cd10': ['acls_drugs'], 'cd11': ['acls_drugs'], 'cd12': ['acls_drugs', 'pressors'],
 'mx02': ['vancomycin', 'betalactams', 'pressors', 'sup'], 'mx04': ['hyperk', 'aminoglycoside'], 'mx05': ['dka_insulin', 'kcl_iv', 'abx_syndromes'],
 'mx08': ['linezolid', 'heparin_ufh'], 'po07': ['linezolid'], 'ld40': ['magnesium_ob', 'gbs_abx']}
CALC4 = {
 'cc05': 'K 7.1 with peaked T waves = severe. Calcium gluconate 1 g now; regular insulin **5 units** (CrCl 15) + dextrose 25 g; glucose hourly x 4 to 6 h; binder and dialysis.',
 'cc06': '3% saline 100 to 150 mL over 10 to 20 min, up to about 3 times. Na 112: aim for about 116 to 118 in the first hours; no more than about 122 at 24 hours (10 per 24 h), 120 if high risk (8 per 24 h).',
 'cc08': 'K 3.2: hold insulin, replace potassium. Then 0.1 units/kg/h x 70 kg = **7 units/h**; at glucose below 250: 0.05 units/kg/h = **3.5 units/h** plus dextrose.',
 'cc09': '40 mEq at the 10 mEq/h peripheral limit = **4 hours**, not 1. Replace Mg 1.3 as well.',
 'cd05': 'Naloxone 0.4 mg IV, repeat every 2 to 3 minutes as needed; 4 mg intranasal if no IV.',
 'cd06': 'Lipid 20%: 1.5 mL/kg x 70 kg = **105 mL** over 2 to 3 min, then 0.25 mL/kg/min = **17.5 mL/min**.',
 'cd07': 'Bicarbonate 1 to 2 mEq/kg (for 70 kg, 70 to 140 mEq = 1.4 to 2.8 ampules of 50 mEq), repeat to narrow QRS.',
 'cd11': 'Example for an 80 kg adult: dantrolene 2.5 mg/kg = **200 mg** IV, repeat until signs resolve.',
}
for cid, drugs in LINK4.items():
    W.setdefault(cid, {'drugs': [], 'calc': '', 'whatif': []})
    for d in drugs:
        if d not in W[cid]['drugs']: W[cid]['drugs'].append(d)
    if cid in CALC4 and not W[cid].get('calc'): W[cid]['calc'] = CALC4[cid]

import json as _j, os as _o
_SRC = {'m00': 'verify_basics', 'm03': 'usp797', 'm04': 'iv_po', 'm09': 'thrombolytics', 'm10': 'trauma_drugs', 'm11': 'neonatal', 'm12': 'peds', 'm13': 'safety', 'm14': 'evidence'}
_IDS = {'m00': 'h', 'm03': 'iv', 'm04': 'po', 'm09': 'st', 'm10': 'tr', 'm11': 'nc', 'm12': 'pi', 'm13': 'ms', 'm14': 'pa'}
def _link(cid, d):
    W.setdefault(cid, {'drugs': [], 'calc': '', 'whatif': []})
    if d not in W[cid]['drugs']: W[cid]['drugs'].append(d)
for m, pre in _IDS.items():
    for n in range(1, 41):
        _link(f'{pre}{n:02d}', _SRC[m])
_link('st10', 'nimodipine'); _link('iv14', 'kcl_iv'); _link('mx03', 'thrombolytics'); _link('mx04', 'trauma_drugs'); _link('tr10', 'trauma_drugs')
CALC5 = {
 'h02': '(140 minus 70) x 80 / (72 x 1.6) = 5,600 / 115.2 = **48.6 mL/min**.',
 'st02': '0.25 mg/kg x 82 kg = **20.5 mg** = 4.1 mL of 5 mg/mL, over 5 seconds, saline flush.',
 'st03': '0.9 x 70 = **63 mg** total; bolus 6.3 mg over 1 minute; 56.7 mg over 60 minutes; waste 37 mg from a 100 mg vial before hanging.',
 'tr03': 'Ketamine 1 to 2 mg/kg x 85 = 85 to 170 mg; etomidate 0.3 x 85 = 25.5 mg; rocuronium 1 to 1.2 x 85 = 85 to 102 mg.',
 'tr05': 'Mannitol 0.25 to 1 g/kg x 80 = 20 to 80 g (20% = 100 to 400 mL).',
 'tr09': '4 x 80 x 40 = **12,800 mL**; half = 6,400 mL by hour 8 from the burn; 2 hours gone, so 6,400 mL over 6 hours = **1,067 mL/h**, then 6,400 mL over 16 hours = 400 mL/h.',
 'nc03': '0.02 mg/kg x 3 kg = 0.06 mg = **0.6 mL** of 0.1 mg/mL IV; ETT would be 0.1 x 3 = 0.3 mg = 3 mL. Saline 10 mL/kg = 30 mL.',
 'nc07': '1.1 kg: load 20 mg/kg = 22 mg; maintenance 5 mg/kg = 5.5 mg daily (caffeine citrate).',
 'nc09': 'D10W 2 mL/kg x 3.2 kg = **6.4 mL** (640 mg dextrose = 200 mg/kg).',
 'pi02': '20 kg: epinephrine 0.01 x 20 = 0.2 mg = **2 mL** of 0.1 mg/mL; amiodarone 5 x 20 = **100 mg**.',
 'pi03': 'Adenosine 0.1 x 15 = 1.5 mg, then 0.2 x 15 = 3 mg. Atropine 0.02 x 10 = 0.2 mg.',
 'pi04': '25 kg: lorazepam 0.1 x 25 = 2.5 mg; levetiracetam 60 x 25 = 1,500 mg; fosphenytoin 20 x 25 = 500 mg PE; valproate 40 x 25 = 1,000 mg.',
 'pi05': '30 kg: insulin 0.05 to 0.1 units/kg/h = 1.5 to 3 units/h; mannitol 0.5 to 1 g/kg = 15 to 30 g; 3% saline 2.5 to 5 mL/kg = 75 to 150 mL.',
 'pi08': '20 kg: 4/2/1 = 40 + 20 = **60 mL/h**; acetaminophen 300 mg; ibuprofen 200 mg.',
 'pa04': 'ARI = 27.5 minus 24.9 = 2.6 points; NNH = 1 / 0.026 = **38**.',
 'pa05': 'ARR = 8.8 minus 1.7 = 7.1; NNT = 1 / 0.071 = **14**. BRIDGE: 3.2 minus 1.3 = 1.9; NNH = **53**.',
}
for cid, t in CALC5.items():
    if cid in W and not W[cid].get('calc'): W[cid]['calc'] = t

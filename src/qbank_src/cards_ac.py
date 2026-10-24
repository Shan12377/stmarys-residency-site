# Anticoagulant and reversal drug cards.
def card(title, sections, sources): return {'title': title, 'sections': sections, 'sources': sources}
def s(t, url, mark='✅'): return {'t': t, 'url': url, 'mark': mark}
ELIQ = s('Eliquis (apixaban) prescribing information, Pfizer', 'https://labeling.pfizer.com/ShowLabeling.aspx?id=14028', '✅✅')
XAR = s('Xarelto (rivaroxaban) prescribing information, DailyMed', 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=xarelto')
PRAD = s('Pradaxa (dabigatran) prescribing information (HemOnc)', 'https://hemonc.org/docs/packageinsert/dabigatran.pdf')
SAV = s('Savaysa (edoxaban) prescribing information, DailyMed', 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=savaysa')
CHEST21 = s('CHEST 2021 VTE guideline update. Chest 2021;160:e545-e608', 'https://doi.org/10.1016/j.chest.2021.07.055')
CHEST22 = s('CHEST 2022 perioperative antithrombotic guideline. Chest 2022;162:e207-e243', 'https://doi.org/10.1016/j.chest.2022.07.025')
PAUSE = s('PAUSE. JAMA Intern Med 2019;179:1469-1478', 'https://doi.org/10.1001/jamainternmed.2019.2431')
CROW = s('Crowther 2009, oral vitamin K vs placebo. Ann Intern Med 2009;150:293-300', 'https://doi.org/10.7326/0003-4819-150-5-200903030-00005')
SUNNY = s('Sunnybrook: reversal of warfarin over anticoagulation (vitamin K)', 'https://sunnybrook.ca/uploads/Reversal_of_Warfarin_Over-Anitcoagulation_-_Focus_on_Vitamin_K.pdf')
KCEN = s('Kcentra prescribing information, DailyMed', 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=kcentra')
ICH = s('2022 AHA/ASA spontaneous ICH guideline. Stroke 2022;53:e282-e361', 'https://doi.org/10.1161/STR.0000000000000407', '✅✅')
TCTMD = s('TCTMD: andexanet alfa pulled from US market (Dec 2025)', 'https://www.tctmd.com/news/andexanet-alfa-pulled-us-market')
RAS = s('Raschke 1993 weight based heparin nomogram. Ann Intern Med 1993;119:874-881', 'https://doi.org/10.7326/0003-4819-119-9-199311010-00002')
HEP = s('Heparin Sodium Injection prescribing information (DailyMed)', 'https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=45dc6b8b-ed5d-40a2-8d9c-084c863ae93a&type=display')
ASH = s('ASH 2018 HIT guideline. Blood Adv 2018;2:3360-3392', 'https://doi.org/10.1182/bloodadvances.2018024489')
ARGA = s('Argatroban prescribing information (2019)', 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/022485s013lbl.pdf')
LOV = s('Lovenox prescribing information, Sanofi (2025)', 'https://products.sanofi.us/lovenox/lovenox.pdf')
ASRA = s('ASRA 4th ed (2018); 5th ed 2025 doi 10.1136/rapm-2024-105766 to recheck', 'https://doi.org/10.1097/AAP.0000000000000763', '⚠️')
LOCAL = {'t': "St. Mary's anticoagulation and reversal order sets (verify locally)", 'url': '', 'mark': '⚠️'}

AC = {
'doacs': card('DOACs: apixaban, rivaroxaban, dabigatran, edoxaban', [
  ('How they work', 'Apixaban, rivaroxaban, edoxaban: direct factor Xa inhibitors. Dabigatran: direct thrombin inhibitor. No routine INR monitoring.'),
  ('Apixaban', '**AF:** 5 mg BID; 2.5 mg BID only with **2 of 3**: age 80+, weight 60 kg or less, SCr 1.5+. **VTE:** 10 mg BID x 7 days, then 5 mg BID; after 6 months, 2.5 mg BID for extended treatment (CHEST 2021). Tablets may be crushed (water, D5W, apple juice or applesauce, or NG tube) ✅✅ [label; CHEST 2021].'),
  ('Rivaroxaban', '**AF:** 20 mg daily with the evening meal; 15 mg if CrCl 15 to 50. **VTE:** 15 mg BID x 21 days, then 20 mg daily; 10 mg daily for extended treatment. **15 and 20 mg must be taken with food** ✅ [label].'),
  ('Dabigatran', '**AF:** 150 mg BID; 75 mg BID if CrCl 15 to 30. **VTE:** after 5 to 10 days of parenteral therapy, 150 mg BID. **Never open or crush** (exposure rises about 75%) ✅ [label].'),
  ('Edoxaban', '**AF:** 60 mg daily; 30 mg if CrCl 15 to 50; **do not use in AF with CrCl above 95** (less effective, boxed warning). **VTE:** after 5 to 10 days parenteral; 60 mg daily (30 mg if CrCl 15 to 50, weight 60 kg or less, or certain P-gp inhibitors) ✅ [label].'),
  ('Not for', 'Mechanical heart valves; high risk antiphospholipid syndrome (warfarin preferred); pregnancy (use LMWH); breastfeeding (labels advise against) ✅ [labels].'),
  ('Interactions', 'Avoid strong CYP3A4 and P-gp inducers (rifampin, carbamazepine, phenytoin, St. John\'s wort); caution with strong inhibitors. Never combine with another anticoagulant except during planned transitions.'),
  ('Switching', 'From a heparin infusion: start the DOAC when the infusion stops. From enoxaparin: start at the time the next enoxaparin dose would be due ✅ [labels].'),
  ('Around procedures (PAUSE)', 'Apixaban, rivaroxaban, edoxaban: low bleed risk, skip 1 day before; high bleed risk, skip 2 days before (plus the day of). Dabigatran longer when CrCl is below 50. No bridging. Restart 24 hours after low risk and 48 to 72 hours after high risk surgery ✅✅ [PAUSE; CHEST 2022].'),
  ('Epidurals', 'Classic ASRA: hold 72 hours (apixaban, rivaroxaban, edoxaban), 120 hours dabigatran; restart 6 hours after catheter removal ⚠️ [5th edition now uses renal based holds; recheck].'),
  ('Reversal', 'Factor Xa inhibitors: 4F-PCC (commonly 50 units/kg or a fixed dose per protocol); andexanet withdrawn from the US market in December 2025. Dabigatran: idarucizumab 5 g IV ✅✅ [ICH 2022; TCTMD].'),
], [ELIQ, XAR, PRAD, SAV, CHEST21, PAUSE, CHEST22, ASRA, ICH, TCTMD, LOCAL]),

'warfarin': card('Warfarin', [
  ('How it works', 'Blocks vitamin K recycling, so the liver cannot finish factors II, VII, IX, X (and proteins C and S). Full effect takes days; half life about 20 to 60 hours.'),
  ('When it is the right choice', 'Mechanical valves, high risk antiphospholipid syndrome, severe kidney disease in some settings, cost.'),
  ('INR high, no bleeding', 'INR 4.5 to 10: hold, recheck; routine vitamin K not needed (Crowther 2009). INR above 10: hold and give oral vitamin K 2.5 to 5 mg ✅✅ [Crowther; Sunnybrook].'),
  ('Major bleeding', 'Hold; vitamin K 10 mg IV (slow); 4F-PCC by INR ✅✅ [Kcentra label; Sunnybrook].'),
  ('Interactions (the big ones)', 'Raise INR: TMP SMX, metronidazole, fluconazole, fluoroquinolones, amiodarone. Lower INR: rifampin, carbamazepine. New illness and diet changes too.'),
  ('Around procedures', 'Stop about 5 days before. AF: do not bridge (CHEST 2022, BRIDGE). Very high risk (mechanical mitral valve, clot in last 3 months): bridging decided with cardiology or hematology ✅✅ [CHEST 2022].'),
  ('Pregnancy and lactation', 'Teratogenic (avoid in pregnancy except special cases); compatible with breastfeeding ✅ [LactMed].'),
  ('HIT', 'Never start warfarin alone in acute HIT; wait for platelets to recover (usually 150,000+) and overlap with a non heparin agent for at least 5 days ✅ [ASH 2018].'),
], [CROW, SUNNY, KCEN, CHEST22, ASH, LOCAL]),

'heparin_ufh': card('Unfractionated heparin', [
  ('How it works', 'Supercharges antithrombin to inactivate thrombin (IIa) and factor Xa.'),
  ('Dose', '**VTE:** 80 units/kg bolus, then 18 units/kg/h (Raschke). **ACS:** 60 units/kg (max 4,000) then 12 units/kg/h (max 1,000 units/h). **Prophylaxis:** 5,000 units SC every 8 to 12 hours ✅✅ [Raschke; label].'),
  ('Weight', 'Actual body weight in most nomograms; some cap the dosing weight ⚠️ [protocol].'),
  ('Monitoring', 'aPTT or anti Xa 6 hours after the bolus and after every rate change; platelets and hemoglobin at baseline and every 2 to 3 days (HIT).'),
  ('Kidneys', 'Not renally cleared: often preferred when CrCl is very low or dialysis.'),
  ('Safety', 'ISMP high alert; standard concentrations; never use benzyl alcohol preserved vials in neonates; read the concentration on every vial (look alike strengths).'),
  ('Reversal', 'Protamine 1 mg per 100 units given in the last 2 to 3 hours, maximum 50 mg, given slowly ✅ [ICH 2022].'),
  ('HIT', 'Platelet fall of 50% or more around day 5 to 10, or new clots: 4Ts; stop all heparin; start argatroban or another non heparin agent ✅ [ASH 2018].'),
], [RAS, HEP, ICH, ASH, LOCAL]),

'enoxaparin': card('Enoxaparin (LMWH)', [
  ('Dose', '**Prophylaxis:** 40 mg SC daily (30 mg every 12 hours in some ortho or trauma protocols). **Treatment:** 1 mg/kg every 12 hours, or 1.5 mg/kg daily for inpatient DVT or PE ✅ [label].'),
  ('Kidneys', 'CrCl below 30: treatment 1 mg/kg every 24 hours; prophylaxis 30 mg daily ✅ [label].'),
  ('Weight', 'Actual weight for treatment; extremes of weight, pregnancy and kidney disease are where anti Xa levels help (peak about 4 hours after a dose at steady state) ✅ [label; lab].'),
  ('Epidurals', 'Hold 12 hours (prophylaxis) or 24 hours (treatment) before placement or removal; next dose 4 hours after removal ✅ [label; ASRA] ⚠️ 5th edition.'),
  ('Reversal', 'Protamine partially reverses (about 60%): 1 mg per 1 mg enoxaparin within 8 hours; 0.5 mg per 1 mg if 8 to 12 hours ✅ [ICH 2022; label].'),
  ('HIT', 'Cross reacts with HIT antibodies: do not use in HIT.'),
  ('Pregnancy and lactation', 'Preferred anticoagulant in pregnancy; compatible with breastfeeding ✅ [LactMed].'),
], [LOV, ASRA, ICH, LOCAL]),

'kcentra': card('4F-PCC (Kcentra) and other reversal agents', [
  ('Warfarin dosing (label)', 'INR 2 to below 4: 25 units/kg (max 2,500). INR 4 to 6: 35 units/kg (max 3,500). INR above 6: 50 units/kg (max 5,000). Dosing weight capped at 100 kg. Always give **vitamin K 10 mg IV** too. Repeat dosing not studied ✅ [label].'),
  ('Factor Xa inhibitors', 'Off label, commonly 50 units/kg or a fixed dose per protocol ✅ [ICH 2022].'),
  ('Contraindications and boxed warning', 'Known HIT (contains heparin); DIC. Boxed warning: arterial and venous clots ✅ [label].'),
  ('Rate', 'Per label, slow IV infusion over minutes; check St. Mary\'s product instructions ⚠️.'),
  ('Other agents', 'Dabigatran: **idarucizumab 5 g IV** (two 2.5 g vials). Heparin: **protamine** (1 mg per 100 units in the last 2 to 3 hours, max 50 mg). Andexanet: withdrawn from the US in December 2025 ✅✅ [ICH 2022; TCTMD].'),
  ('If Kcentra is contraindicated (HIT history)', 'Vitamin K plus plasma (FFP), weighing volume, or another heparin free factor product if on formulary ⚠️ [St. Mary\'s].'),
], [KCEN, ICH, TCTMD, LOCAL]),

'argatroban': card('Argatroban (HIT)', [
  ('Dose', '2 mcg/kg/min continuous infusion; 0.5 mcg/kg/min in moderate or severe hepatic impairment; adjust to aPTT 1.5 to 3 times baseline ✅ [label].'),
  ('Why it is chosen', 'Not renally cleared (hepatic), so it works in kidney failure.'),
  ('Warfarin overlap', 'Argatroban raises the INR. Start warfarin only after platelets recover, overlap at least 5 days, and follow the label method for stopping argatroban ✅ [ASH 2018; label].'),
  ('Alternatives', 'Bivalirudin, fondaparinux, or a DOAC in stable patients per ASH 2018 ✅ [ASH].'),
], [ARGA, ASH]),
}

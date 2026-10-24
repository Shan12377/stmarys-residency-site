# L&D drug cards (part of drugcards.CARDS).
def card(title, sections, sources): return {'title': title, 'sections': sections, 'sources': sources}
def s(t, url, mark='✅'): return {'t': t, 'url': url, 'mark': mark}

CO767 = s('ACOG Committee Opinion 767: severe hypertension in pregnancy and postpartum (2019)', 'https://doi.org/10.1097/AOG.0000000000003075')
PB222 = s('ACOG Practice Bulletin 222: gestational hypertension and preeclampsia (2020)', 'https://doi.org/10.1097/AOG.0000000000003891')
ALG = s('CMQCC/Kansas PQC acute treatment algorithm (cites ACOG)', 'https://kansaspqc.kdhe.ks.gov/acute-treatment-algorithm-spring25')
ACC = s('ACC: antihypertensives in pregnancy and lactation (2026)', 'https://www.acc.org/latest-in-cardiology/articles/2026/07/02/15/04/antihypertensive-medications-in-pregnancy-and-lactation')
PB183 = s('ACOG Practice Bulletin 183: postpartum hemorrhage (2017)', 'https://doi.org/10.1097/AOG.0000000000002351')
WOMAN = s('WOMAN trial. Lancet 2017;389:2105-2116', 'https://doi.org/10.1016/S0140-6736(17)30638-4')
ISMP = s('ISMP high alert medications (TXA added 2024)', 'https://home.ecri.org/blogs/ismp-resources/high-alert-medications-in-acute-care-settings')
PB107 = s('ACOG Practice Bulletin 107: induction of labor (2009)', 'https://doi.org/10.1097/AOG.0b013e3181b48ef5')
FPN = s('FPnotebook: oxytocin regimens (summary)', 'https://mobile.fpnotebook.com/OB/Pharm/Oxytcn.htm')
AAFP = s('AAFP: vaginal misoprostol for cervical ripening', 'https://www.aafp.org/pubs/afp/issues/2006/0201/p511.html')
CO797 = s('ACOG Committee Opinion 797: GBS prevention (2020)', 'https://doi.org/10.1097/AOG.0000000000003668', '✅✅')
CO712 = s('ACOG Committee Opinion 712: intraamniotic infection (2017)', 'https://doi.org/10.1097/AOG.0000000000002236')
MERCK = s('Merck Manual: intraamniotic infection regimens (cites ACOG 712)', 'https://www.merckmanuals.com/professional/multimedia/table/antibiotic-regimens-for-treatment-of-intraamniotic-infection')
CO713 = s('ACOG Committee Opinion 713: antenatal corticosteroids (2017)', 'https://doi.org/10.1097/AOG.0000000000002237')
ALPS = s('MDedge: late preterm steroids (ALPS)', 'https://mdedge.com/content/start-offering-antenatal-corticosteroids-women-delivering-between-34-0/7-and-36-6/7-weeks')
FDANSAID = s('FDA: avoid NSAIDs at 20 weeks or later (2020)', 'https://www.fda.gov/drugs/drug-safety-and-availability/fda-recommends-avoiding-use-nsaids-pregnancy-20-weeks-or-later-because-they-can-result-low-amniotic')
PB181 = s('ACOG Practice Bulletin 181: Rh D alloimmunization (2017)', 'https://doi.org/10.1097/AOG.0000000000002232')
USPSTF = s('USPSTF 2021: low dose aspirin for preeclampsia', 'https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/low-dose-aspirin-use-for-the-prevention-of-morbidity-and-mortality-from-preeclampsia-preventive-medication')
LACT = s('LactMed (NIH)', 'https://www.ncbi.nlm.nih.gov/books/NBK501922/')
LOCAL = {'t': "St. Mary's L&D order sets and pump library (verify locally)", 'url': '', 'mark': '⚠️'}

LD = {
'labetalol_ob': card('Labetalol IV and PO (pregnancy and postpartum BP)', [
  ('What it is for', 'Acute severe range BP (160 or more systolic or 110 or more diastolic for 15 minutes) in pregnancy and postpartum; also oral treatment of chronic hypertension ✅✅ [CO 767; ACC].'),
  ('How it works', 'Blocks beta receptors and alpha 1 receptors (IV ratio about 1:7 alpha to beta): lowers BP without reflex tachycardia.'),
  ('Dose', '**IV:** 20 mg over 2 minutes; recheck BP in 10 minutes; if still severe 40 mg, then 80 mg, each with a 10 minute recheck. If still severe after 80 mg, switch to hydralazine and get help ✅✅ [CO 767; algorithm]. The injection label caps cumulative repeated doses at 300 mg ⚠️ [label].\n**Oral (chronic or step down):** usually 200 to 2,400 mg per day divided 2 to 3 times ✅ [ACC].'),
  ('Weight based?', 'No. Fixed mg doses.'),
  ('Rate', 'Each IV dose over 2 minutes. Patient lying down during and after (orthostatic hypotension).'),
  ('Contraindications', 'Asthma or reactive airway disease, heart block beyond first degree or significant bradycardia, decompensated heart failure, cardiogenic shock. Algorithm: if HR is under 60 or she has asthma, start with hydralazine or nifedipine; if HR is over 110, labetalol is preferred ✅ [algorithm].'),
  ('Interactions', 'Additive hypotension with magnesium, nifedipine, anesthesia. Masks hypoglycemia signs in diabetics.'),
  ('Monitoring', 'BP every 10 minutes during dosing, maternal heart rate, fetal heart rate tracing. Goal is not normal BP: about 130 to 150 systolic and 80 to 100 diastolic ✅ [algorithm].'),
  ('Baby', 'Can cause neonatal bradycardia and hypoglycemia; tell the pediatric team. Compatible with breastfeeding ✅ [ACC; LactMed].'),
  ('Alternatives', 'Hydralazine IV or immediate release nifedipine PO (all three are first line) ✅✅ [CO 767].'),
], [CO767, ALG, ACC, LACT, LOCAL]),

'hydralazine_ob': card('Hydralazine IV (pregnancy and postpartum BP)', [
  ('What it is for', 'First line for acute severe range BP, especially with asthma or bradycardia ✅✅ [CO 767; algorithm].'),
  ('How it works', 'Directly relaxes arterial smooth muscle. Reflex tachycardia is common.'),
  ('Dose', '5 to 10 mg IV (or IM) over 2 minutes; recheck in 20 minutes; if still severe, 10 mg; if still severe after that, switch to labetalol (unless contraindicated) and get help ✅✅ [CO 767; algorithm].'),
  ('Weight based?', 'No.'),
  ('Onset', 'Peaks 10 to 20 minutes, which is why the recheck is at 20 minutes, not 10.'),
  ('Cautions', 'Overshoot hypotension (can drop placental blood flow and cause fetal heart rate changes), maternal tachycardia, headache (can mimic worsening preeclampsia).'),
  ('Monitoring', 'BP every 5 to 10 minutes after dosing, maternal heart rate, fetal heart rate.'),
  ('Alternatives', 'Labetalol IV or nifedipine IR PO.'),
], [CO767, ALG, LOCAL]),

'nifedipine_ob': card('Nifedipine (immediate release for severe BP; extended release for chronic)', [
  ('What it is for', 'IR: acute severe range BP, very useful without IV access. ER: chronic hypertension in pregnancy and postpartum ✅✅ [CO 767; ACC].'),
  ('Dose', '**IR:** 10 mg PO; recheck in 20 minutes; if still severe 20 mg; recheck 20 minutes; 20 mg again; if still severe, switch to labetalol and get help ✅✅ [CO 767; algorithm].\n**ER:** often 30 to 120 mg once daily ✅ [ACC].'),
  ('Administration', '**Swallow whole.** Never sublingual, never bitten or punctured: the BP can crash and drop blood flow to the baby.'),
  ('Interactions', 'Magnesium: label warns about combining with calcium channel blockers; ACOG still uses both with close BP and reflex monitoring. Strong CYP3A4 inhibitors raise levels.'),
  ('Cautions', 'Reflex tachycardia, headache, flushing.'),
  ('Lactation', 'Compatible ✅ [ACC; LactMed].'),
], [CO767, ALG, ACC, LACT]),

'ace_pregnancy': card('ACE inhibitors and ARBs in pregnancy and breastfeeding', [
  ('Pregnancy', 'Contraindicated in pregnancy (fetal kidney injury, low amniotic fluid, skull and growth problems, mostly from second trimester exposure). Stop and switch to labetalol or nifedipine ER ✅✅ [ACC; CO 767].'),
  ('After delivery', 'The ban ends at delivery. Enalapril (and captopril) are preferred ACE inhibitors while breastfeeding ✅ [ACC; LactMed].'),
  ('Pharmacist actions', 'Tell the OB team about the exposure so they can check amniotic fluid and growth. Document.'),
], [ACC, CO767, LACT]),

'oxytocin': card('Oxytocin (induction, augmentation, postpartum hemorrhage)', [
  ('What it is for', 'Induction and augmentation of labor; first line prevention and treatment of postpartum hemorrhage from uterine atony ✅✅ [PB 183; PB 107].'),
  ('Dose', '**Induction, low dose:** start 0.5 to 2 milliunits/min, increase by 1 to 2 milliunits/min every 15 to 40 minutes ✅ [PB 107; summary].\n**High dose regimen:** start 6, increase by 3 to 6 milliunits/min ✅ [PB 107].\n**PPH:** 10 to 40 units in 500 to 1,000 mL IV as a continuous infusion, or 10 units IM ✅✅ [PB 183; summary].'),
  ('Show the math', 'Example standard bag 30 units in 500 mL = 60 milliunits/mL (check St. Mary\'s bag ⚠️). 2 milliunits/min = 2 / 60 x 60 min = **2 mL/h**. 10 milliunits/min = **10 mL/h**. In milliunits/min with this bag, mL/h equals milliunits/min.'),
  ('Safety', 'ISMP high alert drug: one standard concentration, smart pump library, never next to magnesium bags. Avoid rapid undiluted IV push (hypotension, tachycardia) ⚠️ [label].'),
  ('Watch', 'Tachysystole (more than 5 contractions in 10 minutes averaged over 30 minutes) with fetal heart rate changes: lower or stop. Water intoxication and low sodium with long, high dose infusions (oxytocin acts like ADH) ✅ [summary].'),
  ('Alternatives in PPH', 'Methylergonovine, carboprost, misoprostol, plus TXA (see their cards).'),
], [PB183, PB107, FPN, ISMP, LOCAL]),

'methylergonovine': card('Methylergonovine (PPH, second line)', [
  ('Dose', '0.2 mg IM every 2 to 4 hours ✅ [PB 183].'),
  ('How it works', 'Ergot alkaloid: contracts uterine and vascular smooth muscle.'),
  ('Contraindications', 'Hypertension, preeclampsia, heart disease (vasoconstriction can push BP into stroke range) ✅ [PB 183].'),
  ('Boxed warning', 'Strong CYP3A4 inhibitors (HIV protease inhibitors, clarithromycin, azoles): severe vasospasm and ischemia ✅ [label].'),
  ('Handling', 'Refrigerate. IV use only in emergencies, slowly ⚠️ [label].'),
  ('Lactation', 'Single doses compatible per LactMed ✅.'),
  ('Alternatives', 'Carboprost (if no asthma), misoprostol, TXA.'),
], [PB183, LACT]),

'carboprost': card('Carboprost (15 methyl PGF2 alpha; PPH, second line)', [
  ('Dose', '250 mcg IM every 15 to 90 minutes, maximum 8 doses (2 mg) ✅ [PB 183].'),
  ('Contraindication', 'Asthma (bronchospasm) ✅ [PB 183].'),
  ('Side effects', 'Diarrhea, vomiting, fever, bronchospasm.'),
  ('Handling', 'Refrigerate.'),
  ('Alternatives', 'Methylergonovine (if no hypertension), misoprostol, TXA.'),
], [PB183]),

'misoprostol_ob': card('Misoprostol (PPH and cervical ripening)', [
  ('PPH dose', '600 to 1,000 mcg once, oral, sublingual or rectal ✅ [PB 183].'),
  ('Cervical ripening dose', '25 mcg vaginally every 3 to 6 hours ✅✅ [PB 107; AAFP].'),
  ('Contraindication', 'Do not use for ripening or induction after a prior cesarean or major uterine surgery (uterine rupture) ✅✅ [PB 107; AAFP].'),
  ('Side effects', 'Fever, shivering, diarrhea, tachysystole.'),
  ('Why it is useful in PPH', 'Safe with both asthma and hypertension, and needs no refrigeration.'),
], [PB183, PB107, AAFP]),

'txa_pph': card('Tranexamic acid (PPH)', [
  ('Dose', '1 g IV over 10 minutes; a second 1 g if bleeding continues after 30 minutes or restarts within 24 hours ✅✅ [WOMAN; PB 183].'),
  ('Timing', 'Within 3 hours of birth: the mortality benefit was seen when given early ✅ [WOMAN].'),
  ('How it works', 'Antifibrinolytic: blocks plasminogen activation so clots stay in place. It does not make the uterus contract.'),
  ('Never', '**IV only.** Given into the spine by mistake (look alike vials next to spinal anesthetics) it is a potent neurotoxin; ISMP added TXA to its high alert list in 2024 ✅ [ISMP]. Store apart and label syringes "IV only."'),
  ('Cautions', 'Seizures at high doses, thrombosis risk in patients with active clots ⚠️.'),
], [WOMAN, PB183, ISMP]),

'gbs_abx': card('GBS intrapartum prophylaxis (penicillin, ampicillin, cefazolin, clindamycin, vancomycin)', [
  ('Who', 'Positive GBS culture at 36 0/7 to 37 6/7 weeks; GBS bacteriuria any time this pregnancy; a prior infant with invasive GBS; unknown status with labor under 37 weeks, membranes ruptured 18 hours or more, temperature 38 °C or higher, or a positive rapid test ✅✅ [CO 797].'),
  ('First choice', '**Penicillin G** 5 million units IV, then 2.5 to 3 million units every 4 hours until delivery. **Ampicillin** 2 g IV, then 1 g every 4 hours ✅✅ [CO 797].'),
  ('Low risk penicillin allergy', '(No anaphylaxis, angioedema, respiratory distress, hives, or severe skin reaction): **cefazolin** 2 g IV, then 1 g every 8 hours ✅✅ [CO 797].'),
  ('High risk allergy', '**Clindamycin** 900 mg IV every 8 hours only if the isolate is susceptible (including inducible resistance testing); otherwise **vancomycin** 20 mg/kg IV every 8 hours, maximum 2 g per dose ✅✅ [CO 797].'),
  ('Show the math', 'Vancomycin for 72 kg: 20 x 72 = 1,440 mg, round per protocol (for example 1,500 mg). Infusion at no faster than 10 mg/min = at least 150 minutes per label ⚠️ [St. Mary\'s infusion policy].'),
  ('Adequate for the newborn team', 'Penicillin, ampicillin or cefazolin started at least 4 hours before delivery ✅ [CO 797]. Clindamycin and vancomycin do not count as adequate.'),
], [CO797, LOCAL]),

'chorio_abx': card('Intraamniotic infection (chorioamnionitis) antibiotics', [
  ('First line', 'Ampicillin 2 g IV every 6 hours **plus** gentamicin 2 mg/kg load then 1.5 mg/kg every 8 hours, **or** gentamicin 5 mg/kg every 24 hours ✅✅ [CO 712; Merck].'),
  ('Mild penicillin allergy', 'Cefazolin 2 g IV every 8 hours plus gentamicin ✅ [CO 712].'),
  ('Severe penicillin allergy', 'Clindamycin 900 mg IV every 8 hours or vancomycin 1 g IV every 12 hours, plus gentamicin ✅ [CO 712].'),
  ('After delivery', 'Cesarean: one more dose plus clindamycin 900 mg or metronidazole 500 mg for anaerobes. Vaginal: no further doses required ✅ [CO 712].'),
  ('Show the math', 'Gentamicin for 80 kg: load 160 mg, then 120 mg every 8 hours; or once daily 400 mg. Pregnancy changes volume of distribution, so many teams check levels; Hartford is not used in pregnancy ✅.'),
  ('Watch', 'Kidney function and urine output (especially on magnesium); neuromuscular blockade risk with magnesium.'),
], [CO712, MERCK, LOCAL]),

'antenatal_steroids': card('Antenatal corticosteroids (betamethasone, dexamethasone)', [
  ('Dose', 'Betamethasone 12 mg IM every 24 hours x 2 doses, or dexamethasone 6 mg IM every 12 hours x 4 doses ✅ [CO 713].'),
  ('Who', '24 0/7 to 33 6/7 weeks at risk of delivery within 7 days; may consider from 22 0/7 weeks with family wishes; one rescue course if the first was 14 or more days ago (some as soon as 7) and still under 34 weeks ✅ [CO 713].'),
  ('Late preterm (34 0/7 to 36 6/7)', 'Single course for singletons without prior steroids if delivery likely within 7 days; ALPS excluded pregestational diabetes, multiples and chorioamnionitis ✅ [ALPS summary].'),
  ('Watch', 'Maternal hyperglycemia for about 3 days (diabetics need insulin adjustment); neonatal hypoglycemia after late preterm steroids.'),
], [CO713, ALPS]),

'indomethacin_toco': card('Indomethacin (tocolysis)', [
  ('Dose', 'Usually 50 to 100 mg loading dose, then 25 mg every 6 hours, for no more than 48 hours ⚠️ [VERIFY order set].'),
  ('Limits', 'Only before 32 weeks and no longer than 48 hours: risk of premature narrowing of the ductus arteriosus and low amniotic fluid ⚠️ [ACOG preterm labor guidance; VERIFY order set]. The FDA warns against NSAIDs from 20 weeks in general ✅ [FDA].'),
  ('Avoid', 'Kidney disease, bleeding or platelet problems, peptic ulcer, NSAID sensitive asthma.'),
], [FDANSAID, LOCAL]),

'rhig': card('Rh(D) immune globulin', [
  ('Postpartum', '300 mcg IM within 72 hours if the mother is Rh(D) negative and the baby Rh(D) positive ✅ [PB 181].'),
  ('Antenatal', '300 mcg at about 28 weeks and after events like bleeding or procedures ✅ [PB 181].'),
  ('How much it covers', 'One 300 mcg vial covers about 30 mL of fetal whole blood; a screening test (for example Kleihauer Betke) decides if more vials are needed ✅ [PB 181].'),
], [PB181]),

'aspirin_ldp': card('Low dose aspirin for preeclampsia prevention', [
  ('Dose', '81 mg daily after 12 weeks (ideally before 16), usually until delivery ✅ [USPSTF 2021].'),
  ('Who (one high risk factor)', 'Prior preeclampsia, multifetal pregnancy, chronic hypertension, pregestational diabetes, kidney disease, autoimmune disease ✅ [USPSTF].'),
  ('NSAID rule exception', 'The FDA warning against NSAIDs from 20 weeks does not apply to low dose aspirin for this purpose ✅ [FDA].'),
], [USPSTF, FDANSAID]),
}

ADA = s('ADA Standards of Care 2025, Section 15: diabetes in pregnancy', 'https://doi.org/10.2337/dc25-S015')
FDACOD = s('FDA: codeine and tramadol restrictions in breastfeeding (2017)', 'https://www.fda.gov/Drugs/DrugSafety/ucm549679.htm')
ASRA = s('ASRA guidelines 4th ed (2018); 5th ed 2025 (doi 10.1136/rapm-2024-105766) to recheck', 'https://doi.org/10.1097/AAP.0000000000000763', '⚠️')
LOV = s('Lovenox prescribing information (Sanofi)', 'https://products.sanofi.us/lovenox/lovenox.pdf')
FDASTAT = s('FDA: removal of statin pregnancy contraindication (2021)', 'https://fda.gov/drugs/drug-safety-and-availability/fda-requests-removal-strongest-warning-against-using-cholesterol-lowering-statins-during-pregnancy')
LD.update({
'gdm_insulin': card('Diabetes in pregnancy: insulin first', [
  ('Guideline', 'ADA 2025: insulin is preferred when lifestyle is not enough; metformin and glyburide should not be first line because both cross the placenta and may not reach goals ✅ [ADA 2025].'),
  ('Pharmacist role', 'Dose, teach hypoglycemia recognition and treatment, timing with meals, and plan for the big drop in insulin need right after delivery.'),
  ('Steroids', 'Antenatal steroids raise glucose for about 3 days: expect higher insulin needs.'),
], [ADA]),
'ob_pain_lactation': card('Pain control after delivery while breastfeeding', [
  ('Avoid', 'Codeine and tramadol: some mothers are ultrarapid metabolizers and pass dangerous levels to the infant ✅ [FDA 2017].'),
  ('Preferred', 'Scheduled acetaminophen plus ibuprofen (NSAIDs are fine after delivery). If an opioid is needed: low dose oxycodone for a short time, watching the baby for sleepiness and poor feeding ✅ [LactMed].'),
  ('Check any drug', 'LactMed; relative infant dose under 10% is generally acceptable; short half life, high protein binding and low oral bioavailability favor safety ✅ [LactMed].'),
], [FDACOD, LACT]),
'enox_neuraxial': card('Enoxaparin around epidurals and spinals (L&D)', [
  ('Hold before placement or removal', 'Prophylactic dose: at least 12 hours. Treatment dose: at least 24 hours ✅ [ASRA 4th ed; label] ⚠️ recheck 5th edition.'),
  ('After catheter removal', 'Next dose no sooner than 4 hours ✅ [label].'),
  ('Why', 'Spinal epidural hematoma can cause permanent paralysis (boxed warning) ✅ [label].'),
  ('Pharmacist role', 'Tell anesthesia the exact time of the last dose and the earliest safe time.'),
], [ASRA, LOV, LOCAL]),
'nsaid_pregnancy': card('NSAIDs in pregnancy', [
  ('Rule', 'Avoid NSAIDs from 20 weeks: fetal kidney problems and low amniotic fluid; near term, early closure of the ductus ✅ [FDA 2020].'),
  ('Exception', 'Low dose aspirin 81 mg for preeclampsia prevention ✅ [FDA].'),
  ('Instead', 'Acetaminophen for pain or fever.'),
], [FDANSAID]),
'statin_preg': card('Statins in pregnancy and breastfeeding', [
  ('Pregnancy', 'FDA removed the blanket contraindication in 2021; most patients stop when pregnant, very high risk patients (for example familial hypercholesterolemia with heart disease) may continue with their doctor ✅ [FDA 2021].'),
  ('Breastfeeding', 'Not recommended while breastfeeding ✅ [FDA 2021].'),
], [FDASTAT]),
})

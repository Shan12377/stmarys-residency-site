# Drug Information Hub

Her own references, organized by the job each one does. Content comes from public, citable sources. Every dose is marked ✅✅ (two sources), ✅ (one source) or ⚠️ [VERIFY], and every page lists its source links.

## Sections
| Section | Does the job of | Status |
|---|---|---|
| Drug Monographs | Lexicomp or Micromedex type reference | Pilot complete: 10 high alert drugs |
| [[IV_Compatibility]] | Trissel's or King Guide type reference | Built: diluents, lines, filters, containers, extravasation |
| [[Antimicrobial_Guide]] | Sanford type guide | Built: pneumonia, UTI, skin, meningitis, C. diff |
| [[Pediatric_Neonatal_Dosing]] | pediatric dosage handbook or Neofax type reference | Built: 6 checks, everyday doses, neonatal sepsis antibiotics |
| [[Pregnancy_Lactation]] | Briggs type reference | Built: PLLR, relative infant dose, L&D and postpartum quick answers |

## Pilot list (high alert drugs first)
1. [[Heparin]] (done)
2. [[Enoxaparin]] (done)
3. [[Insulin_IV_DKA]] (done)
4. [[Magnesium_Sulfate]] (done)
5. [[Potassium_Chloride_IV]] (done)
6. [[Vancomycin]] (done)
7. [[Gentamicin]] (done)
8. [[Norepinephrine]] (done)
9. [[Thrombolytics_Stroke]] (done)
10. [[4F_PCC]] (done)

## Free references to open directly
| Need | Link |
|---|---|
| Official FDA label | [DailyMed](https://dailymed.nlm.nih.gov/dailymed/) |
| Approvals, label history | [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/) |
| Generic equivalence | [Orange Book](https://www.accessdata.fda.gov/scripts/cder/ob/) |
| Literature | [PubMed](https://pubmed.ncbi.nlm.nih.gov/) |
| Lactation | [LactMed (NIH)](https://www.ncbi.nlm.nih.gov/books/NBK501922/) |
| QT risk | [CredibleMeds](https://crediblemeds.org/) |
| IV stability (free) | [Stabilis](https://www.stabilis.org/) |
| High alert and Do Not Crush lists | [ISMP](https://www.ismp.org/) |
| Hazardous drugs | [NIOSH list](https://www.cdc.gov/niosh/healthcare/hazardous-drugs/) |
| Shortages | [ASHP Drug Shortages](https://www.ashp.org/drug-shortages/current-shortages) |
| Calculators | [MDCalc](https://www.mdcalc.com/) |
| Poison Control | 1 800 222 1222 |

## Subscription references (use through St. Mary's or Pyrls)
Lexicomp, Micromedex (includes Poisindex), Trissel's, King Guide, Sanford Guide, pediatric and neonatal dosage handbook or Neofax, Briggs, Natural Medicines, UpToDate, [Pyrls](https://app.pyrls.com/home).

---

## Which reference do I open in 10 seconds when the phone rings?

### The Golden Rule of Hospital Pharmacy: Hospital Protocol Beats the Textbook
Before you quote Lexicomp or UpToDate to a physician or nurse, **always check St. Mary's Cerner Order Set, Hospital Policy, or Smart Pump Library first** (see [[Stay_Current]]).
- **Why:** If Lexicomp lists three ways to dose a heparin drip, DKA insulin drip, magnesium sulfate, or vancomycin AUC, you must verify against the exact nomogram and standard bag concentration built into St. Mary's smart pumps. Using an outside concentration that does not match the pump library creates a high risk medication error (ISMP High Alert Medications 2024).

```mermaid
flowchart TD
    Q["Phone Rings: What is the question?"] --> H["STEP 0: Is there a St. Mary's Cerner Order Set, Protocol, or Smart Pump Library rule?<br/>(Heparin, DKA, Mag Sulfate, Stroke, Vanc, Standard Drips)<br/>ALWAYS check hospital policy first"]
    H --> T1["IV line question:<br/>Can Drug A and Drug B run together?<br/>What diluent or bag concentration?"]
    H --> T2["Baby or child question:<br/>What is the dose for a neonate or pediatric patient?"]
    H --> T3["Pregnancy or breastfeeding question:<br/>Is this safe for mom or baby?"]
    H --> T4["Adult dose, renal CrCl, antibiotic bug coverage, or crushing tablets?"]

    T1 --> R1["Open TRISSEL'S IV Compatibility<br/>(inside Lexicomp or Micromedex)<br/>Check Y-Site tab vs Admixture tab, concentration, and diluent"]
    T2 --> R2["Under 28 days or NICU: Open NEOFAX (uses PMA + PNA)<br/>1 month to 18 years: Open LEXI-PEDS or Pediatric Dosage Handbook<br/>NEVER use Adult Lexicomp for a neonate"]
    T3 --> R3["Pregnancy: Open BRIGGS or FDA PLLR section<br/>Breastfeeding: Open LACTMED (free NIH)<br/>Look for Relative Infant Dose (RID) below 10%"]
    T4 --> R4["Adult renal or general dosing: Open LEXICOMP or MICROMEDEX<br/>Bug coverage: Hospital Antibiogram + SANFORD GUIDE<br/>Crushing for NG tube: ISMP Do Not Crush + Lexicomp Administration tab"]

    style Q fill:#f8fafc,stroke:#334155,color:#0f172a,stroke-width:2px
    style H fill:#fee2e2,stroke:#991b1b,color:#7f1d1d,stroke-width:2px
    style T1 fill:#fef3c7,stroke:#92400e,color:#78350f,stroke-width:2px
    style T2 fill:#fef3c7,stroke:#92400e,color:#78350f,stroke-width:2px
    style T3 fill:#fef3c7,stroke:#92400e,color:#78350f,stroke-width:2px
    style T4 fill:#fef3c7,stroke:#92400e,color:#78350f,stroke-width:2px
    style R1 fill:#dcfce7,stroke:#166534,color:#14532d,stroke-width:2px
    style R2 fill:#dcfce7,stroke:#166534,color:#14532d,stroke-width:2px
    style R3 fill:#dcfce7,stroke:#166534,color:#14532d,stroke-width:2px
    style R4 fill:#dcfce7,stroke:#166534,color:#14532d,stroke-width:2px
```
*Sources: ISMP Targeted Medication Safety Best Practices 2024; ASHP Guidelines on Providing Drug Information; [[IV_Compatibility]], [[Pediatric_Neonatal_Dosing]], and [[Pregnancy_Lactation]].*

---

## Side by side guide: Trissel's vs Lexicomp vs NeoFax vs Sanford vs Briggs

| Resource | When to open it first | What trap to watch out for (Plain English) |
|---|---|---|
| **Trissel's IV Compatibility** (accessed via the *IV Compatibility* tab in Lexicomp or Micromedex) | Nurse asks: *"Can I Y-site vancomycin with piperacillin tazobactam?"* or *"How long is this diluted bag stable?"* | **Check the right tab and concentration:**<br>• **Y-Site tab:** Two separate bags meeting at the tubing port near the patient (only mixes for a few minutes in the line).<br>• **Admixture (Solution) tab:** Mixed together inside the same IV bag for hours.<br>• **Concentration matters:** Ampicillin is stable much longer in NS than D5W, and high concentrations precipitate faster. Vancomycin and beta lactams can precipitate at certain concentrations.<br>• **"Variable" or "No Data":** Click into the study details. If your patient's concentration is higher than the tested concentration, or if there is no data, treat as **Incompatible** and flush the line with NS between drugs or use a separate lumen (see [[IV_Compatibility]]). |
| **Lexicomp (Adult) vs Micromedex** | Every routine adult verification: renal CrCl adjustments, hepatic adjustments, black box warnings, max daily doses, administration rates, and drug interactions. | **How to use them together:**<br>• **Lexicomp** is fastest at the bench for clean dosing by indication, CrCl cutoffs, and administration rate (push vs piggyback).<br>• **Micromedex** is your tie breaker when Lexicomp is vague, when you need deeper toxicology (**Poisindex**), or when checking detailed **Trissel's** solution stability tables. |
| **NeoFax vs Lexi-Peds (Taketomo Pediatric Handbook)** | **NeoFax:** Any baby in the NICU or under 28 days old.<br>**Lexi-Peds:** Infants over 28 days, children, and adolescents in PICU or general pediatrics. | **Never use Adult Lexicomp for a baby:**<br>• Premature babies clear drugs slowly because their kidneys and liver are still developing.<br>• **NeoFax** doses by **Gestational Age (GA)** or **Postmenstrual Age (PMA = GA + weeks since birth)** plus **Postnatal Age (PNA = days since birth)** (for example, NICU gentamicin every 24, 36, or 48 hours; see [[NICU_Core]]).<br>• **Lexi-Peds** gives weight based `mg/kg` dosing **and** the adult ceiling cap (never exceed the adult dose in a heavy teenager; see [[Pediatric_Neonatal_Dosing]]). |
| **St. Mary's Antibiogram + Sanford Guide** | Doctor asks: *"What empiric antibiotic should we start for this ICU pneumonia or urosepsis?"* or *"Does oral step down work here?"* | **Local resistance beats national averages:**<br>• **Sanford Guide** tells you which bugs a drug covers in general and gives clean renal antibiotic dosing tables.<br>• **St. Mary's Antibiogram** tells you what percentage of local *Pseudomonas*, *E. coli*, or *MRSA* at St. Mary's is actually susceptible this year (see [[ID_Core]] and [[Antimicrobial_Guide]]). |
| **Briggs (Pregnancy) & LactMed (Breastfeeding)** | OB nurse or physician asks: *"Can this mom take labetalol, enoxaparin, or sertraline while pregnant or breastfeeding?"* | **Letters A, B, C, D, X are gone:**<br>• The FDA replaced pregnancy letter categories with the **PLLR** narrative (Risk Summary, Clinical Considerations, Data). Use **Briggs** or the FDA label PLLR section for pregnancy.<br>• For breastfeeding, open **LactMed (NIH, free)** and check the **Relative Infant Dose (RID)**: an **RID below 10%** is generally considered compatible with breastfeeding for full term infants (see [[Pregnancy_Lactation]]). |
| **CredibleMeds + ISMP Lists** | Checking QT prolongation stacking (ondansetron + haloperidol + azithromycin + methadone) or whether a pill can be crushed for an NG/OG tube. | • **CredibleMeds** separates drugs that **clearly cause Torsades de Pointes** ("Known Risk") from drugs that only prolong QTc under certain conditions (check K above 4.0 and Mg above 2.0).<br>• **ISMP Do Not Crush** (and Lexicomp's *Administration* section) stops you from crushing extended release (`ER/XR`), enteric coated (`EC`), or hazardous tablets (see [[Med_Safety_and_Florida_Law]]). |


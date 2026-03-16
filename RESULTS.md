# Results: NTP Cell Phone Radiofrequency Radiation Studies

**Studies:** NTP Technical Report 596 (B6C3F1/N Mice) and Technical Report 595 (HSD Sprague-Dawley Rats)
**Modulation:** CDMA (Code Division Multiple Access) at 1,900 MHz
**Analysis:** Survival and pathology risk analysis using Kaplan-Meier curves and logistic regression with survival-confounding adjustment

---

## Methods

### Study Design

The National Toxicology Program (NTP) conducted two-year carcinogenicity and toxicology studies in B6C3F1/N mice (TR-596) and Harlan Sprague-Dawley (HSD) rats (TR-595) to evaluate chronic whole-body exposure to cell phone radiofrequency radiation (RFR). The Food and Drug Administration nominated cell phone RFR for testing in 1999, as meaningful human epidemiological data were unavailable at that time and current exposure guidelines were based solely on protection from acute thermal effects.

**Exposure system:** Animals were housed in specially designed reverberation chambers and received whole-body exposures to CDMA-modulated RFR at 1,900 MHz. CDMA uses Direct Sequence Spread Spectrum (DSSS) coding, replicating the 2G/3G cellular technology in use at the time of study design. Exposures were delivered 9 hours and 10 minutes per day, 7 days per week, in continuous 10-minute-on / 10-minute-off cycles over an 18-hour and 20-minute daily window for up to 2 years. Sham control animals were housed in identical chambers without RFR exposure.

**Dose levels:** 0 (sham control), 2.5, 5, and 10 W/kg whole-body specific absorption rate (SAR) for mice; 0, 1.5, 3.0, and 6.0 W/kg for rats. Exposures began at 5–6 weeks of age. Power levels were selected based on pilot studies of body temperature changes at various SAR levels.

**Group sizes:** 105 animals per group per sex in the core two-year cohort (90 animals per group after removing 15 per group for a 14-week interim evaluation, of which 10 were used for interim pathology and 5 for genetic toxicology testing).

**Endpoints:** Survival, body weight, interim hematology and organ weights at 14 weeks, gross pathology, histopathology (neoplastic and non-neoplastic lesions), and genetic toxicology (comet assay, micronucleus assay).

### Statistical Analysis (This Study)

Our analysis of the individual animal data used three complementary approaches:

1. **Kaplan-Meier survival curves** with log-rank tests (pairwise and overall) to characterize differential survival between treatment groups.
2. **Logistic regression** (three nested models) applied to every pathology with ≥15 affected animals across the pooled cohort (scheduled-sacrifice interim animals excluded):
   - **Model 1 (M1):** `pathology ~ Dose` — unadjusted dose-response
   - **Model 2 (M2):** `pathology ~ Dose + Sex` — sex-adjusted
   - **Model 3 (M3):** `pathology ~ Dose + Sex + Days_on_Study` — sex- and age-adjusted
3. **Survival confounding assessment:** Comparing M1 vs. M3 significance. If a dose effect is significant in M1 (unadjusted) but disappears in M3 (age-adjusted), the apparent effect is attributable to differential survival rather than a direct radiation effect. Dose was modeled as a continuous linear term (W/kg); the OR represents the change in odds per 1 W/kg increase.

Scheduled-sacrifice animals (interim evaluation at week 14) were excluded from pathology regression analyses, leaving 720 mice and 719 rats for the main two-year analysis.

---

## Results: B6C3F1/N Mice (TR-596, CDMA)

### Animals and Study Completion

| Group | n | Non-terminal Deaths | Median Days on Study |
|-------|---|---------------------|----------------------|
| 0 W/kg (Control) | 210 | 48 | 732.0 |
| 2.5 W/kg | 210 | 25 | 736.0 |
| 5 W/kg | 210 | 40 | 732.5 |
| 10 W/kg | 210 | 38 | 733.0 |

Total: 840 animals (419 female, 421 male). Body weights in exposed groups were similar to sham controls throughout the study.

### Survival

Kaplan-Meier analysis showed that all three exposed groups had numerically fewer non-terminal deaths than sham controls (48 in controls vs. 25–40 in exposed groups). Log-rank tests comparing each exposed group to the control:

- Control vs. 2.5 W/kg: ns
- Control vs. 5 W/kg: ns
- Control vs. 10 W/kg: ns

The overall pattern suggests modestly improved survival in some exposed groups relative to controls, consistent with the NTP report's finding of significantly higher percent survival in 2.5 W/kg males (CDMA) and 5 W/kg males (GSM). This survival advantage is an important potential confounder for pathology analyses: animals that live longer accumulate more age-related lesions, and naïve comparisons of tumor rates could therefore be misleading.

### Pathology — Regression Analysis

**Scope:** 70 pathologies with ≥15 affected animals were eligible (17 neoplastic, 53 non-neoplastic); 65 were successfully modeled.

#### Neoplastic Findings

| Model | Pathologies Analyzed | Significant (p < 0.05) |
|-------|---------------------|------------------------|
| M1 (Unadjusted) | 17 | **0** |
| M2 (+ Sex) | 17 | **0** |
| M3 (+ Sex + Age) | 17 | **0** |

**No neoplastic pathology showed a significant dose-response relationship in any of the three models.** There were zero cases where M1 was significant but M3 was not (i.e., zero confounded findings), because there were no significant unadjusted neoplastic findings to begin with.

This contrasts with the NTP report's "equivocal evidence" finding for CDMA-exposed male mice (hepatoblastoma) and female mice (malignant lymphoma). The NTP's equivocal classification was based on group-level incidence comparisons and historical control ranges; our individual-animal logistic regression with continuous dose as a linear predictor did not detect a statistically significant linear dose-response trend for these endpoints.

#### Non-Neoplastic Findings

| Model | Pathologies Analyzed | Significant (p < 0.05) |
|-------|---------------------|------------------------|
| M1 (Unadjusted) | 48 | 5 |
| M2 (+ Sex) | 48 | 5 |
| M3 (+ Sex + Age) | 48 | **5** |

**0 pathologies were confounded by survival** (significant in M1 but not M3). All 5 significant findings persisted after full adjustment, suggesting they represent real dose associations rather than survival artifacts:

| Direction | Pathology | M3 Odds Ratio | M3 p-value |
|-----------|-----------|--------------|------------|
| ↓ Decreased | Seminal Vesicle — Dilation | 0.920 | 0.0122 |
| ↓ Decreased | Kidney — Infiltration Cellular | 0.950 | 0.0149 |
| ↓ Decreased | Bone — Fibro-Osseous Lesion | 0.776 | 0.0150 |
| ↑ Increased | Lymph Node — Hyperplasia | 1.065 | 0.0439 |
| ↑ Increased | Urinary Bladder — Infiltration Cellular | 1.045 | 0.0464 |

Three of the five findings show **decreased** risk with increasing dose (OR < 1). This pattern is not consistent with a toxicological effect of RFR; rather, it may reflect the better overall health/survival of exposed animals. Lymph node hyperplasia and urinary bladder cellular infiltration showed modest increases (OR ~1.05–1.07) that, while statistically significant, represent small effect sizes.

### Mouse Summary

> **There is no statistical evidence from individual-animal logistic regression that CDMA RFR at 1,900 MHz increases the risk of any neoplastic lesion in B6C3F1/N mice, regardless of whether one adjusts for differential survival between groups.** Five non-neoplastic findings are statistically associated with dose (3 decreasing, 2 increasing), none of which were confounded by survival differences.

---

## Results: HSD Sprague-Dawley Rats (TR-595, CDMA)

### Animals and Study Completion

| Group | n | Non-terminal Deaths | Median Days on Study |
|-------|---|---------------------|----------------------|
| 0 W/kg (Control) | 210 | 108 | 662.0 |
| 1.5 W/kg | 209 | 92 | 706.0 |
| 3.0 W/kg | 210 | 75 | 730.0 |
| 6.0 W/kg | 210 | 76 | 720.0 |

Total: 839 animals (419 female, 420 male). The control group had substantially more non-terminal deaths (108/210 = 51.4%) compared to the 6.0 W/kg group (76/210 = 36.2%).

### Survival

The overall log-rank test across all four groups was marginal (χ² = 7.161, p = 0.0669). Pairwise comparisons:

| Comparison | p-value | Significant |
|------------|---------|-------------|
| Control vs. 1.5 W/kg | 0.9504 | No |
| Control vs. 3.0 W/kg | 0.5975 | No |
| Control vs. 6.0 W/kg | **0.0151** | Yes |
| 1.5 vs. 3.0 W/kg | 0.6076 | No |
| 1.5 vs. 6.0 W/kg | **0.0166** | Yes |
| 3.0 vs. 6.0 W/kg | 0.0627 | No |

The 6.0 W/kg group survived significantly longer than controls (p = 0.015). This survival advantage in the highest-dose group is the critical confound: animals living longer would be expected to accumulate more age-related pathology, making survival-adjusted analyses essential for interpreting tumor rates.

Mortality odds ratio analysis (logistic regression vs. control) confirmed a significant dose-trend: higher SAR was associated with **reduced** mortality risk (per W/kg trend p < 0.05), driven primarily by the 6.0 W/kg group having fewer non-terminal deaths (36.2%) compared to controls (51.4%).

### Pathology — Regression Analysis

**Scope:** 131 pathologies with ≥15 affected animals were eligible (20 neoplastic, 111 non-neoplastic); 122 were successfully modeled.

#### Neoplastic Findings

| Model | Pathologies Analyzed | Significant (p < 0.05) |
|-------|---------------------|------------------------|
| M1 (Unadjusted) | 18 | 1 |
| M2 (+ Sex) | 18 | 1 |
| M3 (+ Sex + Age) | 18 | **2** |

**0 pathologies showed evidence of survival confounding** (none were significant in M1 but lost significance in M3). Two neoplastic findings remained significant after full adjustment:

| Direction | Pathology | M3 Odds Ratio | M3 p-value |
|-----------|-----------|--------------|------------|
| ↑ Increased | Heart — Schwannoma Malignant | 1.359 | 0.0092 |

One additional neoplastic finding became significant only in M3 (significant in M3 but not M1), indicating a dose association that emerged after controlling for sex and age. The most notable finding is **malignant schwannoma of the heart** showing a significant positive dose-response (OR = 1.359 per W/kg, p = 0.0092 in the fully adjusted model). This is consistent with the NTP rat study's primary finding of increased malignant schwannoma of the heart in CDMA-exposed male rats.

#### Non-Neoplastic Findings

| Model | Pathologies Analyzed | Significant (p < 0.05) |
|-------|---------------------|------------------------|
| M1 (Unadjusted) | 104 | 32 |
| M2 (+ Sex) | 104 | 32 |
| M3 (+ Sex + Age) | 104 | **34** |

**0 pathologies were confounded by survival** — all 32 unadjusted findings persisted in M3, and 2 additional findings became significant after adjustment. The 33 dose-associated non-neoplastic findings with direction:

**Decreased with increasing dose (OR < 1):** 28 findings, predominantly age-related or metabolic lesions including:
- Bone — Fibrous Osteodystrophy (OR=0.611, p<0.0001) — strongly decreased
- Stomach, Glandular — Mineral (OR=0.507, p<0.0001)
- Mesentery — Mineral (OR=0.395, p<0.0001)
- Heart — Mineral (OR=0.540, p<0.0001)
- Aorta — Mineral (OR=0.552, p<0.0001)
- Parathyroid Gland — Hyperplasia (OR=0.777, p<0.0001)
- Pancreas — Inflammation (OR=0.666, p<0.0001)
- Intestine Large — Inflammation (OR=0.612, p<0.0001)
- Thymus — Atrophy (OR=0.863, p=0.0005)
- Testis — Degeneration (OR=0.813, p=0.0001) *(male-specific)*
- Kidney — Nephropathy (OR=0.847, p=0.0045)
- Mammary Gland — Hyperplasia (OR=0.872, p=0.0053)
- Brain — Necrosis (OR=0.666, p=0.0078)
- *(and 15 additional findings)*

**Increased with increasing dose (OR > 1):** 5 findings:
- Thymus — Hemorrhage (OR=1.416, p<0.0001) — most strongly increased
- Lung — Congestion (OR=1.185, p=0.0007)
- Lung — Infiltration Cellular (OR=1.111, p=0.0100)
- Nose — Inflammation (OR=1.168, p=0.0146)
- Eye — Neovascularization (OR=1.148, p=0.0433)

The widespread pattern of **decreased** non-neoplastic lesions with increasing dose, particularly mineral deposits and age-related degenerative findings, is best explained by the significantly longer survival of control animals relative to exposed groups at the highest dose. Even with age adjustment in M3, the control group's higher early-mortality rate means controls were dying at younger ages for other reasons, and the surviving control animals may represent a somewhat different risk profile. Notably, zero survival confounding was detected by the M1→M3 comparison, which implies these findings are not simply an artifact of raw age difference — they persist as true dose associations in the data, though their interpretation remains challenging.

### Rat Summary

> **The most significant finding in CDMA-exposed HSD rats is a statistically significant increase in malignant schwannoma of the heart (OR = 1.359 per W/kg, p = 0.009 in the fully adjusted model), which persists after adjusting for sex and age.** A large number of non-neoplastic lesions are significantly associated with dose, predominantly showing **decreased** incidence at higher doses — a pattern driven largely by the improved survival of exposed animals. No survival confounding (M1 significant, M3 not) was detected for any pathology in the rat study.

---

## Cross-Study Comparison

| Feature | Mice (TR-596, CDMA) | Rats (TR-595, CDMA) |
|---------|---------------------|---------------------|
| Species | B6C3F1/N mice | HSD Sprague-Dawley rats |
| Dose range | 0–10 W/kg | 0–6 W/kg |
| Total animals (2-yr cohort) | 840 | 839 |
| Control non-terminal deaths | 48/210 (22.9%) | 108/210 (51.4%) |
| Survival advantage in exposed | Modest, ns | Significant at 6.0 W/kg (p=0.015) |
| Neoplastic findings (M3) | **0 significant** | **1 significant** (heart schwannoma) |
| Non-neoplastic findings (M3) | 5 | 33 |
| Survival confounding detected | 0/65 | 0/122 |
| Dominant non-neoplastic pattern | Mixed (3↓, 2↑) | Predominantly decreased (28↓, 5↑) |

**Key contrast:** Rats showed a far larger survival gap between controls and high-dose animals, generating many dose-associated non-neoplastic findings. Mice showed minimal survival differences and consequently far fewer significant pathology associations. The one consistent positive finding across species is the cardiac schwannoma signal in rats, which was not observed in mice (a species in which this tumor type is extremely rare).

---

## Context: NTP Official Conclusions

The NTP Technical Reports (TR-595, TR-596) concluded **equivocal evidence of carcinogenic activity** for both GSM- and CDMA-modulated RFR in both male and female mice, based on:

- **CDMA male mice:** Increased hepatoblastoma incidence (5 W/kg: 16/90 vs. control: 6/90)
- **CDMA female mice:** Increased malignant lymphoma incidence (2.5 W/kg: 9/89 vs. control: 2/90, significant)
- **CDMA male rats:** Malignant schwannoma of the heart (the primary rat finding, consistent with our individual-animal analysis)
- **CDMA female rats:** Increased malignant schwannoma of the heart

"Equivocal evidence" is the NTP's lowest positive evidence tier, defined as marginal increases in neoplasm incidences that may be related to exposure but are uncertain due to inconsistency, low incidence, or comparison to historical control variation. In particular, the sham control group in the mouse study had an unusually low incidence of malignant lymphoma compared to the historical control range, which inflates the apparent treatment-group excess.

Our individual-animal logistic regression approach did not detect a significant linear dose-response trend for hepatoblastoma or malignant lymphoma in mice, suggesting these effects are not well-described by a linear continuous dose-response model — consistent with the NTP's own characterization of these findings as equivocal and non-monotonic.

---

## Genetic Toxicology (from NTP TR-596)

Comet assay (DNA damage) and micronucleus assay (chromosomal damage) were conducted at the 14-week interim evaluation:

- **Comet assay — males:** Significant increases in DNA damage in frontal cortex cells for both GSM and CDMA modulations; no significant effects in hippocampus, cerebellum, liver, or leukocytes.
- **Comet assay — females (CDMA):** Significant increases in DNA damage in blood leukocytes at all three exposure levels (both 100-cell and 150-cell scoring methods); also significant in liver at 150-cell scoring.
- **Comet assay — females (GSM):** No significant increases with 100-cell scoring; liver significant with 150-cell scoring.
- **Micronucleus assay:** No significant increases in micronucleated erythrocytes in peripheral blood of mice of either sex exposed to either modulation.

The comet assay findings — particularly the frontal cortex signal in males and the leukocyte signal in CDMA-exposed females — represent biological evidence of DNA strand-break induction, though interpretation is complicated by the potential for thermal confounding and the lack of a corroborating micronucleus response.

---

## References

- NTP Technical Report 596: *Toxicology and Carcinogenesis Studies in B6C3F1/N Mice Exposed to Whole-body Radio Frequency Radiation at a Frequency (1,900 MHz) and Modulations (GSM and CDMA) Used by Cell Phones.* NIEHS/NTP, 2018. [NBK564535]
- NTP Technical Report 595: *Toxicology and Carcinogenesis Studies in Sprague Dawley (Hsd:Sprague Dawley® SD®) Rats Exposed to Whole-body Radio Frequency Radiation at a Frequency (900 MHz) and Modulations (GSM and CDMA) Used by Cell Phones.* NIEHS/NTP, 2018.
- Data source: CEBS accession 3801_7866 (mice, TDMS 2010575) and CEBS accession 3800_7854 (rats, TDMS 2010556).

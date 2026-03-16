# TR-595 Rat Study Data — CDMA Cell Phone Radiation

**Source:** CEBS / NIEHS — Cell Phone Radiation: CDMA study
**Accession:** 3800_7854
**NTP Technical Report:** TR-595
**TDMS Number:** 2010556

## Study Summary

2-year whole-body exposure study of Harlan Sprague Dawley (HSD) rats to CDMA cell phone radiofrequency radiation. Female animals only in this dataset.

- **Species/Strain:** HSD Rats (female)
- **n:** 419 animals across 4 treatment groups
- **Exposure route:** Whole body
- **Study number:** C20105B

## Treatment Groups

| Group | W/kg (SAR) | n |
|---|---|---|
| Vehicle Control | 0 | 105 |
| Low | 1.5 W/kg | 104 |
| Mid | 3.0 W/kg | 105 |
| High | 6.0 W/kg | 105 |

## Files

| File | Description |
|---|---|
| `2010556_Female_Individual_Animal_Survival_Data.xls` | Per-animal survival data: animal ID, cage, days on study, treatment, removal reason, week of removal |

## Data Format

The `.xls` file is HTML-encoded and is parsed with `pandas.read_html()`. It contains two tables:
- Table 0: Study metadata
- Table 1: Individual animal records (419 rows × 6 columns)

## Download

```
https://cebs.niehs.nih.gov/cebs/get_file/accno/3800_7854/file/2010556_Female_Individual_Animal_Survival_Data.xls
```

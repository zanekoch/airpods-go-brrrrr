# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Package Management

Use `uv` for all package management. Never use pip or pip3.

```bash
uv sync                          # Install dependencies
uv run python main.py            # Run the main script
uv run jupyter notebook          # Start Jupyter notebook server
uv add <package>                 # Add a dependency
```

## Project Overview

Statistical survival analysis of NIEHS National Toxicology Program (NTP) Technical Report 596 data — effects of CDMA cell phone radiofrequency radiation on female B6C3F1 mice (419 animals, 4 treatment groups).

## Architecture

- **`/data/`** — Raw `.xls` study data from NIEHS NTP. Parsed with `xlrd`/`pandas`.
- **`/notebooks/survival_summary.ipynb`** — Primary analysis: data cleaning, group summaries, mortality analysis, and Kaplan-Meier survival curves via `lifelines`.
- **`main.py`** — Entry point stub (minimal).

**Key libraries**: `pandas` (data), `lifelines` (survival analysis/K-M curves), `matplotlib` (visualization), `xlrd`/`lxml`/`openpyxl` (Excel parsing).

## Data

The raw data file is `data/TR-596_Technical_Report_Pathology_Tables_and_Curves/2010575_Female_Individual_Animal_Survival_Data.xls`. Key columns: animal ID, treatment group (Vehicle Control / 2.5 / 5 / 10 W/kg), days on study, week of removal, removal reason.

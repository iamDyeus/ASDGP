<div align="center">

# Agentic Synthetic Data Generation Pipeline 

Generate realistic synthetic datasets from a small CSV template using an agentic workflow powered by crewAI and OpenAI.

<br/>

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Agentic](https://img.shields.io/badge/Agentic-crewai-6b48ff)
![Status](https://img.shields.io/badge/status-experimental-orange)

</div>

## Overview

The *ASGDP* analyzes a sample tabular dataset, infers patterns and constraints, generates new rows that preserve structure and relationships, validates quality, and exports results. It’s ideal for test data, demos, and POCs where realistic data is needed without exposing production records.

## How it works

The pipeline uses a sequential multi‑agent crew (see `src/crew.py` and `src/config/*`):

- CSV Data Pattern Analyst → inspects the CSV template and infers schema, types, ranges, formats.
- Synthetic Data Generator → produces N rows following the inferred rules.
- Data Quality Orchestrator → validates consistency, uniqueness, and constraints.
- Multi‑Format Storage Specialist → prepares CSV and JSON outputs for downstream use.

Inputs are provided in `src/main.py` and the sample CSV lives in `assets/sample_data.csv`.

## Project structure

```
.
├─ assets/
│  ├─ sample_data.csv      # your seed/template CSV
│  └─ sample_data.pdf      # example asset (not required by the code path)
├─ src/
│  ├─ main.py              # CLI entry (run/train/replay/test)
│  ├─ crew.py              # crew/agents/tasks wiring
│  └─ config/
│     ├─ agents.yaml       # agent definitions
│     └─ tasks.yaml        # task prompts and outputs
├─ requirements.txt
├─ pyproject.toml
├─ output.txt              # default run output
└─ README.md
```

## Prerequisites

- Python 3.11+
- An OpenAI API key

## Setup

1. Create and activate a virtual environment

- Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

- macOS/Linux (bash/zsh):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Configure environment

Create a `.env` file in the project root with your key:

```env
OPENAI_API_KEY=sk-...
```

## Usage

Place your seed CSV at `assets/sample_data.csv` and adjust `required_rows` in `src/main.py` as needed.

- Generate synthetic data (default flow)

```powershell
python src/main.py run
```


Outputs:

- A consolidated run report is written to `output.txt`.
- The storage specialist agent is instructed to prepare CSV and JSON versions of the dataset; if token usage is a concern, tune `src/config/tasks.yaml` and `src/config/agents.yaml` to streamline formatting or reduce verbosity.

## Configuration tips

- Number of rows: edit `required_rows` in `src/main.py`.
- Models/temperature: see `LLM(model=..., temperature=...)` in `src/crew.py`.
- Task fidelity/output style: edit `src/config/tasks.yaml`.
- Agent behavior and constraints: edit `src/config/agents.yaml`.

## Notes

- Agent Orchestration is provided by [crewai](https://github.com/crewai/crewai).
- The current flow expects a CSV seed file. You can replace `assets/sample_data.csv` with your own template using the same headers/shape you want to emulate.

## Troubleshooting

- Missing API key: set `OPENAI_API_KEY` in your `.env`.
- Rate limits/model errors: try a smaller `required_rows`, lower verbosity, or a lighter model.
- Large CSVs: start with a small representative sample to improve reliability and reduce cost.

## Future features

1. Streamlit-based UI for upload, parameter tuning, and one-click runs.
2. Upload any sample data format (CSV, JSON, Excel, Parquet, PDF) and let the LLM infer structure and build the dataset context automatically.
3. “Ask your synthetic dataset” feature: attach a vector database and enable natural‑language querying over generated data.

## Current System Performance

### Input
```csv
#,Vehicle Description,Device-ID,Date,Time,Odometer Km,Lat/Lon,Address,Latest Batt %,Since Last Check-In
1,EE_WWMNH_A_V_KA53B3470_SUCTION,ee_wwmnh_a_v_ka53b3470_suction,01/01/2014,05:30:18,22823,,,"",0d 00h 00m
2,E11_KA04C5158_JETTING,e11_ka04c5158_jetting,01/01/2014,05:30:20,22358,,,"",0d 18h 07m
3,SW2_KA04AA7685_DESILTING,sw2_ka04aa7685_desilting,01/01/2014,05:30:20,7981,,,"",0d 01h 17m
4,WWMN_CV1_KA53B3464_JETTING,wwmn_cv1_ka53b3464_jetting,01/01/2014,05:30:20,14804,,,"",28d 08h 13m
5,S12_KA05D8083_TANKER,s12_ka05d8083_tanker,01/01/2014,05:30:20,32840,,,"",0d 02h 16m
6,E12_KA04D6648_JETTING,e12_ka04d6648_jetting,01/01/2014,05:30:20,14721,,,"",0d 16h 40m
7,WWMN_CV1_KA04AA9020_DESILTING,wwmn_cv1_ka04aa9020_desilting,01/01/2014,05:30:20,14801,,,"",1d 00h 13m
8,SE5_KA04A3044_JETTING,se5_ka04a3044_jetting,01/01/2014,05:30:22,17052,,,"",0d 00h 03m
9,E21_KA02AC4521_JETTING,e21_ka02ac4521_jetting,01/01/2014,05:30:29,40815,,,"",0d 00h 00m
10,W21_KA04D4156_JETTING,w21_ka04d4156_jetting,01/01/2014,05:30:30,26751,,,"",0d 00h 00m
```

### Output
```csv
Vehicle Description,Device-ID,Date,Time,Odometer Km,Lat/Lon,Address,Latest Batt %,Since Last Check-In
E12_KA05D9999_TANKER,e12_ka05d9999_tanker,03/15/2023,08:45:12,15023,,,,
SW3_KA04B1234_CLEANING,sw3_ka04b1234_cleaning,07/02/2024,12:30:22,25000,,,,
EE_WWMNH_B_V_KA53B1234_SUCTION,ee_wwmnh_b_v_ka53b1234_suction,01/10/2025,09:00:00,32840,,,,
E11_YZ12C5678_JETTING,e11_yz12c5678_jetting,05/21/2023,14:15:30,22358,,,,
SW2_KA04AA7685_DESILTING,sw2_ka04aa7685_desilting,08/04/2024,16:45:18,7981,,,,
WWMN_CV1_KA53B3464_JETTING,wwmn_cv1_ka53b3464_jetting,02/14/2025,07:02:25,14804,,,,
S12_KA05D8083_TANKER,s12_ka05d8083_tanker,08/30/2023,11:20:45,32840,,,,
E13_KA05A1234_VACUUM,e13_ka05a1234_vacuum,04/12/2023,18:05:10,40000,,,,
SW4_KA06C9876_DEBRIS,sw4_ka06c9876_debris,06/22/2023,15:15:00,20500,,,,
EE_WWMNH_A_V_KA53B5678_SUCTION,ee_wwmnh_a_v_ka53b5678_suction,09/01/2025,20:10:09,15000,,,,
E10_KA04D5555_JETTING,e10_ka04d5555_jetting,12/25/2024,13:00:00,30000,,,,
SW1_KA04F1111_CLEANING,sw1_ka04f1111_cleaning,10/10/2023,09:31:22,18050,,,,
WWMN_CV1_KA53B7654_JETTING,wwmn_cv1_ka53b7654_jetting,01/05/2025,14:54:40,21900,,,,
S13_KA05D8888_TANKER,s13_ka05d8888_tanker,11/11/2024,06:45:00,45000,,,,
SW3_KA04E7777_DESILTING,sw3_ka04e7777_desilting,03/30/2025,08:12:18,16000,,,,
EE_WWMNH_C_V_KA53B8888_SUCTION,ee_wwmnh_c_v_ka53b8888_suction,02/18/2024,12:00:00,12000,,,,
S14_KA05D6666_VACUUM,s14_ka05d6666_vacuum,05/30/2023,17:30:30,37000,,,,
SW2_KA04A4444_CLEANING,sw2_ka04a4444_cleaning,06/01/2024,19:45:00,29000,,,,
E12_KA05B5555_JETTING,e12_ka05b5555_jetting,04/01/2025,09:10:10,35000,,,,
```
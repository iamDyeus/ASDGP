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
77,NE2_KA02AC5944_JETTING,ne2_ka02ac5944_jetting,01/01/2014,15:51:40,63270,13.0349/77.5726,Sanjay Nagar,,0d 00h 00m
78,W21_KA04D5305_TANKER,w21_ka04d5305_tanker,01/01/2014,16:04:48,6489,13.0103/77.5673,Malleshwaram,,0d 00h 00m
79,N12_KA04B7114_TANKER,n12_ka04b7114_tanker,01/01/2014,16:04:56,37588,13.0291/77.6107,Shampura,,0d 00h 00m
80,E12_KA04D6650_JETTING,e12_ka04d6650_jetting,01/01/2014,16:05:32,20033,12.9660/77.6788,Keerthi Regency,,0d 17h 30m
81,WWW_V_VV1_KA53B3465_JETTING,www_v_vv1_ka53b3465_jetting,01/01/2014,16:24:02,31739,12.9834/77.5206,Kamakshi Palya,,0d 21h 10m
82,E24_KA04C5159_JETTING,e24_ka04c5159_jetting,01/01/2014,16:24:33,70036,13.0045/77.6674,Kottur,,0d 00h 00m
83,N12_KA04AA1780_DESILTING,n12_ka04aa1780_desilting,01/01/2014,16:33:55,15647,13.0411/77.5882,Hebbal,,0d 16h 40m
84,S11_KA04D4106_JETTING,s11_ka04d4106_jetting,01/01/2014,16:34:12,95417,12.9226/77.5970,Tilak Nagar,,0d 00h 00m
```

### Output
```csv
Vehicle Description,Device-ID,Date,Time,Odometer Km,Lat/Lon,Address,Latest Batt %,Since Last Check-In
NE2_KA02AC5944_JETTING,ne2_ka02ac5944_jetting,03/15/2024,12:45:30,63270,13.0349/77.5726,Sanjay Nagar,85.5,1d 12h 30m
W21_XB03AC1234_TANKER,w21_xb03ac1234_tanker,07/22/2023,08:15:45,45000,28.6139/77.2090,Connaught Place,,2d 05h 15m
NE2_KA02AC1234_JETTING,ne2_ka02ac1234_jetting,11/05/2024,14:30:00,123456,19.0760/72.8777,Mumbai,,0d 00h 45m
W21_XB02AC5678_TANKER,w21_xb02ac5678_tanker,01/10/2025,09:00:00,98765,12.9716/77.5946,Bangalore,60.0,3d 02h 10m
NE2_KA02AC9876_JETTING,ne2_ka02ac9876_jetting,09/12/2023,16:20:15,25000,22.5726/88.3639,Kolkata,75.2,0d 12h 00m
W21_XB01AC4321_TANKER,w21_xb01ac4321_tanker,02/28/2024,11:00:00,30000,13.0827/80.2707,Chennai,,1d 08h 30m
NE2_KA02AC3456_JETTING,ne2_ka02ac3456_jetting,05/20/2024,18:45:00,60000,15.3173/75.7139,Mysore,90.5,2d 00h 15m
W21_XB04AC8765_TANKER,w21_xb04ac8765_tanker,06/30/2023,07:30:00,15000,17.3850/78.4867,Hyderabad,45.0,0d 05h 00m
NE2_KA02AC6543_JETTING,ne2_ka02ac6543_jetting,08/14/2024,19:15:00,40000,26.9124/75.7873,Jaipur,,1d 10h 20m
W21_XB05AC3210_TANKER,w21_xb05ac3210_tanker,04/01/2025,10:30:00,20000,30.7333/76.7794,Chandigarh,80.0,0d 02h 50m
NE2_KA02AC7890_JETTING,ne2_ka02ac7890_jetting,12/25/2023,13:00:00,50000,19.2183/84.5228,Bhubaneswar,,3d 01h 00m
W21_XB06AC0987_TANKER,w21_xb06ac0987_tanker,10/10/2024,15:45:00,35000,11.0168/76.9558,Kochi,55.0,1d 04h 30m
NE2_KA02AC2345_JETTING,ne2_ka02ac2345_jetting,03/30/2024,17:00:00,70000,9.9312/78.1828,Tirunelveli,,2d 12h 05m
W21_XB07AC4567_TANKER,w21_xb07ac4567_tanker,01/15/2025,08:00:00,80000,10.8505/78.6922,Nagercoil,65.0,0d 03h 15m
NE2_KA02AC5678_JETTING,ne2_ka02ac5678_jetting,07/05/2023,14:00:00,90000,15.2993/74.1240,Goa,,1d 06h 45m
W21_XB08AC6789_TANKER,w21_xb08ac6789_tanker,02/20/2024,11:30:00,120000,19.0760/72.8777,Mumbai,70.0,0d 00h 30m
NE2_KA02AC8901_JETTING,ne2_ka02ac8901_jetting,09/30/2024,16:15:00,110000,22.5726/88.3639,Kolkata,,2d 09h 20m
W21_XB09AC1234_TANKER,w21_xb09ac1234_tanker,06/15/2023,09:45:00,130000,28.6139/77.2090,Connaught Place,50.0,1d 05h 00m
NE2_KA02AC5432_JETTING,ne2_ka02ac5432_jetting,11/11/2024,12:00:00,140000,13.0349/77.5726,Sanjay Nagar,95.0,0d 01h 15m
```
<div align="center">

# Agentic Synthetic Data Generation Pipeline 

Generate realistic synthetic datasets from a small CSV template using an agentic workflow powered by crewAI and OpenAI.

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
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

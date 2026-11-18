# FastAPI Learning Projects

A Python learning repository with two FastAPI applications, a model-training notebook, and standalone Pydantic validation examples.

## Contents

| Path | Description |
| --- | --- |
| `main.py` | Patient-record API backed by a local JSON file |
| `app.py` | Insurance-premium prediction API using the saved `model.pkl` artifact |
| `fastapi_ml_model.ipynb` | Notebook for the machine-learning workflow |
| `Pydantic/` | Small examples of validation and computed fields |

Run one API at a time. The patient API and prediction API have different endpoints and data requirements.

## Requirements

Use a Python version compatible with the installed FastAPI and Pydantic releases. Install the runtime packages:

```bash
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

```bash
python -m pip install fastapi "uvicorn[standard]" pydantic pandas scikit-learn
```

## Run an API

From the repository root, start the patient-record example:

```bash
uvicorn main:app --reload
```

Or start the model-backed prediction example instead:

```bash
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation. The prediction API loads `model.pkl` during startup.

## Data and safety

The patient example uses local JSON data and is an educational exercise, not a secure medical-record system. Do not enter real patient information. The checked-in model is a serialized pickle artifact; only load pickle files from sources you trust.

## Project status

This repository collects learning examples. It does not currently include a dependency lockfile, deployment configuration, or a production security setup.

## Author

[Sameer Raza](https://github.com/Sameer-ship-it)

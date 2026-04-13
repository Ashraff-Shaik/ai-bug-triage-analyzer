# AI Bug Triage + Root Cause Analyzer

RAG-based bug triage system using Sentence Transformers, FAISS, and LLM.

## Setup

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser&#10;venv/Scripts/Activate.ps1&#10;pip install -r requirements.txt
streamlit run app.py
```

## Usage

1. Enter bug description
2. Get similar bugs, predicted module, severity, root cause, and fix

## Files
- `data/bugs.csv`: Training dataset
- `src/`: Core components
- `app.py`: Streamlit UI

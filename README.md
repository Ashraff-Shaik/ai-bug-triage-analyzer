# 🪲 AI Bug Triage & Root Cause Analyzer

An AI-powered system that analyzes bug reports and recommends **root causes, severity, and fixes** using NLP and similarity search.

---


## 💡 Problem Statement

Manual bug triage is time-consuming and error-prone. This project automates:

* Bug classification
* Root cause identification
* Fix recommendation

---

## 🧠 How It Works

1. Input bug description
2. Convert to embeddings (Sentence Transformers)
3. Retrieve similar bugs (FAISS)
4. Analyze and generate insights
5. Display results via Streamlit UI

---

## 🛠 Tech Stack

* Python
* Sentence Transformers
* FAISS
* Streamlit

---

## ⚙️ Features

* Semantic similarity search
* Root cause prediction
* Severity & module detection
* Interactive UI for bug analysis

---

## ▶️ Run Locally

```bash
git clone https://github.com/Ashraff-Shaik/ai-bug-triage-analyzer.git
cd ai-bug-triage-analyzer

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Project Structure

```bash
src/
  ├── data_loader.py
  ├── embedding.py
  ├── vector_store.py
  ├── retriever.py
  ├── llm_engine.py
  ├── triage_system.py
```

---

## 🚀 Future Improvements

* Integrate LLM (OpenAI / Ollama)
* Add confidence scoring
* Deploy as web app
* Chat-based interface

---

## 🙌 Author

Ashraff Shaik

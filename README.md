# Fraud Investigation Assistant — GenAI + RAG + HITL (Vertex AI + Streamlit)

This project is a Generative AI–powered Fraud Detection & Investigation Assistant built using **Google Vertex AI**, **Streamlit**, and **BigQuery**. It combines:
- **Gemini 1.5 Pro** for generating fraud investigation summaries
- **RAG (Retrieval-Augmented Generation)** using recent transaction behavior from **BigQuery**
- **LLM-as-a-Judge** to evaluate AI-generated summaries
- **Human-in-the-Loop (HITL)** feedback interface for analysts

---

## Project Structure

```
fraud_genai_app/
├── app.py                  # Streamlit main app
├── fraud_summary.py        # Gemini-based summary generation
├── llm_judge.py            # Evaluates LLM summary using Gemini
├── hitl.py                 # Human review form with feedback
├── rag.py                  # RAG: fetch recent user behavior from BigQuery
├── README.md               # This file
```

---

## How to Run

### 1.  Install Dependencies
```bash
pip install streamlit google-cloud-aiplatform google-cloud-bigquery
```

### 2. Authenticate
```bash
gcloud auth application-default login
```

### 3.  Launch the App
```bash
streamlit run app.py
```

---

##  GCP Setup Required

- Enable **Vertex AI API** and **BigQuery API** in your GCP project.
- Create and populate the `banking.transactions` table in BigQuery with at least:
  - `customer_id`, `timestamp`, `location`, `device`, `amount`
- Update your GCP project ID in:
  - `vertexai.init(...)` in `fraud_summary.py`
  - BigQuery query in `rag.py`

---

##  Features

| Feature                   | Description |
|---------------------------|-------------|
|  RAG                      | Pulls real user behavior from BigQuery to ground the prompt |
|  Gemini 1.5 Pro           | Generates fraud explanation summary |
|  LLM-as-a-Judge           | Evaluates summary for quality |
|  Human-in-the-Loop        | Analysts score and comment on LLM output |
| Review Logging            | Easily extended to log reviews to BigQuery or GCS |

---

## Future Enhancements
- Logging reviews to BigQuery
- Scheduled fine-tuning using low-score feedback
- Role-based access for analysts

---

## Author
Built by [Rekha Suraye], powered by Vertex AI & Streamlit 

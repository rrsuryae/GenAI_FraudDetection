from vertexai.generative_models import GenerativeModel
import vertexai

vertexai.init(project="your-project-id", location="us-central1")

def generate_fraud_summary(txn_data):
    model = GenerativeModel("gemini-1.5-pro-preview-0409")

    template = """
You are a financial fraud investigator assistant. Analyze the suspicious transaction and generate a summary.

Transaction:
- Amount: ${amount}
- Location: ${location}
- Time: ${time}
- Device: ${device}

Customer’s recent behavior:
${user_behavior_summary}

Explain:
1. Why this may be fraudulent
2. Behavioral deviations
3. Suggested next steps for the fraud analyst
"""
    for key, val in txn_data.items():
        template = template.replace("${" + key + "}", val)

    response = model.generate_content(template)
    return template, response.text

import streamlit as st
from fraud_summary import generate_fraud_summary
from llm_judge import evaluate_summary
from hitl import review_form
from rag import get_user_behavior_summary

st.title("🛡️ Fraud Investigation Assistant (GenAI + RAG + HITL)")

customer_id = st.text_input("Customer ID", "12345")
amount = st.text_input("Amount", "$3,400")
location = st.text_input("Location", "Lagos, Nigeria")
time = st.text_input("Time of Transaction", "3:21 AM GMT")
device = st.text_input("Device Used", "Android Unknown Device")

if st.button("Generate Fraud Summary"):
    user_behavior_summary = get_user_behavior_summary(customer_id)

    txn_data = {
        "amount": amount,
        "location": location,
        "time": time,
        "device": device,
        "user_behavior_summary": user_behavior_summary
    }

    fraud_prompt, llm_output = generate_fraud_summary(txn_data)

    st.subheader("🧠 LLM Summary")
    st.write(llm_output)

    st.info("Running LLM-as-a-Judge Evaluation...")
    evaluation = evaluate_summary(fraud_prompt, llm_output)
    st.subheader("✅ LLM-as-a-Judge Evaluation")
    st.write(evaluation)

    st.subheader("🧑‍💼 Human-in-the-Loop Review")
    review_form(customer_id, txn_data, fraud_prompt, llm_output, evaluation)

import streamlit as st

def review_form(customer_id, txn_data, prompt, llm_summary, llm_score):
    with st.form("hitl_review_form"):
        manual_score = st.slider("Manual Score (1–10):", 1, 10, 7)
        feedback = st.text_area("Analyst Feedback:")
        override = st.selectbox("Override decision?", ["No", "Flag as Fraud", "Clear as Safe"])

        submitted = st.form_submit_button("Submit Review")
        if submitted:
            review_log = {
                "customer_id": customer_id,
                "transaction": txn_data,
                "llm_summary": llm_summary,
                "llm_score": llm_score,
                "manual_score": manual_score,
                "manual_feedback": feedback,
                "override_decision": override
            }
            st.success("Review submitted.")
            st.json(review_log)

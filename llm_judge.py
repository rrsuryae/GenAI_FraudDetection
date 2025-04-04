from vertexai.generative_models import GenerativeModel

def evaluate_summary(prompt, summary):
    model = GenerativeModel("gemini-1.5-pro-preview-0409")
    judge_prompt = f"""
You are a quality evaluator reviewing an AI-generated fraud investigation summary.

Here is the original input:
{prompt}

Here is the generated summary:
{summary}

Evaluate the summary based on:
1. Clarity and readability
2. Correctness of reasoning
3. Appropriateness of recommended actions

Respond with:
- A score between 1 and 10
- A short explanation for the score
"""
    response = model.generate_content(judge_prompt)
    return response.text

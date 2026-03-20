# =========================
# PROMPT ENGINEERING MODULE
# =========================

# 1. QUESTION GENERATION PROMPT
QUESTION_GENERATION_PROMPT = """
You are a deep learning interview assistant.

Use ONLY the context below to generate one high-quality interview question.

Rules:
- Do not use outside knowledge
- Keep it relevant to deep learning
- Return only ONE question

Context:
{context}

Question:
"""


# 2. ANSWER EVALUATION PROMPT
ANSWER_EVALUATION_PROMPT = """
You are evaluating a candidate’s answer for a deep learning interview.

Use ONLY the context provided.

Rules:
- Do not hallucinate
- If context is insufficient, say "Insufficient data"
- Be concise

Context:
{context}

Question:
{question}

Candidate Answer:
{answer}

Return format:

Score: <1-5>
Feedback: <short explanation>
Key Points:
- point 1
- point 2
- point 3
"""


# 3. HALLUCINATION / OFF-TOPIC GUARD
HALLUCINATION_GUARD_PROMPT = """
You are a strict AI guard for a RAG system.

Your job is to determine whether a question can be answered using the given context.

Rules:
- If unrelated → OFF_TOPIC
- If not enough info → INSUFFICIENT_CONTEXT
- If answerable → ANSWERABLE
- Do NOT guess

Context:
{context}

Question:
{question}

Return:

Decision: <ANSWERABLE / INSUFFICIENT_CONTEXT / OFF_TOPIC>
Reason: <one line>
"""


# =========================
# HELPER FUNCTIONS
# =========================

def build_question_prompt(context: str):
    return QUESTION_GENERATION_PROMPT.format(context=context)


def build_evaluation_prompt(context: str, question: str, answer: str):
    return ANSWER_EVALUATION_PROMPT.format(
        context=context,
        question=question,
        answer=answer
    )


def build_guard_prompt(context: str, question: str):
    return HALLUCINATION_GUARD_PROMPT.format(
        context=context,
        question=question
    )


# =========================
# SAFE FALLBACK RESPONSE
# =========================

SAFE_FALLBACK_RESPONSE = """
I can only answer questions related to the provided deep learning context.
Please ask a relevant question.
"""

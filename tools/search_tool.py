from google import genai
from config.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL = "gemini-2.5-flash"


def ask_pdf(pdf_text, question):
    prompt = f"""
You are an AI Study Assistant.

Below is a student's study material.

Answer ONLY using the provided content.

If the answer is not present,
say:
"I couldn't find this information in the uploaded PDF."

-------------------------

Study Material

{pdf_text}

-------------------------

Question

{question}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return response.text
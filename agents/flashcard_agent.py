from google import genai
from config.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL = "gemini-2.5-flash"


def generate_flashcards(source, num_cards):
    prompt = f"""
You are an expert teacher.

Create {num_cards} study flashcards from the study material below.

Rules:
- Each flashcard must have:
    Question:
    Answer:
- Keep answers short (1-3 sentences).
- Number each flashcard.
- Do not include unnecessary explanations.

Study Material:

{source}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return response.text
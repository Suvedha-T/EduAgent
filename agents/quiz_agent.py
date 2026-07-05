from google import genai
from config.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL = "gemini-2.5-flash"


def generate_quiz(
    source,
    quiz_type,
    num_questions,
    difficulty,
):
    prompt = f"""
You are an expert teacher.

Create {num_questions} {quiz_type} questions.

Difficulty:
{difficulty}

Study Material:

{source}

Rules:

1. Number each question.
2. Provide four options if MCQ.
3. Give the correct answer after every question.
4. Use clear formatting.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return response.text
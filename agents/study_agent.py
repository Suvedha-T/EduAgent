from google import genai
from config.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-2.5-flash"


def ask_study_agent(question: str) -> str:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=question,
    )
    return response.text
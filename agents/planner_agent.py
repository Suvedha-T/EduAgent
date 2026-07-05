from google import genai
from config.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL = "gemini-2.5-flash"


def generate_study_plan(subjects, exam_date, hours):
    prompt = f"""
You are an expert academic mentor.

Create a personalized study timetable.

Subjects:
{subjects}

Exam Date:
{exam_date}

Daily Study Hours:
{hours}

Instructions:
- Divide study time evenly.
- Include revision days.
- Include short breaks.
- Present the schedule day by day.
- Use markdown formatting.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return response.text
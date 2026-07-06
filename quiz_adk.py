from google.adk.agents import Agent
from agents.quiz_agent import generate_quiz

quiz_agent = Agent(
    name="QuizAgent",
    description="Generates quizzes."
)

def run(prompt):
    return generate_quiz(
        prompt,
        "MCQ",
        10,
        "Medium"
    )
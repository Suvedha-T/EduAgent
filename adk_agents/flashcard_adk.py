from google.adk.agents import Agent
from agents.flashcard_agent import generate_flashcards

flashcard_agent = Agent(
    name="FlashcardAgent",
    description="Creates flashcards."
)

def run(prompt):
    return generate_flashcards(
        prompt,
        10
    )
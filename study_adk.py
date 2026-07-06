from google.adk.agents import Agent
from agents.study_agent import ask_study_agent

study_agent = Agent(
    name="StudyAgent",
    description="Explains concepts and answers academic questions."
)

def run(prompt):
    return ask_study_agent(prompt)
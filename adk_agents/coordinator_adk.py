from google.adk.agents import Agent

from adk_agents.study_adk import run as study_run
from adk_agents.quiz_adk import run as quiz_run
from adk_agents.flashcard_adk import run as flashcard_run
from adk_agents.planner_adk import run as planner_run

from agents.router import detect_agent

coordinator = Agent(
    name="CoordinatorAgent",
    description="Routes requests to the correct AI agent."
)

def run(prompt):

    agent = detect_agent(prompt)

    if agent == "study":
        return study_run(prompt)

    elif agent == "quiz":
        return quiz_run(prompt)

    elif agent == "flashcard":
        return flashcard_run(prompt)

    elif agent == "planner":
        return planner_run(prompt)

    return "No suitable agent found."
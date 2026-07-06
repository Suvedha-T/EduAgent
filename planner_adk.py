from google.adk.agents import Agent
from agents.planner_agent import generate_study_plan

planner_agent = Agent(
    name="PlannerAgent",
    description="Creates personalized study plans."
)

def run(subjects):
    return generate_study_plan(
        subjects,
        "Next Month",
        4
    )
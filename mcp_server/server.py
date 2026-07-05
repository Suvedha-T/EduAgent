from mcp.server.fastmcp import FastMCP

from tools.pdf_tool import extract_pdf_text
from agents.quiz_agent import generate_quiz
from agents.flashcard_agent import generate_flashcards

mcp = FastMCP("EduAgent Tools")


@mcp.tool()
def read_pdf(path: str):
    """Extract text from a PDF."""
    return extract_pdf_text(path)


@mcp.tool()
def create_quiz(topic: str):
    """Generate quiz questions."""
    return generate_quiz(
        topic,
        "MCQ",
        10,
        "Medium",
    )


@mcp.tool()
def create_flashcards(topic: str):
    """Generate flashcards."""
    return generate_flashcards(
        topic,
        10,
    )


if __name__ == "__main__":
    mcp.run()
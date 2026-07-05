import os
import streamlit as st

from agents.study_agent import ask_study_agent
from tools.pdf_tool import extract_pdf_text
from tools.search_tool import ask_pdf
from agents.quiz_agent import generate_quiz
from agents.flashcard_agent import generate_flashcards
from agents.planner_agent import generate_study_plan
from agents.router import detect_agent

# -----------------------------
# Configuration
# -----------------------------
UPLOAD_FOLDER = "database/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(
    page_title="EduAgent",
    page_icon="🎓",
    layout="wide",
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎓 EduAgent")

page = st.sidebar.radio(
    "Select Mode",
    [
        "Smart Assistant",
        "Study Assistant",
        "Quiz",
        "Flashcards",
        "Study Planner",
        "Resources",
    ],
)

st.title("🎓 EduAgent")

# ==================================================
# STUDY ASSISTANT
# ==================================================
if page == "Study Assistant":

    st.header("AI Study Mentor")

    question = st.text_area(
        "Ask your question",
        height=150,
    )

    if st.button("Ask"):

        if question.strip():

            with st.spinner("Thinking..."):

                answer = ask_study_agent(question)

            st.write(answer)

# ==================================================
# RESOURCES
# ==================================================
elif page == "Resources":

    st.header("📄 Study Resources")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        save_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        # Save PDF only once
        if (
            "current_pdf" not in st.session_state
            or st.session_state["current_pdf"] != uploaded_file.name
        ):

            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            text = extract_pdf_text(save_path)

            st.session_state["pdf_text"] = text
            st.session_state["current_pdf"] = uploaded_file.name

        st.success("PDF uploaded successfully!")

        st.write("**File:**", uploaded_file.name)

        with st.expander("Preview Extracted Text"):

            st.write(st.session_state["pdf_text"][:2000])

        st.divider()

        pdf_question = st.text_input(
            "Ask a question about this PDF"
        )

        if st.button("Ask PDF"):

            if pdf_question.strip():

                with st.spinner("Thinking..."):

                    answer = ask_pdf(
                        st.session_state["pdf_text"],
                        pdf_question
                    )

                st.subheader("Answer")

                st.write(answer)

# ==================================================
# PLACEHOLDER PAGES
# ==================================================
elif page == "Quiz":

    st.header("📝 AI Quiz Generator")

    source_option = st.radio(
        "Quiz Source",
        [
            "Topic",
            "Uploaded PDF"
        ]
    )

    if source_option == "Topic":

        source = st.text_area(
            "Enter Topic"
        )

    else:

        if "pdf_text" not in st.session_state:

            st.warning("Please upload a PDF first.")

            st.stop()

        source = st.session_state["pdf_text"]

    quiz_type = st.selectbox(
        "Quiz Type",
        [
            "MCQ",
            "True/False",
            "Short Answer"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    num_questions = st.slider(
        "Number of Questions",
        5,
        20,
        10,
    )

    if st.button("Generate Quiz"):

        with st.spinner("Generating Quiz..."):

            quiz = generate_quiz(
                source,
                quiz_type,
                num_questions,
                difficulty,
            )

        st.markdown(quiz)

elif page == "Flashcards":

    st.header("🗂 AI Flashcard Generator")

    source_option = st.radio(
        "Flashcard Source",
        [
            "Topic",
            "Uploaded PDF"
        ],
        key="flashcard_source"
    )

    if source_option == "Topic":

        source = st.text_area(
            "Enter Topic",
            key="flashcard_topic"
        )

    else:

        if "pdf_text" not in st.session_state:

            st.warning("Please upload a PDF first.")

            st.stop()

        source = st.session_state["pdf_text"]

    num_cards = st.slider(
        "Number of Flashcards",
        5,
        20,
        10,
        key="flashcard_slider"
    )

    if st.button("Generate Flashcards"):

        with st.spinner("Generating Flashcards..."):

            cards = generate_flashcards(
                source,
                num_cards,
            )

        st.markdown(cards)

elif page == "Study Planner":

    st.header("📅 AI Study Planner")

    subjects = st.text_area(
        "Enter subjects (one per line)"
    )

    exam_date = st.date_input(
        "Exam Date"
    )

    study_hours = st.slider(
        "Daily Study Hours",
        1,
        12,
        4
    )

    if st.button("Generate Study Plan"):

        with st.spinner("Planning your schedule..."):

            plan = generate_study_plan(
                subjects,
                exam_date,
                study_hours
            )

        st.markdown(plan)

if page == "Smart Assistant":

    st.header("🤖 EduAgent Smart Assistant")

    prompt = st.text_area(
        "What would you like me to do?"
    )

    if st.button("Run"):

        agent = detect_agent(prompt)

        st.success(f"Coordinator selected: {agent.upper()} Agent")

        if agent == "study":

            answer = ask_study_agent(prompt)

            st.write(answer)

        elif agent == "quiz":

            quiz = generate_quiz(
                prompt,
                "MCQ",
                10,
                "Medium",
            )

            st.write(quiz)

        elif agent == "flashcard":

            cards = generate_flashcards(
                prompt,
                10,
            )

            st.write(cards)

        elif agent == "planner":

            plan = generate_study_plan(
                prompt,
                "Next Month",
                4,
            )

            st.write(plan)

        elif agent == "resource":

            if "pdf_text" not in st.session_state:

                st.warning("Upload a PDF first.")

            else:

                answer = ask_pdf(
                    st.session_state["pdf_text"],
                    prompt,
                )

                st.write(answer)
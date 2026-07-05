# 🎓 EduAgent – A Multi-Agent AI Study Mentor for Students

## 📌 Overview

EduAgent is a Multi-Agent AI Study Mentor designed to help students prepare for examinations efficiently.

The application integrates multiple specialized AI agents that collaborate to assist students with learning, revision, quiz generation, flashcard creation, study planning, and PDF-based question answering.

Built using **Google Gemini**, **Google ADK concepts**, and **Streamlit**.

---

# 🚀 Features

### 📖 Study Assistant
- Explains difficult concepts
- Answers academic questions
- Provides simple explanations

---

### 📄 PDF Resource Agent
- Upload study materials
- Extract text automatically
- Ask questions from uploaded PDFs

---

### 📝 Quiz Generator
Generate:
- MCQs
- True/False
- Short Answer Questions

Difficulty Levels:
- Easy
- Medium
- Hard

---

### 🗂 Flashcard Generator

Automatically creates revision flashcards from

- Topics
- Uploaded PDFs

---

### 📅 Study Planner

Generates personalized study schedules based on

- Subjects
- Exam Date
- Daily Study Hours

---

### 🤖 Smart Coordinator

Routes user requests to the appropriate AI module.

Examples:

- Explain Machine Learning
- Generate 20 MCQs
- Create Flashcards
- Prepare Study Plan

---

# 🏗 Project Architecture

Student

↓

Streamlit UI

↓

Coordinator Agent

↓

Study Agent

Quiz Agent

Flashcard Agent

Planner Agent

Resource Agent

↓

Google Gemini

---

# 🛠 Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google ADK Concepts
- PyPDF
- Git
- GitHub

---

# 📂 Project Structure

EduAgent/
│
├── agents/
├── config/
├── tools/
├── database/
├── logs/
├── utils/
├── app.py
├── README.md
├── requirements.txt

---

# ▶ Installation

Clone the repository

git clone https://github.com/Suvedha-T/EduAgent.git

Install dependencies

pip install -r requirements.txt

Run

streamlit run app.py

---

# 🔐 Security

API Keys are stored securely using

.env

and are excluded using

.gitignore

---

# 🌟 Future Scope

- Voice-based interaction
- OCR for handwritten notes
- AI Exam Predictor
- Mobile Application
- Cloud Database Integration

---

# 👩‍💻 Author

Suvedha T

B.E. CSE (Artificial Intelligence & Machine Learning)

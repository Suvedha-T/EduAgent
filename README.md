# 🎓 EduAgent – A Multi-Agent AI Study Mentor for Students

> An AI-powered study companion that helps students learn smarter through multiple specialized AI agents.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_2.5_Flash-green)
![Google ADK](https://img.shields.io/badge/Google-ADK-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📌 Problem Statement

Students often struggle to prepare effectively for examinations because they need multiple resources for learning, revision, quizzes, flashcards, and study planning.

Existing solutions usually solve only one problem at a time.

EduAgent combines these learning tasks into a single AI-powered multi-agent educational platform.

---

# 💡 Solution

EduAgent is a Multi-Agent AI Study Mentor that intelligently routes student requests to specialized AI agents.

Each agent focuses on one educational task while the Coordinator Agent selects the appropriate agent based on the student's request.

This modular architecture makes the system scalable, reusable, and easier to maintain.

---

# 🚀 Features

## 📖 Study Assistant

- Explain concepts
- Answer academic questions
- Simplify difficult topics

---

## 📄 PDF Resource Agent

- Upload study notes
- Extract text from PDFs
- Ask questions from uploaded notes

---

## 📝 Quiz Generator

Generate

- MCQs
- True/False
- Short Answer Questions

Difficulty Levels

- Easy
- Medium
- Hard

---

## 🗂 Flashcard Generator

Automatically generates revision flashcards from

- Topics
- Uploaded PDFs

---

## 📅 Study Planner

Creates personalized study plans using

- Subjects
- Exam Date
- Daily Study Hours

---

## 🤖 Smart Coordinator Agent

Automatically routes user requests to the appropriate specialized agent.

Example

```
Explain Machine Learning
```

↓

Study Agent

```
Generate 20 MCQs
```

↓

Quiz Agent

```
Create Flashcards
```

↓

Flashcard Agent

---

# 🏗 Architecture

> Insert your Architecture Diagram here.

---

# 🧠 Multi-Agent Architecture

EduAgent consists of

- Coordinator Agent
- Study Agent
- Quiz Agent
- Flashcard Agent
- Study Planner Agent
- Resource Agent

Each agent performs one specialized educational task.

---

# 🛠 Technology Stack

## Frontend

- Streamlit

## Backend

- Python

## AI

- Google Gemini 2.5 Flash

## Agent Framework

- Google ADK

## PDF Processing

- PyPDF

---

# 📂 Folder Structure

```text
EduAgent
│
├── agents
├── adk_agents
├── config
├── database
├── logs
├── prompts
├── tools
├── utils
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔒 Security

The project follows secure development practices.

- API Keys stored in `.env`
- `.env` excluded using `.gitignore`
- No credentials committed to GitHub

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/EduAgent.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📷 Screenshots

Add screenshots here

- Home Page
- Study Assistant
- Quiz Generator
- Flashcards
- Study Planner
- PDF Q&A

---

# 🌱 Future Enhancements

- Voice Assistant
- Mobile Application
- OCR for Handwritten Notes
- Student Progress Analytics
- Cloud Database Integration

---

# 🏆 Kaggle AI Agents Capstone

This project was developed as part of the

**AI Agents: Intensive Vibe Coding Capstone Project**

using Google AI technologies.

---

# 👩‍💻 Author

**Suvedha T**

B.E. Artificial Intelligence & Machine Learning

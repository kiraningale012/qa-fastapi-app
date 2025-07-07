# 🧠 Question Answering System (FastAPI + Transformers)

This project is a **Question Answering Web App** built with **FastAPI** and **Hugging Face Transformers**. It allows users to input a paragraph of context and ask natural language questions. The system responds with detailed, human-like answers using a pretrained language model like `google/flan-t5-large`.

---

## 🚀 Features

- ⚡ Detailed answer generation using LLMs (FLAN-T5)
- 📡 REST API endpoint for QA
- 🌐 Clean HTML UI with AJAX (Bootstrap + Fetch API)
- 🧱 Modular folder structure (router, service, schema, utility)
- 🧠 Context-aware, human-like answers to programming/documentation queries

---

## 🏗️ Project Structure
qa-fastapi-app/
├── main.py # App entry point
├── router/
│ └── router.py # API routes
├── services/
│ └── service.py # Model loading and QA logic
├── schema/
│ └── schema.py # Pydantic models
├── utility/
│ └── utility.py # Prompt formatter / helpers
├── templates/
│ └── index.html # HTML frontend
├── static/ # Static files (CSS/JS/images if needed)
├── README.md # Project documentation
└── requirements.txt # Python dependencies


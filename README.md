👩‍⚕️ Medical-Femino
Medical-Femino is an AI-powered platform focused on women's health, safety, and wellness. From intelligent medical assistance to image-based diagnosis and real-time emergency alerts, the app is a comprehensive health companion, leveraging state-of-the-art LLMs and AI tools.

🧠 Core Features
💬 Dr. Femino – AI Chatbot for Women’s Health
An intelligent chatbot built with:

OpenAI's LLMs

LangChain for conversational flow

Prompt engineering and retrieval tools for contextual medical advice

What it does:

Answers questions related to gynecology, menstrual health, pregnancy, and general female wellness

Offers medically sound responses in an empathetic tone

Private, anonymous, and always available

🩻 Femiai – Image-Based Diagnosis with Privacy
Securely encodes images uploaded by the user (e.g., skin rashes, visible symptoms)

Parses and interprets the image using LLaMaParser

Provides diagnostic suggestions based on the image + user query

Ensures end-to-end privacy using encryption and secure data channels

🆘 AI Alert – One-Click Emergency Safety System
Sends instant alert messages to:

Family members

Nearest women’s care centers

Local police stations

Works with geolocation and SMS APIs

Designed for fast response in distress situations

🛠️ Tech Stack
AI & NLP
OpenAI GPT-4

LangChain

LLaMaParser

PromptLayer, ChromaDB for context management

Backend
Python, Flask

FastAPI for certain LLM routes

Frontend
HTML/CSS/JavaScript

Optional React integration for chat UI

Security & APIs
Encryption Libraries (e.g., Fernet)

Twilio / Fast2SMS for alerts

Geolocation APIs (Google Maps API or similar)

📦 Folder Structure
cpp
Copy code
Medical-Femino/
│
├── backend/
│   ├── chatbot/
│   ├── femiai/
│   └── alert/
│
├── frontend/
│   ├── templates/
│   └── static/
│
├── requirements.txt
└── README.md
⚙️ Getting Started
Clone the repo:

bash
Copy code
git clone https://github.com/simran911/Medical-Femino.git
cd Medical-Femino
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
python app.py

🌐 Live Demo (if available)
Coming Soon...

🙋‍♀️ Built For
Women of all ages looking for private, reliable, and intelligent healthcare support and safety assistance.

🤝 Contributing
PRs are welcome! Feel free to fork the project and submit enhancements, especially around:

Expanding the knowledge base for Dr.Femino

Improving image processing models

Adding more alert integrations

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.


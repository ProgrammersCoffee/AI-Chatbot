# 🤖 AI Chatbot using FastAPI, React & Groq API

An intelligent AI chatbot built with **Python FastAPI**, **React.js**, and **Groq API (Llama 3.1)** for real-time conversational AI.

This project demonstrates how to build a **full-stack AI chatbot application** with a modern frontend and scalable backend architecture.

---

## 🚀 Features

✅ Real-time AI conversation
✅ FastAPI backend API
✅ React frontend UI
✅ Groq API integration (Llama 3.1 Model)
✅ Chat history management
✅ Responsive dark-mode chatbot interface
✅ REST API communication between frontend and backend
✅ Error handling & API validation

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Groq API
* Pydantic
* Uvicorn
* dotenv

### Frontend

* React.js
* Vite
* CSS3

---

## 📂 Project Structure

```bash
simple_chatbot/
│── backend/
│   ├── app.py
│   ├── .env
│   ├── requirements.txt
│
│── frontend/
│   └── chatbot_ui/
│       ├── src/
│       │   ├── App.jsx
│       │   ├── App.css
│       │   └── main.jsx
│       ├── package.json
│       └── vite.config.js
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ProgrammersCoffee/simple_chatbot.git
cd simple_chatbot
---
 
### 2️⃣ Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run FastAPI server:

```bash
python -m uvicorn app:app --reload
```

Backend runs on:

```txt
http://127.0.0.1:8000
```

---

### 3️⃣ Frontend Setup

Navigate to frontend:

```bash
cd frontend/chatbot_ui
```

Install dependencies:

```bash
npm install
```

Run React application:

```bash
npm run dev
```

Frontend runs on:

```txt
http://localhost:5173
```

---

## 🔌 API Endpoint

### Chat Endpoint

**POST** `/chat/`

Request Body:

```json
{
  "role": "user",
  "message": "Hello"
}
```

Response:

```json
{
  "response": "Hello! How can I help you?"
}
```

---

## 🧠 How It Works

1. User sends a message from React UI
2. Request is sent to FastAPI backend
3. FastAPI communicates with Groq API (Llama 3.1)
4. AI response is generated
5. Response is returned to frontend and displayed in chat

---

## 📸 Project Preview

Add screenshots of your chatbot UI here. 

Example:
![Chatbot Screenshot]("chatbot1.jpeg")
![Chatbot Screenshot]("chatbot2.jpeg")
![Chatbot Screenshot]("chatbot3.jpeg")


---

## 🎯 Future Improvements

* Restaurant AI Ordering System
* Voice Assistant Support
* Database Integration
* Multi-user Conversations
* Authentication System
* Docker Deployment
* Cloud Hosting (AWS / Render)

---

## 👨‍💻 Author

**Mohamed Esmael**
AI Engineer | Machine Learning Enthusiast

### Connect with me

* LinkedIn: https://www.linkedin.com/in/muhamed-esmeal-224248268/
* GitHub: https://github.com/ProgrammersCoffee

---
 
## ⭐ If you found this project useful, give it a star on GitHub!

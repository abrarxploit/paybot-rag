# 💳 PayBot — Razorpay Docs AI Assistant (RAG Chatbot)

> Ask anything about Razorpay APIs and get accurate, source-backed answers using AI + your own documentation.

---

## 📸 Demo

![Demo](<img width="1919" height="1079" alt="Screenshot 2026-04-29 135403" src="https://github.com/user-attachments/assets/88b5a6b7-5955-4524-a224-1949058aadc1" />)

---

## 🧠 What This Project Does

This is a Retrieval-Augmented Generation (RAG) chatbot that:

- Reads Razorpay docs (.txt)
- Converts them into embeddings
- Stores them in ChromaDB
- Retrieves relevant context
- Uses Gemini AI to answer ONLY from docs

If answer is not found → "I don’t have that info."

---

## ⚙️ Tech Stack

- Python 3.10+
- Streamlit
- ChromaDB
- Sentence Transformers
- Google Gemini API

---

## 📁 Project Structure

```
paybot/
├── app.py
├── rag.py
├── ingest.py
├── requirements.txt
├── .env
├── docs/
├── chroma_db/
└── screenshots/
    └── demo.png
```

---

## ⚡ Run in 2 Minutes

### 1. Clone

```
git clone https://github.com/your-username/paybot.git
cd paybot
```

### 2. Create venv

```
python -m venv venv
```

Activate:

PowerShell:

```
.\venv\Scripts\Activate.ps1
```

CMD:

```
venv\Scripts\activate
```

---

### 3. Install

```
pip install -r requirements.txt
```

---

### 4. Add API Key

Create `.env`:

```
GEMINI_API_KEY=your_key_here
```

---

### 5. Add Docs

Put `.txt` files in `docs/`

---

### 6. Build DB

```
python ingest.py
```

---

### 7. Run

```
python -m streamlit run app.py
```

Open: http://localhost:8501

---

## ❗ Troubleshooting

Execution policy:

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Rebuild DB:

```
delete chroma_db/
python ingest.py
```

---

## 👨‍💻 Author

Abrar Shabir Dar

---

## 📜 License

MIT

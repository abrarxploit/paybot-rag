# 💳 PayBot — Razorpay Docs RAG Chatbot

> An AI-powered chatbot that answers questions about Razorpay APIs using Retrieval-Augmented Generation (RAG) — no hallucinations, only answers grounded in real Razorpay documentation.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-green.svg)](https://chromadb.com)
[![Gemini](https://img.shields.io/badge/Google-Gemini_API-orange.svg)](https://aistudio.google.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<br>
---

## 🛠️ Tech Stack Used

| Layer | Tool | Details |
|---|---|---|
| Embeddings | sentence-transformers | all-MiniLM-L6-v2 model, runs 100% locally |
| Vector DB | ChromaDB | Persistent local storage, no cloud needed |
| LLM | Google Gemini 2.5 Flash Lite | Free tier, no credit card required |
| UI | Streamlit | Clean Python web interface |
| Language | Python 3.10+ | Industry standard for AI/ML |

<br>

## 🧠 What is RAG?

Retrieval-Augmented Generation (RAG) is an AI architecture that combines:
- A Vector Database — stores your documents as mathematical embeddings
- An LLM — generates human-readable answers

Instead of relying on the LLM's training data (which may be outdated or wrong), RAG retrieves relevant chunks from your own documents and forces the LLM to answer only from those chunks — making every answer accurate and hallucination-free.

Your Question
     ↓
[Embed Query] ──── sentence-transformers (runs locally, FREE)
     ↓
[Search Vector DB] ── ChromaDB (local persistent storage)
     ↓
[Retrieve Top 5 Chunks] ── most relevant passages from Razorpay docs
     ↓
[Build Grounded Prompt] ── "Answer ONLY using this context: ..."
     ↓
[Gemini LLM] ── generates answer using ONLY retrieved context
     ↓
✅ Accurate Answer + Source Chunks displayed to user
<br>

## 📸 Demo

<img width="1919" height="1079" alt="Screenshot 2026-04-29 135403" src="https://github.com/user-attachments/assets/08e46639-c07f-4042-9563-c0bf3be7e756" />


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


## 📁 Project Structure

```
paybot/
├── app.py         #Streamlit UI- Chat Interface
├── rag.py         # Core RAG logic
├── ingest.py      #Document ingestion- chunks + embeds docs
├── requirements.txt
├── .env           #Place your API Key here
├── docs/          #Razorpay knowledge base
├── chroma_db/     #Auto created by ingest.py

```

---

## ✅ Prerequisites

Before starting, make sure you have:

- [ ] Python 3.10+ → [Download](https://www.python.org/downloads/) *(during install, check "Add to PATH")*
- [ ] Free Gemini API Key → [Get it here](https://aistudio.google.com) *(no credit card needed)*
- [ ] VS Code → [Download](https://code.visualstudio.com/) *(recommended editor)*

<br>

## 🚀 Installation — Complete Step by Step

### Step 1 — Download this project

Option A — Download ZIP (easiest, no Git needed):
1. Click the green **<> Code** button at top of this page
2. Click **Download ZIP**
3. Right click thExtract Allct All**
4. Open the extracted paybot-rag-main Option B — Clone with Git:h Git:**
git clone https://github.com/abrarxploit/paybot-rag.git
cd paybot-rag
---

### Step 2 — Open terminal inside the project Windows (easiest way): way):**
1. Open the project folder in File Explorer
2. Click the address bar at top
3. Type cmd anEnter*Enter**
4. Terminal opens directly in that foVS Code: Code:**
1. Open VS Code → File → Open Folder → select paybot-rag
2Ctrl + trl + ** to open terminal

---

### Step 3 — Install all dependencies

``bash
pip install -r requirements.txt

> ⏳ First time takes 2-3 minutes — downloads the embedding model (~80MB). Wait for it to complete fully.

Expected output:
Successfully installed chromadb streamlit google-generativeai sentence-transformers ...

---

### Step 4 — Set up your Gemini API Key

**Get your free key:**
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Sign in with Google
3. Click **"Get API Key"** → **"Create API Key"**
4. Copy the key (looks like: `AIzaSyXXXXXXXXXXXXX`)

**Add it to the project:**

Create a new file called `.env` in the project root folder and add:

GEMINI_API_KEY=your_actual_key_here

> ⚠️ **Never share this file. Never upload it to GitHub.** It's already in `.gitignore` so it won't upload accidentally.

---

### Step 5 — Add Razorpay documentation to `docs/` folder

The bot answers from whatever documents you give it. Here's how to add docs:

1. Open any Razorpay docs page e.g. [razorpay.com/docs/payments](https://razorpay.com/docs/payments)
2. Press **`Ctrl+A`** (select all) → **`Ctrl+C`** (copy)
3. Open Notepad → **`Ctrl+V`** (paste)
4. Save as `razorpay_payments.txt` inside the `docs/` folder
5. Repeat for more pages:

| URL | Save as |
|---|---|
| razorpay.com/docs/payments | `razorpay_payments.txt` |
| razorpay.com/docs/orders | `razorpay_orders.txt` |
| razorpay.com/docs/refunds | `razorpay_refunds.txt` |
| razorpay.com/docs/payment-links | `razorpay_links.txt` |
| razorpay.com/docs/webhooks | `razorpay_webhooks.txt` |
| razorpay.com/docs/subscriptions | `razorpay_subscriptions.txt` |

> 💡 More pages = smarter bot. Even 2-3 pages works fine to start.

---

### Step 6 — Build the Vector Database

bash
python ingest.py

Expected output:
✅ Ingested 12 chunks from ./docs/razorpay_payments.txt
✅ Ingested 9 chunks from ./docs/razorpay_orders.txt
✅ Ingested 7 chunks from ./docs/razorpay_refunds.txt
...
🎉 All done! Vector DB is ready.

> 📌 Run this again whenever you add new `.txt` files. Delete the `chroma_db/` folder first to avoid duplicates.

---

### Step 7 — Launch PayBot 🚀

bash
python -m streamlit run app.py

Your browser opens automatically at **`http://localhost:8501`**

Start asking questions like:
- *"What is Razorpay?"*
- *"How do I create a payment link?"*
- *"What payment methods does Razorpay support?"*
- *"How do refunds work?"*
- *"What are webhooks?"*

<br>

## 🔧 Configuration & Tuning

**`ingest.py` — Chunk size** (how much text per piece):
python
# Default — balanced
chunk_size=800, overlap=150

# For more`rag.py` — Number of chunks retrieved:=200

**`rag.py` — Number of chunks retrieved:**
python
# Default
def retrieve(query, top_k=5):

# For broader answers
def retrieve(query, top_k=7):
`

<br>
## 👨‍💻 Author

Abrar Shabir Dar

---

## 📜 License

MIT

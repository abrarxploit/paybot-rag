paybot-rag/
│
├── app.py                  # Streamlit UI — chat interface
├── rag.py                  # Core RAG logic — retrieval + generation
├── ingest.py               # Document ingestion — chunks + embeds docs
├── requirements.txt        # All dependencies
├── .env                    # Your API key (create this yourself)
├── .gitignore              # Prevents secrets from being uploaded
│
├── docs/                   # Put your Razorpay .txt files here
│   └── razorpay_payments.txt
│
├── chroma_db/              # Auto-created when you run ingest.py
│   └── ...
│

<br>

## ❓ Troubleshooting

| Error | Fix |
|---|---|
| streamlit not recognized | Use python -m streamlit run app.py instead |
| GEMINI_API_KEY not found | Make sure .env file exists with your key |
| quota exceeded | You hit free tier limit — wait a few minutes and retry |
| Empty file error | Open the .txt file — if blank, re-copy the docs page |
| chroma_db already exists | Delete chroma_db/ folder and run python ingest.py again |
| module not found | Run pip install -r requirements.txt again |

<br>
## Working Screenshot
<img width="1919" height="1079" alt="Screenshot 2026-04-29 135403" src="https://github.com/user-attachments/assets/7482ab0e-b588-40bc-935e-64850f35f2a4" />


## 🔧 Configuration

You can tune these settings for better results:

**In ingest.py** — chunk size controls how much text each piece contains:
# Larger = more context per answer, but slower
chunk_size=800, overlap=150
**In `rag.py** — top_k controls how many chunks are retrieved:
``python
# Higher = more context, but may hit token limits
def retrieve(query, top_k=5):
`

<br>

## 🤝 Contributing

1. Fork this repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Push and open a Pull Request

<br>

## 📄 License

MIT License — free to use, modify, and distribute.

<br>

## 👤 Abrar*Abrar**
- GitHub: [@abrarxploit](https://github.com/abrarxploit)
- Built as part of Razorpay AI Engineer placement preparation

<br>

--What is RAG?s RAG?** Retrieval-Augmented Generation combines a vector database (for finding relevant information) with an LLM (for generating human-readable answers). Instead of relying on the LLM's training data, RAG grounds every answer in your actual documents — making it accurate, up-to-date, and hallucination-free.

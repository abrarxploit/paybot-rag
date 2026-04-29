import os
import chromadb
from sentence_transformers import SentenceTransformer

# Runs locally on your laptop — FREE
embedder = SentenceTransformer("all-MiniLM-L6-v2")

chroma = chromadb.PersistentClient(path="./chroma_db")
collection = chroma.get_or_create_collection("razorpay_docs")

def chunk_text(text, chunk_size=800, overlap=150):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def ingest_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)
    embeddings = embedder.encode(chunks).tolist()

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"{filepath}_{i}" for i in range(len(chunks))]
    )
    print(f"✅ Ingested {len(chunks)} chunks from {filepath}")

for fname in os.listdir("./docs"):
    if fname.endswith(".txt"):
        ingest_file(f"./docs/{fname}")
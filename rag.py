import chromadb
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

embedder = SentenceTransformer("all-MiniLM-L6-v2")
chroma = chromadb.PersistentClient(path="./chroma_db")
collection = chroma.get_or_create_collection("razorpay_docs")
model = genai.GenerativeModel("gemini-2.5-flash-lite")  # free & fast

def retrieve(query, top_k=5):
    query_embedding = embedder.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )
    return results["documents"][0]

def generate_answer(query, chunks):
    context = "\n\n---\n\n".join(chunks)
    prompt = f"""You are a helpful assistant for Razorpay.
Answer ONLY using the context below.
If answer not in context, say "I don't have that info."

Context:
{context}

Question: {query}
Answer:"""

    response = model.generate_content(prompt)
    return response.text

def ask(query):
    chunks = retrieve(query)
    return generate_answer(query, chunks), chunks
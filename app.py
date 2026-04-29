import streamlit as st
from rag import ask

st.set_page_config(page_title="PayBot", page_icon="💳")
st.title("💳 PayBot — Razorpay Docs Assistant")
st.caption("Ask anything about Razorpay APIs")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if query := st.chat_input("e.g. How do I create a payment link?"):
    st.session_state.messages.append({"role": "user", "content": query})
    
    with st.chat_message("user"):
        st.write(query)
    
    with st.chat_message("assistant"):
        with st.spinner("Searching docs..."):
            answer, chunks = ask(query)
        st.write(answer)
        
        with st.expander("📄 Source chunks used"):
            for i, chunk in enumerate(chunks):
                st.text(f"Chunk {i+1}:\n{chunk[:300]}...")
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
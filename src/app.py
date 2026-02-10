import streamlit as st
from backend.model import generate_response

st.set_page_config(
    page_title="Org Suppport Chatbot",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Org Support Chatbot")
st.caption("A chatbot designed to assist with organizational support inquiries.")

#initialize chat history

if "messages"  not in st.session_state:
    st.session_state.messages = []

#Display previous messages

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#User input

user_input = st.chat_input("Ask a support question...")

if user_input:
    #store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
You are a helpful organization support chatbot.
Answer clearly and professionally.

User question:
{user_input}

Answer:
"""

    bot_response = generate_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(bot_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )
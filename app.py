import streamlit as st

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

    bot_response = "This is a placeholder response. Replace with actual chatbot logic."

    with st.chat_message("assistant"):
        st.markdown(bot_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )
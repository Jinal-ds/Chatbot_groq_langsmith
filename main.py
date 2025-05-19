import streamlit as st
from chatbot import stream_chat_response  # Import your chatbot streaming function

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 Chatbot using Groq + LangSmith")

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.chat_history.append(("User", user_input))

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Stream assistant response
    response_text = ""
    with st.chat_message("assistant"):
        response_placeholder = st.empty()

        for chunk in stream_chat_response(user_input):
            response_text += chunk
            response_placeholder.markdown(response_text)

    st.session_state.chat_history.append(("Assistant", response_text))




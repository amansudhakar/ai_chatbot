import streamlit as st
import requests

st.title("AI Chatbot")

if "messages" not in st.session_state: st.session_state.messages = []
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]): st.markdown(msg["content"])

if prompt := st.chat_input("What is on your mind?"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    
    try:
        
        response = requests.post("http://localhost:8000/chat", json={"message": st.session_state.messages })
        if response.status_code == 200:

            bot_response = response.json().get("response", "No response key found.")

        else:

            bot_response = f"Backend Error: Received status {response.status_code}"
            
    except Exception as e:
        # This catches connection errors (like if the backend isn't running)
        bot_response = f"Connection Error: {e}"
    
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.rerun()

# frontend/app.py
import streamlit as st
import requests

st.title("AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# frontend/app.py

# ... (previous code) ...

if prompt := st.chat_input("What is on your mind?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    try:
        # 1. Send request to FastAPI
        response = requests.post("http://localhost:8000/chat", json={"message": prompt})
        
        # 2. Check if the server actually returned a "Success" status (200)
        if response.status_code == 200:
            bot_response = response.json().get("response", "No response key found.")
        else:
            # This helps you see the error in the UI if the backend fails
            bot_response = f"Backend Error: Received status {response.status_code}"
            
    except Exception as e:
        # This catches connection errors (like if the backend isn't running)
        bot_response = f"Connection Error: {e}"
    
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.rerun()

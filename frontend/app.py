import streamlit as st
import requests

st.title("AI Chatbot")
st.set_page_config(layout="wide")

if "chats" not in st.session_state: st.session_state.chats = {"New Chat": []}
if "current_chat_id" not in st.session_state: st.session_state.current_chat_id = "New Chat"

with st.sidebar : 

    st.title("My Conversations")
    
    if st.button("Create New Chat"):

        new_id = f'New Chat {len(st.session_state.chats) + 1}'
        st.session_state.chats[new_id] = []
        st.session_state.current_chat_id = new_id
        st.rerun()

    st.divider()
    chat_options = list(st.session_state.chats.keys())
    st.session_state.current_chat_id = st.radio("Current Chats", chat_options)

    if st.button("Delete Current Chat"):

        if st.session_state.current_chat_id in st.session_state.chats:
            
            del st.session_state.chats[st.session_state.current_chat_id]
            st.session_state.current_chat_id = list(st.session_state.chats.keys())[0] if st.session_state.chats else "New Chat"
            st.rerun()

st.title(f"{st.session_state.current_chat_id}")
current_msg = st.session_state.chats[st.session_state.current_chat_id]

for msg in current_msg:

    with st.chat_message(msg["role"]): st.markdown(msg["content"])

if prompt := st.chat_input("What is on your mind?"):

    st.session_state.chats[st.session_state.current_chat_id].append({"role": "user", "content": prompt})
    
    try:
        
        response = requests.post("http://localhost:8000/chat", json={"message": st.session_state.chats[st.session_state.current_chat_id]})
        if response.status_code == 200:

            bot_response = response.json().get("response", "No response key found.")

        else:

            bot_response = f"Backend Error: Received status {response.status_code}"
            
    except Exception as e:
        # This catches connection errors (like if the backend isn't running)
        bot_response = f"Connection Error: {e}"
    
    st.session_state.chats[st.session_state.current_chat_id].append({"role": "assistant", "content": bot_response})
    st.rerun()

# ai_chatbot
AI Chatbot made using GROQ api

ai-chatbot/
├── backend/
│   ├── main.py            # FastAPI code
├── frontend/
│   └── app.py             # Streamlit code
└── README.md              # This file

Setup : 

1. Clone the Repository 

-Bash

git clone https://github.com/amansudhakar/ai_chatbot.git
cd ai_chatbot

2. Install the mandatory Requirements

-Bash

pip install "fastapi[standard]" streamlit groq python-dotenv requests

3. Configure your environmental variables

-Bash

set GROQ_API_KEY = [your_actual_api_key_here]

Running the Application : 

1. Terminal 1 (Backend)

-Bash

cd backend
uvicorn main:app --reload

2. Terminal 2 (Frontend)

-Bash

cd frontend
streamlit run app.py
#streamlit automatically opens in your default browser

import os
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq  #
from dotenv import load_dotenv

load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Create a completion using Llama 3
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": request.message}
            ],
            model="llama-3.3-70b-versatile", # High-performance model
        )
        
        # Return the response text
        return {"response": chat_completion.choices[0].message.content}
    except Exception as e:
        return {"response": f"Groq API Error: {str(e)}"}

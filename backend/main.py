import os
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq  
from dotenv import load_dotenv

load_dotenv()

#Initializing the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

app = FastAPI()

class ChatRequest(BaseModel):   #restricts the request frm the frontend to be a string only
    message: list

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    
    try:

        chat_history = request.message  #recieving chat history from the frontend
        interaction = await asyncio.to_thread ( 

            client.chat.completions.create,
            messages = chat_history,
            model="llama-3.3-70b-versatile", # Groq's High-performance model
        )
        
        return {"response": interaction.choices[0].message.content}
        
    except Exception as e:
        
        return {"response": f"Groq API Error: {str(e)}"}

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

class ChatRequest(BaseModel):
    message: str

chat_history = list()     #keeps a local history of the chat btw the bot

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    
    try:

        chat_history.append({"role" : "user", "content" : request.message})
        chat_completion = await asyncio.to_thread ( 
            
            client.chat.completions.create,
            messages = chat_history,
            model="llama-3.3-70b-versatile", # Groq's High-performance model
        )
        
        ai_rep = chat_completion.choices[0].message.content
        chat_history.append({"role" : "assistant", "content" : ai_rep})
        
        return {"response": ai_rep}
        
    except Exception as e:
        
        return {"response": f"Groq API Error: {str(e)}"}

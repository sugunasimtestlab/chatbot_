import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from chatbot import chat_with_phi2

# FastAPI instance
app = FastAPI()

# Request model
class ChatRequest(BaseModel):
    message: str

# API Endpoint for Chatbot
@app.post("/chat")
async def chat(request: ChatRequest):
    return {"response": chat_with_phi2(request.message)}

# Serve HTML Frontend
@app.get("/")
def serve_frontend():
    return FileResponse("index.html")

# Run FastAPI App
if __name__ == "__main__":
    uvicorn.run("deploy:app", host="127.0.0.1", port=8080, reload=True)

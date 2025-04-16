from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import roll


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


class QueryRequest(BaseModel):
    Query: str


@app.post("/api/chat")
def chatwithBot(request: QueryRequest):
    return {"answer": roll.Answer(request.Query)}

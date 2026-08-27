from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.rag import RAGPipeline

app = FastAPI(
    title="Cost Efficient RAG API",
    version="1.0.0"
)

rag = RAGPipeline()


class QueryRequest(BaseModel):
    question: str
    k: int = 3


@app.get("/")
def home():
    return {
        "message": "RAG API is running!"
    }


@app.post("/ask")
def ask(request: QueryRequest):
    try:
        response = rag.ask(
            question=request.question,
            k=request.k
        )
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
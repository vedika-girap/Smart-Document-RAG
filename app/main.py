from fastapi import FastAPI, UploadFile, File
import shutil
from pathlib import Path
from pydantic import BaseModel

from app.rag.container import (
    ingestion_service,
    rag_service,
)


app = FastAPI(
    title="Smart Document RAG"
)


UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

@app.get("/")
def root():
    return {
        "message": "Smart Document RAG API"
    }


@app.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer,
        )

    chunks = ingestion_service.ingest_pdf(
        Path(file_path)
    )

    return {
        "filename": file.filename,
        "chunks_created": chunks,
        "status": "indexed",
    }

class ChatRequest(BaseModel):
    query: str
    top_k: int = 5

@app.post("/chat")
def chat(request: ChatRequest):

    results = rag_service.retriever.retrieve(request.query,request.top_k)

    answer = rag_service.generator.generate(request.query, results)

    sources = [
        {
            "filename": document.metadata.get("filename"),
            "chunk_id": document.metadata.get("chunk_id"),
            "score": score,
        }
        for document, score in results
    ]

    return {
        "answer":answer, "sources": sources,
    }
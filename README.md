# Smart Document RAG

A document question-answering API that retrieves relevant passages from uploaded PDFs and uses a Groq-hosted language model to generate answers grounded in those passages.

## How it works

1. Upload a PDF through the FastAPI endpoint.
2. Extract its text and split it into overlapping chunks.
3. Embed the chunks with `all-MiniLM-L6-v2` and store them in a local FAISS index.
4. Submit a question; the API retrieves relevant chunks and asks the configured Groq model to answer using that context.
5. Receive the answer with source filenames, chunk IDs, and retrieval scores.

The FAISS index and chunk metadata are stored locally under `data/index/`.

## Features

- PDF upload and text extraction
- Semantic search using normalized sentence-transformer embeddings and FAISS
- Context-grounded question answering through the Groq API
- Local persistence for the vector index and document metadata
- FastAPI endpoints with interactive OpenAPI documentation

## Tech stack

Python 3.12+, FastAPI, Sentence Transformers, FAISS, LangChain text splitters, Groq, and Uvicorn.

## Getting started

### Prerequisites

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/)
- A Groq API key

### Install

```bash
git clone https://github.com/vedika-girap/Smart-Document-RAG.git
cd Smart-Document-RAG
uv sync --group dev
```

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Keep your API key private; `.env` is excluded from Git.

### Run the API

```bash
uv run uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

## API

### Upload a PDF

```bash
curl -X POST "http://127.0.0.1:8000/documents/upload" \
  -F "file=@document.pdf"
```

### Ask a question

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d "{\"query\":\"What is this document about?\",\"top_k\":5}"
```

The chat response contains an `answer` and a `sources` list with each source's filename, chunk ID, and retrieval score.

## Tests

```bash
uv run pytest -q
```

## Project structure

```text
app/
  embeddings/      Text embedding
  loaders/         Document loaders
  llm/             Groq answer generation
  preprocessing/   Text chunking
  rag/             Ingestion and RAG services
  retrieval/       FAISS-backed retrieval
  main.py          FastAPI application
tests/             Unit tests
data/              Uploaded PDFs and local index data
```

## Current scope

The upload endpoint currently ingests PDFs. Although loaders for other formats are present in the codebase, they are not yet wired into the upload flow. The application is a local starter project: it does not currently provide authentication, document-management endpoints, or page-level citations. Retrieval scores are ranking signals, not confidence probabilities.

INDEX_PATH = "data/index/index.faiss"
DOCUMENTS_PATH = "data/index/documents.json"

from pathlib import Path

from app.embeddings.embedder import Embedder
from app.vector_store.faiss_store import FaissStore

from app.retrieval.retriever import Retriever
from app.llm.generator import Generator
from app.rag.rag_service import RAGService
from app.rag.ingestion import IngestionService

index_path = Path(INDEX_PATH)
documents_path = Path(DOCUMENTS_PATH)

embedder = Embedder()

vector_store = FaissStore(
    dimension = 384
)
if index_path.exists() and documents_path.exists():
    vector_store.load(INDEX_PATH)
    vector_store.load_documents(DOCUMENTS_PATH)

retriever = Retriever(embedder=embedder, vector_store=vector_store)
generator = Generator()
rag_service = RAGService(
    retriever,
    generator
)

ingestion_service = IngestionService(
    embedder = embedder,
    vector_store = vector_store
)

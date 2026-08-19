from app.embeddings.embedder import Embedder
from app.vector_store.faiss_store import FaissStore
from app.retrieval.retriever import Retriever
from app.llm.generator import Generator
from app.rag.rag_service import RAGService
from app.rag.ingestion import IngestionService

embedder = Embedder()

vector_store = FaissStore(
    dimension = 384
)

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
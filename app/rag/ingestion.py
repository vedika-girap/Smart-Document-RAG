import numpy as np
from pathlib import Path


from app.loaders.pdf_loader import PDFLoader
from app.preprocessing.lc_chunker import LangChainChunker
from app.embeddings.embedder import Embedder
from app.vector_store.faiss_store import FaissStore

INDEX_DIR = Path("data/index")
INDEX_DIR.mkdir(
    parents=True,
    exist_ok=True,
)
INDEX_PATH = Path(
    "data/index/index.faiss"
)

DOCUMENTS_PATH = Path(
    "data/index/documents.json"
)

class IngestionService():
    def __init__(self, embedder:Embedder, vector_store: FaissStore):
        self.embedder = embedder
        self.vector_store = vector_store
        self.chunker = LangChainChunker()

    def ingest_pdf(self, file_path: Path):
        loader = PDFLoader()
        document = loader.load(file_path)
        chunks = self.chunker.split(document)
        texts = [
            chunk.content
            for chunk in chunks
        ]
        vectors = self.embedder.embed_documents(texts)
        vectors = np.asarray(vectors, dtype="float32")
        self.vector_store.add(vectors, chunks)

        self.vector_store.save(
            str(INDEX_PATH)
        )

        self.vector_store.save_documents(
            str(DOCUMENTS_PATH)
        )
        return len(chunks)
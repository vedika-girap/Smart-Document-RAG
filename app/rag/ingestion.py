import numpy as np

from app.loaders.pdf_loader import PDFLoader
from app.preprocessing.lc_chunker import LangChainChunker
from app.embeddings.embedder import Embedder
from app.vector_store.faiss_store import FaissStore


class IngestionService():
    def __init__(self, embedder:Embedder, vector_store: FaissStore):
        self
        self.embedder = embedder
        self.vector_store = vector_store
        self.chunker = LangChainChunker()

    def ingest_pdf(self, file_path: str):
        loader = PDFLoader(file_path)
        document = loader.load()
        chunks = self.chunker.split(document)
        texts = [
            chunk.content
            for chunk in chunks
        ]
        vectors = self.embedder.embed_documents(texts)
        vectors = np.asarray(vectors, dtype="float32")
        self.vector_store.add(vectors, chunks)

        return len(chunks)
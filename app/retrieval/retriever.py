from app.embeddings.embedder import Embedder
from app.models.document import Document
from app.vector_store.faiss_store import FaissStore

class Retriever:

    def __init__(self, embedder:Embedder, vector_store:FaissStore):
        self.embedder= embedder
        self.vector_store = vector_store

    def retrieve(self, query: str, k: int = 5)-> list[tuple[Document, float]]:
        query_vector = self.embedder.embed(query)

        results = self.vector_store.search(
            query_vector.reshape(1,-1),
            k=k,
        )        
        return results
    
from app.llm.generator import Generator
from app.retrieval.retriever import Retriever

class RAGService:

    def __init__(self, retriever:Retriever, generator:Generator):
        self.retriever = retriever
        self.generator = generator

    def answer(self, query: str, k: int = 5,)->str:
        documents = self.retriever.retrieve(query, k=k)
        return self.generator.generate(query, documents)


        
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.models.document import Document

load_dotenv()

class Generator:
    def __init__(self, model: str= "gpt-4.1-mini"):
        self.client = OpenAI(
            api_key= os.getenv("OPEN_API_KEY")
        )        
        self.model = model

    def generate(
        self,
        query: str,
        documents: list[tuple[Document, float]],
    )->str:
        context = "\n\n".join(
            f"""
        Source: {document.metadata.get("filename")}
        Chunk: {document.metadata.get("chunk_id")} 
   
        {document.content} 
        """
            for document, score in documents
        )
        prompt =f"""
You are a helpful question-answering assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context,
say that you don't have enough information.

Context:
{context}

Question:
{query}
"""

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text
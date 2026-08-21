import os

from dotenv import load_dotenv
from groq import Groq

from app.models.document import Document

load_dotenv()

class Generator:
    def __init__(self, model: str= "openai/gpt-oss-20b"):
        self.client = Groq(
            api_key= os.getenv("GROQ_API_KEY")
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

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature= 0,
        )

        return response.choices[0].message.content
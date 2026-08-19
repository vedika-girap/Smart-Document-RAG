from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.models.document import Document

class LangChainChunker:

    def __init__(
            self,
            chunk_size: int = 500,
            overlap: int = 100
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = overlap,
        )

    def split(
            self,
            document: Document,
    ) -> list[Document]:
        texts = self.splitter.split_text(
            document.content
        )

        chunks = []

        for i, text in enumerate(texts):
            metadata = document.metadata.copy()
            metadata["chunk_id"] = i

            chunks.append(
                Document(
                    content= text,
                    metadata= metadata,
                )
            )
        return chunks
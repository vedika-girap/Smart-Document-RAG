from app.models.document import Document

class TextChunker:
    """
    Splits a document into fixed-size chunks.
    """

    def __init__(self, chunk_size: int = 500, overlap: int = 100):
        if overlap >= chunk_size:
            raise ValueError(
                "overlap must be smaller than chunk_size"
            )
        self.chunk_size = chunk_size
        self.overlap = overlap



    def split(self, document: Document) -> list[Document]:
        chunks = []
        text = document.content
        step = self.chunk_size - self.overlap
        for i in range(0, len(text), step):
            # finds space from end of the chunk
            index = chunk.rfind(" ")
            chunk = text[i : index]
            metadata = document.metadata.copy()
            metadata["chunk_id"] = len(chunks)

            new_document = Document(
            content=chunk,
            metadata=metadata,
            )

            chunks.append(new_document)

        return chunks
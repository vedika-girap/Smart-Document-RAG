from pathlib import Path

from pypdf import PdfReader

from app.loaders.base_loader import BaseLoader
from app.models.document import Document

class PDFLoader(BaseLoader):
    """
    Loader for PDF documents.
    """

    def load(self, file_path: Path) ->Document:
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

        return Document(
            content = text,
            metadata= {
                "filename": file_path.name,
                "filetype": "pdf",
            }, 
        )
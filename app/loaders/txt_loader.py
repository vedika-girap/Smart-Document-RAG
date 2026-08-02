from pathlib import Path

from app.loaders.base_loader import BaseLoader
from app.models.document import Document

class TXTLoader(BaseLoader):
    """
    Loader for plain text files.
    """

    def load(self, file_path: Path) -> Document:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        return Document(
            content= text,
            metadata={
                "filename":file_path.name,
                "filetype": "txt"
            },
        )
from abc import  ABC, abstractmethod
from pathlib import Path

from app.models.document import Document

class BaseLoader(ABC):
    """Abstract base class for all document loaders."""

    @abstractmethod
    def load(self, file_path: Path) -> Document:
        """
        Read a file and return a Document object.
        """

        pass
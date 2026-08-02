from dataclasses import dataclass, field
from typing import Any

@dataclass
class Document:
    """
    Represents a document used throughout the RAG pipeline.
    """

    content:str
    metadata: dict[str, Any] = field(default_factory=dict)
    
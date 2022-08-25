"""Abstract interface for the ingestor."""

from typing import List
from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract interface for the ingestor."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Can ingest abstract method."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse abstract method."""
        pass

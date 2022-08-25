from typing import List

from .IngestorInterface import IngestorInterface
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    ingestors = [DOCXIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.ingestors:
            if importer.can_ingest(path):
                return importer.parse(path)

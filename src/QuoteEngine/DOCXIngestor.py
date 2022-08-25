"""ingest docx file with quotes."""

from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    """ingest docs file with quotes."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse docx file."""
        if not cls.can_ingest(path):
            raise Exception(f'file {path} is not supported in this module')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                new_quote = QuoteModel(
                    parse[0].removeprefix('"').removesuffix('"'), parse[1])
                quotes.append(new_quote)
        return quotes

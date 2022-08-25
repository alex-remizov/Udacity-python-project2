"""ingest txt file with quotes."""

from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """ingest txt file with quotes."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt file."""
        if not cls.can_ingest(path):
            raise Exception(f'file {path} is not supported in this module')

        with open(path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        content = content.split('\n')

        quotes = [QuoteModel(
            x.split(' - ')[0], x.split(' - ')[1]) for x in content]

        return quotes

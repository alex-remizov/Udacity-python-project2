"""ingest pdf file with quotes."""

from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """ingest pdf file with quotes."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse pdf file."""
        if not cls.can_ingest(path):
            raise Exception(f'file {path} is not supported in this module')

        tmp_path = f'./{random.randint(0, 10000000)}.txt'
        subprocess.call(['pdftotext', path, tmp_path])

        with open(tmp_path, 'r') as f:
            content = f.read()
        content = content.split('\n')
        content = content[0]
        content = content.split(' "')
        quotes = []
        for x in content:
            quotes.append(QuoteModel(
                x.split(' - ')[0].replace('"', '').replace("'", ""),
                x.split(' - ')[1].replace('"', '').replace("'", "")))

        os.remove(tmp_path)

        return quotes

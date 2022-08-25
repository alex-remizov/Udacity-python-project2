from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp_path = f'./{random.randint(0, 10000000)}.txt'
        subprocess.call(['pdftotext', path, tmp_path])

        with open(tmp_path, 'r') as f:
            content = f.read()
        content = content.split('\n')
        content = content[0]
        content = content.split(' "')
        quotes = [QuoteModel(x.split(' - ')[0].replace('"','').replace("'",""), x.split(' - ')[1].replace('"','').replace("'","")) for x in content]

        os.remove(tmp_path)

        return quotes

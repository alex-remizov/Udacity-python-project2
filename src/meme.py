"""CLI tool for a meme generator."""

import os
import random
import argparse

from src.QuoteEngine.Ingestor import Ingestor
from src.QuoteEngine.QuoteModel import QuoteModel
from src.MemeGenerator.MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "src/_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['src/_data/DogQuotes/DogQuotesTXT.txt',
                       'src/_data/DogQuotes/DogQuotesDOCX.docx',
                       'src/_data/DogQuotes/DogQuotesPDF.pdf',
                       'src/_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('src/tmp/meme.jpg')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image

    parser = argparse.ArgumentParser(description='CLI to generate a mem')
    parser.add_argument('--path',
                        type=str, default=None, help='path for the image')
    parser.add_argument('--body',
                        type=str, default=None, help='body of the text')
    parser.add_argument('--author',
                        type=str, default=None, help='author of the text')

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))

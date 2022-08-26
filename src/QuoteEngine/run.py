from .Ingestor import Ingestor
path = "./_data/DogQuotes/DogQuotesPDF.pdf"
# path = "./_data/DogQuotes/DogQuotesTXT.txt"
# path = "./_data/DogQuotes/DogQuotesCSV.csv"
# path = "./_data/DogQuotes/DogQuotesDOCX.docx"
x = Ingestor.parse(path)
print(x)
print(type(x[0]))
print(x[0].__dict__)

#TODO: remove this file



# python -m src.QuoteEngine.run
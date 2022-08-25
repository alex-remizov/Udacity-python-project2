from src.QuoteEngine.Ingestor import Ingestor
path = "src/_data/DogQuotes/DogQuotesPDF.pdf"
# path = "src/_data/DogQuotes/DogQuotesTXT.txt"
# path = "src/_data/DogQuotes/DogQuotesCSV.csv"
# path = "src/_data/DogQuotes/DogQuotesDOCX.docx"
x = Ingestor.parse(path)
print(x)
print(type(x[0]))
print(x[0].__dict__)

#TODO: remove this file



# python -m src.QuoteEngine.run
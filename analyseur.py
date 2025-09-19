from PyPDF2 import PdfReader
from interface import entry

docPath = entry.get()

reader = PdfReader(docPath)
page = reader.pages[0]
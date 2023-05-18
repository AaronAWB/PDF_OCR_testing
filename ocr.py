import platform
from PyPDF2 import PdfReader
from tempfile import TemporaryDirectory
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

file = open('pleasant_bay.pdf','rb')
reader = PdfReader(file)

print(len(reader.pages))

def get_metadata(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        info = reader.metadata
    return info
       
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        results = []
        for i in range(0, len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            results.append(text)
    return ' '.join(results) # Convert list to a single string

def image_to_text(image_file):
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text

print(image_to_text('pleasant_bay.pdf'))

if __name__ == "__main__":
    main()
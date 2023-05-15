from PyPDF2 import PdfReader

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

print(extract_text_from_pdf('pleasant_bay.pdf')) 
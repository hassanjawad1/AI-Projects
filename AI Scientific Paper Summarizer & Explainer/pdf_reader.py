# PyMuPDF
import fitz  

#fuction to extract data from pdf as text 
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

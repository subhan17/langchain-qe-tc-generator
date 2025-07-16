import fitz

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for pages in doc:
            text +=pages.get_text()

    return text
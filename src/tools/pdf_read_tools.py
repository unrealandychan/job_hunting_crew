from PyPDF2 import PdfReader
from langchain_core.tools import tool


# This tool reads the content of a PDF file
@tool
def get_pdf_content(path) -> str:
    """
    This tool reads the content of a PDF file
    :param path:
    :return: content
    """
    with open(path, "rb") as file:
        pdf = PdfReader(file)
        content = ""
        for page in range(len(pdf.pages)):
            content += pdf.pages[page].extract_text()
    return content

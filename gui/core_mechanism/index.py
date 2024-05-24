from typing import List
from PyPDF2 import PdfReader 
import logging

import regex as re 
def pdf_data_handler(words: List[str],pdf_path: str = None):
    """Converts a PDF file to text and searches for specific keywords.

    Args:
        words (List[str]): (placeholder for future keyword search functionality)
        pdf_path (str, optional): The path to the PDF file to be processed. Defaults to the user's current working directory if not specified.

    Returns:
        str: The Result of the search algorithm implemented in searchLessonCode function

    Raises:
        FileNotFoundError: If the specified PDF file cannot be located.
    """
    logging.basicConfig(filename='runtime_error.log', level=logging.ERROR)  #  # Retrieve logger
    error_logger = logging.getLogger('error_logger')

    try:
        pdf = PdfReader(pdf_path)
        pages = [page for page in pdf.pages]
        page_number = [pdf.get_page_number(pages[i]) for i in range(len(pages))]
        if(len(page_number)==1):
            txt=pages[0].extract_text()
        else: 
            txt = []
            for i in range(page_number):
                txt.append(pages[i].extract_text())
        processed_pdf = txt 
        return searchLessonCode(words,processed_pdf)
    except FileNotFoundError as fnfe:
        logging.error(f"File Not Found: {fnfe}")
        raise FileNotFoundError("Specified PDF file not found.") from fnfe  # Chain the exception
    except Exception as ex: #helpful during development process however it will be less required in daily use
        logging.exception(f"An error occurred during PDF processing: {ex}")  # Log full traceback

def searchLessonCode(lesson_codes: List[str], processed_pdf:str)->str:
    """
    Searches for the specified lesson codes within a PDF document.
    Args:
        lesson_codes (List[str]): A list of lesson codes to search for (e.g., ["muh321", "muh324", "muh325"]).
        processed_pdf (str): The extracted text content from the PDF document.
    Returns:
        str: If any of the lesson codes are found in the PDF, returns a string containing the found code(s). Otherwise, returns an empty string ("").
    Raises: 
        If the pdf variable is an empty string or it is not assigned to a valid pdf object. 
 
    """
    txt = ""
    for i in range(len(processed_pdf)):
        for j in lesson_codes:
                if(re.search(j,processed_pdf[i]) != None):
                    txt += j+'\n'
    else: 
        for i in range(len(lesson_codes)):
            txt += lesson_codes[i]+"\n" if re.search(lesson_codes[i],processed_pdf) != None else ""
    return txt

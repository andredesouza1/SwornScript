import re
import streamlit as st  
from PyPDF2 import PdfReader

from marvin import ai_fn

def extract_type_info(s):
    if s.startswith('<class'):
        # Extract the type from '<class ...>'
        match = re.search(r"<class '(.+?)'>", s)
        if match:
            return match.group(1)
    elif s.startswith('typing'):
        # Extract the type from 'typing.Optional[str]'
        match = re.search(r"typing\.Optional\[(.+?)]", s)
        if match:
            return match.group(1)
    else:
        # Default case, return the original string
        return s

def read_single_pdf(file):
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    all_page_text = ""
    for i in range(count):
        page = pdfReader.pages[i]
        all_page_text += page.extract_text()
    return all_page_text



def get_empty_fields(input_dict):
    empty_keys = []
    for key, value in input_dict.items():
        if isinstance(value, str) and value.strip() == "":
            empty_keys.append(key)
        elif isinstance(value, list) and not value:
            empty_keys.append(key)
        elif isinstance(value, bool) and not value:
            empty_keys.append(key)
        elif isinstance(value, int) and value == 0:
            empty_keys.append(key)
    return empty_keys


@ai_fn
def rewrite_document(full_text: str, info_to_add: dict) -> str:
    """
    You are an expert writer and editor. Given `full_text`, and `info_to_add`, return the rewritten document that preserves the original document and adds new information. Provide the rewritten document in a readable format.
    """
    





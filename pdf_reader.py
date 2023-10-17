from PyPDF2 import PdfReader
#import streamlit as st
class read_pdf:
    def __init__(self):
        super(read_pdf, self).__init__()
  #  @st.cache_data   
    def read(self, file)-> list:
        reader = PdfReader(file)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return text
        



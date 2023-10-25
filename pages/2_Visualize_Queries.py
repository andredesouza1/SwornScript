import streamlit as st
from pydantic import BaseModel, Field, create_model
import query_builder
from typing import Optional, Tuple
import handle_state
import utils
from PyPDF2 import PdfReader
import pandas as pd

st.session_state.update(st.session_state)
handle_state.set_initial_states()




st.title("View Queries Types")


for i in range(len(st.session_state.query_instances)):
    Title = st.session_state.query_instances[i].__dict__['__pydantic_core_schema__']['schema']['model_name']
    st.write(f'<span style="font-size: 24px;">Query Name: {Title}</span>', unsafe_allow_html=True)
    
    
    for key in st.session_state.query_instances[i].__dict__['model_fields'].keys():
       
        annotation = st.session_state.query_instances[i].__dict__["model_fields"][key].annotation
        
        if str(annotation).startswith("<class"):
            st.write(f'<span style="font-size: 16px;">Field: {key}</span>',
                    f'      |      ' 
                    f'<span style="font-size: 16px;">Data Type: {utils.extract_type_info(str(annotation))}</span>',
                    f'      |      '  
                    f'<span style="font-size: 16px;">Required: Yes</span>',
                    unsafe_allow_html=True)
        elif str(annotation).startswith("typing.Optional"):
            st.write(f'<span style="font-size: 16px;">Field: {key}</span>',
                    f'      |      '  
                    f'<span style="font-size: 16px;">Data Type: {utils.extract_type_info(str(annotation))}</span>',
                    f'      |      '  
                    f'<span style="font-size: 16px;">Required: No</span>',
                    unsafe_allow_html=True)
        
        

        st.write(f'<span style="font-size: 16px;">Description: {st.session_state.query_instances[i].__dict__["model_fields"][key].description}</span>', unsafe_allow_html=True)    
        
       
class_names = [instance.__name__ for instance in st.session_state.query_instances]

# Create a select box with the class names
selected_class_name = st.sidebar.selectbox("Select the query you want to run", class_names)      

uploaded_file = st.sidebar.file_uploader("Upload a document to run the query on",accept_multiple_files=False,type=['pdf'])



if st.sidebar.button("Run Query"):
    st.session_state.output = None
    st.session_state.df = None
    # Find the selected class in the list
    selected_class = None
    for class_instance in st.session_state.query_instances:
        if class_instance.__name__ == selected_class_name:
            selected_class = class_instance
            break

    if selected_class:
        print(selected_class)
        st.session_state.selected_class = selected_class    
    else:
        print(f"Class '{selected_class_name}' not found in the list")
    

    raw_text = utils.read_single_pdf(uploaded_file)
    
    
    
    st.session_state.output = selected_class(raw_text)

    st.session_state.df = pd.DataFrame.from_dict(st.session_state.output.__dict__, orient='index')

# print(st.session_state.query_instances[0].__dict__)



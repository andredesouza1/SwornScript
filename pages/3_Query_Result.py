import streamlit as st 
import handle_state
import utils
import pandas as pd
import query_builder

st.session_state.update(st.session_state)
handle_state.set_initial_states()


st.title('Query Results')


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

if st.session_state.df is not None:
    # Create a Streamlit app
    st.table(st.session_state.df)

    question_type = st.selectbox("Select the type of question you want to ask", ["Yes or No", "Sentiment"])
    query_question = st.text_input("Enter a question about query you just ran, you can ask a yes or no question or a question that address sentiment(positive,neutral,negative)")
    
    if st.button("Ask the AI"):
        if question_type == "Yes or No":
            response = query_builder.YesorNo(f"Based on the context provided answer a question. Context: {str(st.session_state.output.__dict__)} Question {query_question}")
            with st.chat_message("assistant"):
                st.write(f'<span style="font-size: 24px;">{response.name}</span>', unsafe_allow_html=True)
           
        elif question_type == "Sentiment":
            response = query_builder.Sentiment(f"Based on the context provided provide the sentment related to the content of the question. Context: {str(st.session_state.output.__dict__)} Question {query_question}")
            with st.chat_message("assistant"):
                st.write(f'<span style="font-size: 24px;">{response.name}</span>', unsafe_allow_html=True)
            
    
    
        


    



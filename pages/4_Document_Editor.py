from pydantic import BaseModel
import streamlit as st
import handle_state
from pydantic import BaseModel, Field, create_model
import utils
from marvin import ChatCompletion

st.session_state.update(st.session_state)
handle_state.set_initial_states()

st.title("Document Editor")
st.write("Identify the information you may want to add to your document and the AI will rewrite the document for you")

output_dict = st.session_state.output.__dict__


empty_list =utils.get_empty_fields(output_dict)


empty_list_description = []
for item in empty_list:
    empty_list_description.append(st.session_state.selected_class.__dict__["model_fields"][str(item)].description)

info_to_add = {}
if st.session_state.selected_class:
    for i in range(len(empty_list)):
        if st.checkbox(f"The following information could improve your document would you like to provide this information? {empty_list}: {empty_list_description[i]}", key=f"checkbox{i}",value=False):    
            st.text_input(f"Enter the information you want to add", key=f"input{i}",)
            info_to_add[empty_list[i]] = st.session_state[f"input{i}"]
   

if st.button("Rewrite document"):
    rewritten_document = utils.rewrite_document(st.session_state.output.__dict__['full_text'],info_to_add)
    messages = [{'role': 'user', 'content': f"Return this in a more redable format: {rewritten_document}"}]
    openai = ChatCompletion('gpt-3.5-turbo').create(messages = messages)
    st.chat_message("assistant").write(openai.response.choices[0].message.content)


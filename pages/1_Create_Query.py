import streamlit as st
from pydantic import create_model
import query_builder    

import handle_state


st.session_state.update(st.session_state)
handle_state.set_initial_states()

st.title("Query Builder")

if st.button("Create New Query"):
    temp = st.session_state.query_instances
    st.session_state.clear()
    handle_state.set_initial_states()
    st.session_state.query_instances = temp

query_name = st.text_input("Enter the name of the query type you want to create")
  
st.write("_________________________________________________________________________________________")

param_list = []
model_to_create = None

if st.button("Add a new field"):
    st.session_state.counter +=1

if st.button("Remove a field") and st.session_state.counter >= 1:
    st.session_state.counter -=1

st.write(st.session_state.counter)

for i in range(st.session_state.counter):
    st.text_input(f"Enter the name for the information you want to extract ", key=f"name{i}",)
    st.selectbox("Select the data type", ["str", "int", "float", "bool", "list"], key=f"type{i}", )
    st.text_input(f"Enter a description for the information you want to extract", key=f"description{i}",)
    st.checkbox("Required", key=f"required{i}",value=False)



if st.button("Submit"):
    has_empty_fields = False

    for i in range(st.session_state.counter):
        if st.session_state[f"name{i}"] == "":
            st.error("You must enter a name for each field")
            has_empty_fields = True
            break
        elif st.session_state[f"description{i}"] == "":
            st.error("You must enter a description for each field")
            has_empty_fields = True
            break

    if has_empty_fields:
        # Exit the processing if there are empty fields
        st.error("Please fill in all the required fields.")
    else:
        # Process the submitted data
        for i in range(st.session_state.counter):
            submitted_data = {
                "query_name": st.session_state[f"name{i}"],
                "data_type": st.session_state[f"type{i}"],
                "required": st.session_state[f"required{i}"],
                "description": st.session_state[f"description{i}"],
            }
            st.session_state.display_list.append(submitted_data)
            st.session_state.param_list.append(query_builder.create_param_tuple(st.session_state[f"name{i}"], st.session_state[f"type{i}"], st.session_state[f"description{i}"], st.session_state[f"required{i}"]))
            
if st.sidebar.button("Save Query Type"):
    has_empty_fields = False
    if query_name == "":
        has_empty_fields = True
    
    if has_empty_fields:
        # Exit the processing if there are empty fields
        st.error("Query must have a name.")
    else:
        if st.session_state.param_list != []:
            param_dict = dict(st.session_state.param_list)
            print(param_dict)
            # Dynamically create the BarModel class
            model_to_create = create_model(query_name, **param_dict, __base__=query_builder.CustomQueryBase)
            st.session_state.query_instances.append(model_to_create) 
    

st.sidebar.table(st.session_state.display_list) 


    

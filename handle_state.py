import streamlit as st  




def set_initial_states():

    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    else:
        st.session_state.counter = st.session_state.counter

    if 'param_list' not in st.session_state:
        st.session_state.param_list = []
    else:
        st.session_state.param_list = st.session_state.param_list
    
    if 'display_list' not in st.session_state:
        st.session_state.display_list = []
    else:
        st.session_state.display_list = st.session_state.display_list  

    if 'query_instances' not in st.session_state:
        st.session_state.query_instances = []
    else:
        st.session_state.query_instances = st.session_state.query_instances

    if 'output' not in st.session_state:
        st.session_state.output = None
    else:
        st.session_state.output = st.session_state.output

    if 'df' not in st.session_state:
        st.session_state.df = None
    else:
        st.session_state.df = st.session_state.df

    if 'selected_class' not in st.session_state:
        st.session_state.selected_class = None
    else:
        st.session_state.selected_class = st.session_state.selected_class
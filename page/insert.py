import streamlit as st
import sys
sys.path.insert(1, 'controller')

import client as client

def insert():
    st.title('Insert Person')

    with st.form(key='insert'):
        input_fullname = st.text_input(label = 'FullName')
        input_email = st.text_input(label='Email')
        input_age = st.text_input(label="Age")        
        
        button_submit = st.form_submit_button('Insert')

        if button_submit:
            client.insert(input_fullname, input_email, input_age)
            st.success('Person inserted successfully')
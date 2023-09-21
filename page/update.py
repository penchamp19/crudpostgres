import streamlit as st
import sys
sys.path.insert(1, 'controller')

import client as client

#Function Update data by id from table person
def update():
    st.title("Update")

    update_id = st.number_input(label='Id', format="%d", step=1)
    input_fullname = st.text_input(label='FullName')
    input_email = st.text_input(label='Email')
    input_age = st.text_input(label='Age')

    if st.button('Update'):
        client.update(update_id, input_fullname, input_email, input_age)
        st.success('Update Success')
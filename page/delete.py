import streamlit as st
import sys
sys.path.insert(1, 'controller')

import client as client

#Function Update data by id from table person
def delete():
    st.title("Delete")

    delete_id = st.number_input(label='Id', format="%d", step=1)

    if st.button("Delete"):
        client.delete(delete_id)
        st.success("Delete Success")
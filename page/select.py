import streamlit as st
import sys
sys.path.insert(1, 'controller')

import client as client

def select_all():
    st.title('Select All Person')

    persons = client.select_all()
    if persons:
        st.table(persons)
    else:
        st.write("No person found")
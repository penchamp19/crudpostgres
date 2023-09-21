import streamlit as st
import page.insert as insert
import page.select as select
import page.update as update
import page.delete as delete

#Crerate sidebar menu
st.sidebar.title("Menu")

page = st.sidebar.selectbox('', ['Home','Insert', 'Update', 'Delete'])

if page == 'Insert':
    insert.insert()
elif page == 'Home':
    select.select_all()
elif page == 'Update':
    update.update()
elif page == 'Delete':
    delete.delete()
import streamlit as st
from st_pages import Page, add_page_title, show_pages
from streamlit_extras.switch_page_button import switch_page
try:
    del st.session_state['logUser']
except:
    x=12
switch_page('Home')


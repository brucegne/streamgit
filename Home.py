import streamlit as st
from st_pages import Page, add_page_title, show_pages

add_page_title("Welcome to my site")

show_pages(
  [
    page("pages/contacts.py","Contacts",""),
    page("pages/photos.py","Photo Library",""),
  ]
)

pholder = st.sidebar.empty()
with pholder.container():
  uname = st.text_input("Enter User Name")
  upass = st.text_input("Enter Password")
  login = st.button("Login")
  if login:
    pholder.write("")
  
lcol, rcol = st.columns([3,1])

lcol.header("This is on the left")
rcol.header("This is on right")

import streamlit as st
from st_pages import Page, add_page_title, show_pages

add_page_title()

def bldMenu():
  show_pages(
    [
      Page("Home.py","Home",":us:"),
      Page("contacts.py","Contacts","🏡"),
      Page("DetaZips.py","ZipCode Lookup","💩"),
      Page("photos.py","Photo Library","📸"),
    ]
  )

def dispLog():
    pholder = st.sidebar.empty()
    with pholder.container():
      uname = st.text_input("Enter User Name")
      upass = st.text_input("Enter Password")
      login = st.button("Login")
      if login:
        st.session_state['logStatus'] = 'Yes'
        pholder.write("")
        bldMenu()

if 'logStatus' not in st.session_state:
    dispLog()
else:
    bldMenu()   

lcol, rcol = st.columns([1,1])

lcol.header("This is on the left")
rcol.header("This is on right")

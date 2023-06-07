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

bldMenu()

lcol, rcol = st.columns([1,2])

with lcol:
  st.subheader("Please Login")
  with st.form(lform, clear_on_submit=True):
    usrname=st.text_input(max_chars=15, key="uname")
    upasswd=st.text_input(max_chars=15, key="upass", type="password")
    logbtn=st.form_submit_button("Login", key="lBtn")


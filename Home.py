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

lcol, rcol = st.columns(1,2)

lcol.subheader("Please Login")
lcol.form(lform, clear_on_submit=True)
usrname=lcol.text_input(max_chars=15, key="uname")
upasswd=lcol.text_input(max_chars=15, key="upass", type="password")
logbtn=lcol.form_submit_button("Login", key="lBtn")


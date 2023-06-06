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

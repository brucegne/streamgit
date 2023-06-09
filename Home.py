import streamlit as st
from deta import Deta
from st_pages import Page, add_page_title, show_pages
from streamlit_extras.switch_page_button import switch_page

add_page_title()

# user_name = st.sidebar.empty()

def bldMenu():
  show_pages(
    [
      Page("Home.py","Home",":us:"),
      Page("contacts.py","Contacts","🏡"),
      Page("DetaZips.py","ZipCode Lookup","💩"),
      Page("photos.py","Photo Library","📸"),
      Page("Logout.py", "Logout", ":door:"),
    ])
  
bldMenu()

hdr = st.empty()
logit = st.container()

# Connect to Deta Base with your Data Key

lcol, rcol = st.columns([1,1])

with lcol:
  st.subheader("Please Login")
  with st.form("lform", clear_on_submit=True):
    usrname=st.text_input("User Name", max_chars=20, key="uname")
    upasswd=st.text_input("Password", max_chars=20, key="upass", type="password")
    logbtn=st.form_submit_button("Login")
    qryString = {}
    if logbtn:
        deta = Deta("b0fhjqxu_fG4y33DEMaK8qWfMGABUSbn8cGFNxXhC")
        db = deta.Base("UserBase")
        qryString["login_name"] = usrname.strip()
        recs = db.fetch(qryString).items
        logit.write(qryString)
        logit.write(recs)
        if len(recs) > 0:
            file_pass = recs[0]['passwd']
            if file_pass == upasswd:
                hdr.write("Welcome " + recs[0]["full_name"])
                st.session_state['logUser'] = usrname
                switch_page("Zipcode Lookup")
            else:
               hdr.write("Invalid password entered")
        else:
           hdr.write("Invalid user name or password")

        

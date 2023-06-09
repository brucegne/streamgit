import streamlit as st
from st_pages import Page, add_page_title, show_pages
from streamlit_extras.switch_page_button import switch_page

for key in st.session_state.keys():
    del st.session_state[key]

switch_page('Home')

from deta import Deta

deta_key = "b0fvbhznajp_skZPFvqP1e1dV6eK5BHkuDm72uM6FKf4"

deta = Deta(deta_key)

db = deta.Base("UserBase")
qryString={}
usrname = input("Enter User Name  ")
pwd = input("Enter your password  ")
qryString["login_name"] = usrname

rec = db.fetch(qryString).items
if len(rec) > 0:
    file_pass = rec[0]['passwd']
    if file_pass == pwd:
        print("Welcome "+rec[0]['full_name'], "Key Value  "+rec[0]['key'])
        kv = rec[0]['key']
        db.update(key=kv,updates={"oldpass": kv, "passwd": "Pa$$w0rd"})
    else:
        print("Sorry, invalid password")
        
        
    

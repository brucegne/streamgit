import streamlit as st
import streamlit_authenticator as stauth

pholder = st.sidebar.empty()
with pholder.container():
  uname = st.text_input("Enter User Name")
  upass = st.text_input("Enter Password")
  
lcol, rcol = st.columns([3,1])

lcol.header("This is on the left")
rcol.header("This is on right")

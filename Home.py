import streamlit as st
import streamlit_authenticator as stauth

lcol, rcol = st.columns([3,1])

lcol.header("This is on the left")
rcol.header("This is on right")

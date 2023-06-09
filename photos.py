import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
import os, json, time
from deta import Deta, Drive
from st_pages import Page, add_page_title, show_pages

add_page_title()

if 'logUser' not in st.session_state:
   switch_page('Home')
else:
    st.subheader("Current User " + st.session_state['full_name'])

deta_key = "b0fvbhznajp_skZPFvqP1e1dV6eK5BHkuDm72uM6FKf4"
zips_key = "b0fvbhznajp_xGQ4ave87rKLwaYZ5QcCkCovWFoM5thU"

st.markdown("<h1 style='text-align: center; color: grey;'>Photo Library</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: red;'>Stored on Deta Drive</h2>", unsafe_allow_html=True)

project = Deta(deta_key)
drive_name = 'PicCollection'
drive = project.Drive(drive_name)

topEnd = st.empty()

picList = drive.list()
photoList = ['Please select']
for rec in picList['names']:
    photoList.append(rec)
selPhoto = st.selectbox("Choose Photo", photoList)

if selPhoto and "select" not in selPhoto:
    img = drive.get(selPhoto)
    pic = img.read()
    topEnd.image(pic,width=150)
    img.close()

# Initialize a streamlit file uploader widget.
uploaded_file = st.file_uploader("Choose a file")

# If user attempts to upload a file.
if uploaded_file is not None:
    with st.spinner(text="Loading image"):
        bytes_data = uploaded_file.getvalue()

# Show the image filename and image.
#    st.write(f'filename: {uploaded_file.name}')
#    st.image(bytes_data)

        # Upload the image to deta using put with filename and data.
        drive.put(uploaded_file.name, data=bytes_data)


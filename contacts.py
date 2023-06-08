import streamlit as st
import pandas as pd
from deta import Deta
import time
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, add_page_title, show_pages

add_page_title()

if 'logUser' not in st.session_state:
   switch_page('Home')

# Data to be written to Deta Base

hdr = st.empty()
deta_key = "b0fvbhznajp_skZPFvqP1e1dV6eK5BHkuDm72uM6FKf4"
zips_key = "b0fvbhznajp_xGQ4ave87rKLwaYZ5QcCkCovWFoM5thU"

deta = Deta(deta_key)

db = deta.Base("bgfamily")

st.markdown("<h1 style='text-align: center; color: grey;'>Deta Contacts Database</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: red;'>It is was it is.</h2>", unsafe_allow_html=True)

with st.form("form", clear_on_submit=True):
    name = st.text_input("Your name")    
    age = st.text_input("Your age")
    notes = st.text_area("Enter the notes for this person")
    submitted = st.form_submit_button("Store in database")
    if submitted:
        db.put({"name": name, "age": age, "notes": notes})
        hdr.success(name+" Has been added to the database")
detdat = db.fetch().items
df = pd.DataFrame(detdat)
result_area = st.empty()
result_area.dataframe(df.filter(items=['name','age', 'notes', 'basis']).sort_values(by=['name','age']))

#time.sleep(5)
#hdr.write("")
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
#for rec in detdat:
#    st.write(rec['key'], str(rec['age']), rec['name'])

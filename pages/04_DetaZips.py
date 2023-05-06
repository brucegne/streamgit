import streamlit as st
import pandas as pd
from deta import Deta
import json

# Connect to Deta Base with your Data Key
deta_key = "b0fhjqxu_fG4y33DEMaK8qWfMGABUSbn8cGFNxXhC"
zips_key = "b0fhjqxu_T35JeurA5CdztSiUEzBkxoaCvczQzurmgJ"

deta = Deta(zips_key)

db = deta.Base("Zipcode")

hdr = st.container()
qryString = {}
county = st.text_input("Enter partial county name and press enter.")
if county:
    qryString["county?contains"] = county.title()
    db_content = db.fetch(qryString).items
    try:
        df = pd.DataFrame(db_content)
        if len(df.filter(items=['city','county', 'state', 'population']).sort_values(by=['city','county']))>9:
            st.dataframe(df.filter(items=['city','county', 'state','zip', 'population']).sort_values(by=['city','county']))
            hdr.success("Total locations found :"+str(len(db_content)))
        else:
            hdr.info("No matches found." + str(qryString))
    except:
        st.error("Error processing query  " + str(qryString))
           
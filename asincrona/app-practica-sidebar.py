import pandas as pd
import streamlit as st

superstore_link = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'

df_super_store = pd.read_csv(superstore_link)

# Create the title for the web app
st.title("Practica de sidebar")

sidebar_aux = st.sidebar
sidebar_aux.title("Menú (SideBar)")

sidebar_aux.write("")
st.dataframe(df_super_store)

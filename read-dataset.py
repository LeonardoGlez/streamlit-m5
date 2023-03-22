import streamlit as st
import pandas as pd

names_link = "dataset.csv"
df_info = pd.read_csv(names_link)

st.title("DataFrame en Streamlit")
st.dataframe(df_info)
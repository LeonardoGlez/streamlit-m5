import streamlit as st
import pandas as pd

st.title('Streamlit con cache')
DATA_URL = 'dataset.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# Genera mensaje de cargando
data_load_state = st.text('Loading data...')
#solo lee mil registros
data = load_data(10000)
data_load_state.text("Done !")

st.dataframe(data)
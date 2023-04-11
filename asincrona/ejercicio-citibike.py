import streamlit as st
import pandas as pd

DATA_URL = 'fuentes/citibike-tripdata.csv'
DATE_COLUMN = 'started_at'

@st.cache
def load_data(number_rows):
  data = pd.read_csv(DATA_URL, nrows = number_rows)
  lowercase = lambda x: str(x).lower()
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  data.rename(lowercase, axis='columns', inplace=True)
  data.rename(columns={'start_lat':'lat','start_lng':'lon'}, inplace=True)
  return data


data_bike = load_data(100000) 

# crear title de la app web
st.title("Citibike maps")

sidebar = st.sidebar
sidebar.title("Filtros disponibles")

agree = sidebar.checkbox("todos los viajes?")
if agree:
    data_bike = load_data(500)

agree_porhora = sidebar.checkbox("Recorridos por hora?")
if agree:
    data_bike = load_data(500)
#st.write(data_bike['lat'].unique())
#st.write(data_bike['lon'].unique())

optionals = st.expander("Horas", True)
fare_select = optionals.slider(
    "Select the Fare",
    min_value=float(data_bike["Fare"].min()),
    max_value=float(data_bike["Fare"].max())
)
st.write(f"Total names : {data_bike.shape[0]}")
st.dataframe(data_bike)

st.map(data_bike)
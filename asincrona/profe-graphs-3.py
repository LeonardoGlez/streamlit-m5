import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'

titanic_data = pd.read_csv(titanic_link)

fig, ax = plt.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)

fig2, ax2 = plt.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')
st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)

st.markdown("___")
fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)

st.markdown("___")
st.write("Grafica de lineas desde streamlit")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.markdown("___")
st.write("Mapa de ciudad de San Francisco")

map_data = pd.DataFrame(
    #np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    np.random.randn(100, 2) / [50, 50] + [20.723606, -103.371153],
    columns=['lat', 'lon'])

st.map(map_data)
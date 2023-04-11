import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import codecs
import matplotlib.pyplot as plt

# Function with cache that load all employees
@st.cache
def load_dataAll():
    data = pd.read_csv("fuentes/Employees.csv")
    return data

# Function with cache that filter a number of rows
@st.cache
def load_data(nrows):
    data = pd.read_csv("fuentes/Employees.csv", nrows=nrows)
    return data

# Function with cache that filter by Emloyee_ID
@st.cache
def load_data_byname(name):
    data = pd.read_csv('fuentes/Employees.csv')
    filtered_data_byname = data[data['Employee_ID'].str.upper().str.contains(name)]
    return filtered_data_byname

# Function with cache that filter by HomeTown
@st.cache
def load_data_byhometown(filter_desc):
    data = pd.read_csv('fuentes/Employees.csv')
    filtered_data_byhometown = data[data['Hometown'].str.upper().str.contains(filter_desc)]
    return filtered_data_byhometown

# Function with cache that filter by Unit
@st.cache
def load_data_byunit(filter_desc):
    data = pd.read_csv('fuentes/Employees.csv')
    filtered_data_byunit = data[data['Unit'].str.upper().str.contains(filter_desc)]
    return filtered_data_byunit

# Function with cache that filter by Education_level
@st.cache
def load_data_byeducation_level(educ_level):
    data = pd.read_csv('fuentes/Employees.csv')
    filtered_data_byeduc_level = data[ data['Education_Level'] == educ_level ]
    return filtered_data_byeduc_level

# Function with cache that filter by Hometown
@st.cache
def load_data_byhometownSelect(hometown_selec):
    data = pd.read_csv('fuentes/Employees.csv')
    filtered_data_byHomeTownSelec = data[ data['Hometown'] == hometown_selec ]
    return filtered_data_byHomeTownSelec

# Function with cache that filter by Unit
@st.cache
def load_data_byUnitSelect(unit_selec):
    data = pd.read_csv('fuentes/Employees.csv')
    filtered_data_byUnitSelec = data[ data['Unit'] == unit_selec ]
    return filtered_data_byUnitSelec

df_employees = load_data(500)
df_employeescomplete = load_dataAll()

# crear title de la app web.
st.title("Employees App (By Leonardo Gonzalez)")

sidebar = st.sidebar
sidebar.title("Filters")

# Checkbox that show or hide datafram.
show_df = sidebar.checkbox("Show Data Frame?", value=True )
if show_df:
    # Create filter input by Employee_ID
    filter_employee = sidebar.text_input("Employee_ID:")
    if (sidebar.button('Find Employee_ID')):
        if (filter_employee):            
            df_employees = load_data_byname(filter_employee.upper())

    # Create filter input by Hometown
    filter_hometown = sidebar.text_input("Hometown:")
    if (sidebar.button('Find Hometown')):
        if (filter_hometown):            
            df_employees = load_data_byhometown(filter_hometown.upper())

    # Create filter input by Unit
    filter_unit = sidebar.text_input("Unit:")
    if (sidebar.button('Find Unit')):
        if (filter_unit):            
            df_employees = load_data_byunit(filter_unit.upper())

    # Create filter selectedbox by education level
    selc_education_level  = sidebar.selectbox('Select Education Level', df_employeescomplete.sort_values(by='Education_Level')['Education_Level'].unique())
    btnFilterbyEducLevel = sidebar.button('Find Education Level')
    if (btnFilterbyEducLevel):
        df_employees = load_data_byeducation_level( selc_education_level)
    
    # Create filter selectedbox by Hometown
    selc_hometown  = sidebar.selectbox('Select Hometown', df_employeescomplete.sort_values(by='Hometown')['Hometown'].unique())
    btnFilterbyHomeTown= sidebar.button('Find Hometown (Select)')
    if (btnFilterbyHomeTown):
        df_employees = load_data_byhometownSelect( selc_hometown)

    # Create filter selectedbox by Unit
    selc_unit  = sidebar.selectbox('Select Unit', df_employeescomplete.sort_values(by='Unit')['Unit'].unique())
    btnFilterbyUnit= sidebar.button('Find Unit (Select)')
    if (btnFilterbyUnit):
        df_employees = load_data_byUnitSelect( selc_unit)

    # Show information of employees 
    st.write(f"Total Employees : {df_employees.shape[0]}")
    st.dataframe(df_employees)

# Create Graphs   

# Graph Age
st.markdown("___")
fig, ax = plt.subplots()
ax.hist(df_employeescomplete["Age"])
ax.set_xlabel("Age")
st.header("Age Histogram")
st.pyplot(fig)

# Graph Unit
st.markdown("___")
fig2, ax2 = plt.subplots()
ax2.hist(df_employeescomplete["Unit"])
ax2.set_xlabel("Unit")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
st.header("Unit Frecuency")
st.pyplot(fig2)

# Graph Hometown 
st.markdown("___")
#Create new dataframe
df_empl_homtown = df_employeescomplete[['Hometown','Attrition_rate']].groupby('Hometown').sum()
#st.dataframe(df_empl_homtown)
fig3, ax3 = plt.subplots()
y_pos = df_empl_homtown.index
x_pos = df_empl_homtown['Attrition_rate']
ax3.barh(y_pos, x_pos)
ax3.set_ylabel("Hometown")
ax3.set_xlabel("Attrition rate")
st.header('Hometowns with more Attrition Rate')
st.pyplot(fig3)

# Graph Age vs Attrition Rate 
st.markdown("___")
#Create new dataframe
df_empl_Age = df_employeescomplete[['Age','Attrition_rate']].groupby('Age').sum()
#st.dataframe(df_empl_Age)
fig4, ax4 = plt.subplots()
y_pos2 = df_empl_Age.index
x_pos2 = df_empl_Age['Attrition_rate']
ax4.barh(y_pos2, x_pos2)
ax4.set_ylabel("Age")
ax4.set_xlabel("Attrition rate")
st.header('Ages with more Attrition Rate')
st.pyplot(fig4)


# Graph dispersion between Time of service and Attriton Rate
st.markdown("___")
fig3, ax3 = plt.subplots()
ax3.scatter(df_employeescomplete["Time_of_service"], df_employeescomplete["Attrition_rate"])
ax3.set_xlabel("Time of service")
ax3.set_ylabel("Attrition rate")
st.header("Relation between Time of service and Atrrition Rate")
st.pyplot(fig3)
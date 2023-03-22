import streamlit as st

myname = st.text_input('Nombre :')
if (myname):
  st.write(f"Tu nombre es : {myname}")
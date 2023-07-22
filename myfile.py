import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

st.title("Título del proyecto Jorge 2")
st.write("Hola, ¿**cómo** estás?")
st.write("Hola, ¿**cómo** estás?")
st.write("Bien")

#Lectura del dataframe
df = pd.read_excel('/app/streamlit_app/Catalogo1960_2021.xlsx')

#Magnitud
magnitudInicio = st.slider("Magnitud inicio:", 3, 9, step=1)
magnitudFin = st.slider("Magnitud fin:", magnitudInicio, 9, step=1)
#queryMagnitud = "MAGNITUD >= " + str(magnitudInicio) + " and MAGNITUD <= " + str(magnitudFin)
queryMagnitud = "MAGNITUD >= " + str(magnitudInicio)
#df = df.query("MAGNITUD >= {}".format(magnitudInicio))
df = df.query(queryMagnitud)

#Mostrar mapa
st.map(df)

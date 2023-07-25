import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
from datetime import datetime

st.title("Título del proyecto Jorge 2")
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

start_time = st.slider("Ver casos ocurridos en",value=datetime(2020, 1, 1, 9, 30),format="DD/MM/YY - hh:mm")
st.write("Fecha seleccionada:",


df = df.query(queryMagnitud)

#Mostrar mapa
st.map(df)

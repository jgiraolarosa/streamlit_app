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





start_time = st.slider("FECHA UTC",datetime(1960, 1, 1),datetime(2022, 1, 1))
st.write("Fecha seleccionada:", start_time)

queryTime = "FECHA_UTC >= " + str(start_time)


df = df.query(queryMagnitud & queryTime)
#df = df.query(queryTime)


#Mostrar mapa
st.map(df)

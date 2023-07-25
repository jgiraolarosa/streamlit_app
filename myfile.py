import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
from datetime import datetime

st.title("Título del proyecto Jorge 2")
st.write("Hola, ¿**cómo** estás?")
st.write("Bien")
st.write("Hola, ¿**cómo** estás?")



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


def iguala_formato(fecha_numero):
    string=str(fecha_numero)
    return datetime(int(string[:4]),int(string[4:6]),int(string[6:]))
    
df['FECHA_UTC_NEW']=df['FECHA_UTC'].apply(iguala_formato)
st.write(df['FECHA_UTC_NEW'])

#df = df[(df.MAGNITUD>=magnitudInicio)]
df = df[df.FECHA_UTC_NEW<start_time]
#df = df[(df.MAGNITUD>=magnitudInicio) & (df.FECHA_UTC>=start_time)]
#df = df.query(queryTime)


#Mostrar mapa
st.map(df)

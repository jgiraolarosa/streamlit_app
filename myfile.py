import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
from datetime import datetime

st.title("Sismos en Perú de 1960-2021")

#Lectura del dataframe
df = pd.read_excel('/app/streamlit_app/Catalogo1960_2021.xlsx')

#Magnitud
magnitudPosible = [3,4,5,6,7,8,9]
magInicio, magFin = st.select_slider("Magnitud del sismo:", options=magnitudPosible, value=(3,9))

#Fecha
start_time = st.slider("Fechas:", datetime(1960, 1, 1), datetime(2021, 12, 31))
#st.write("Fecha seleccionada:", start_time)
queryTime = "FECHA_UTC >= " + str(start_time)

def iguala_formato(fecha_numero):
    string=str(fecha_numero)
    return datetime(int(string[:4]),int(string[4:6]),int(string[6:]))
    
df['FECHA_UTC_NEW']=df['FECHA_UTC'].apply(iguala_formato)
#st.write(df['FECHA_UTC_NEW'])

#df = df[df.FECHA_UTC_NEW<start_time]
df = df[(df.MAGNITUD>=magInicio) & (df.MAGNITUD<=magFin)]
#df = df[df.MAGNITUD>=magInicio & df.MAGNITUD<=magFin & df.FECHA_UTC_NEW<start_time]
#df = df.query(queryTime)

#Mostrar mapa
st.map(df)

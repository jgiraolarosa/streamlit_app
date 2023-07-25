import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
from datetime import datetime

st.title("Sismos en Perú de 1960-2021")
st.write("En esta página podrá visualizar la ubicación y profundidad de los sismos ocurridos entre 1960 a 2021. A continuación, seleccione la magnitud y periodo de ocurrencia para visualizarlos en el mapa.")
#Lectura del dataframe
df = pd.read_excel('/app/streamlit_app/Catalogo1960_2021.xlsx')

#Magnitud
magnitudPosible = [3.0,4.0,5.0,6.0,7.0,8.0,9.0]
magInicio, magFin = st.select_slider("Magnitud:", options=magnitudPosible, value=(3.0,9.0))

#Fecha
fechaInicio = datetime(1960, 1, 1)
fechaFin = datetime(2021, 12, 31)
start_time, end_time = st.slider("Fechas:", fechaInicio, fechaFin, value=(fechaInicio,fechaFin))
#st.write("Fecha inicio seleccionada:", start_time)
#st.write("Fecha fin seleccionada:", end_time)
#queryTime = "FECHA_UTC >= " + str(start_time)

def iguala_formato(fecha_numero):
    string=str(fecha_numero)
    return datetime(int(string[:4]),int(string[4:6]),int(string[6:]))
    
df['FECHA_UTC_NEW']=df['FECHA_UTC'].apply(iguala_formato)
#st.write(df['FECHA_UTC_NEW'])

#df = df[df.FECHA_UTC_NEW<start_time]
df = df[(df.MAGNITUD>=magInicio) & (df.MAGNITUD<=magFin) & (df.FECHA_UTC_NEW>=start_time) & (df.FECHA_UTC_NEW<=end_time)]
#df = df[df.MAGNITUD>=magInicio & df.MAGNITUD<=magFin & df.FECHA_UTC_NEW<start_time]
#df = df.query(queryTime)

if magInicio == magFin:
    st.write("Se muestran los sismos de magnitud ", magInicio,"ocurridos entre", start_time, "a", end_time)
else:
    st.write("Se muestran los sismos en el rango de magnitud ", magInicio, " y ", magFin, "ocurridos entre", start_time, "a", end_time)
#Mostrar mapa
st.map(df,color=df.MAGNITUD)

#Fuente:
st.write("Fuente: Catálogo Sísmico del Perú de 1960 a 2021.[https://www.datosabiertos.gob.pe/dataset/catalogo-sismico-1960-2021-igp")

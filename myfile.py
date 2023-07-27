import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
from datetime import datetime

#Formato de fecha y hora para el query
def iguala_formato(fecha_numero):
    string=str(fecha_numero)
    return datetime(int(string[:4]),int(string[4:6]),int(string[6:]))

#Formato de hora
def format_time(hora):
    string = str(hora)
    input_str = string.zfill(6)
    # Extracting hours, minutes, and seconds from the input string
    hours = int(input_str[:2])
    minutes = int(input_str[2:4])
    seconds = int(input_str[4:6])

    # Formatting the time as "HH:MM:SS"
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return formatted_time

#Formato de fecha
def only_year(fecha_numero):
    string = str(fecha_numero)
    dt_object = datetime(int(string[:4]), int(string[4:6]), int(string[6:]))
    return dt_object.date()

#Color
def color(point):
    if point < 4:
        string='F40166'
    elif point <5:
        string='F5C35C'
    elif point < 6:
        string='FA904F'
    elif point < 7:
        string='EE704A'
    elif point < 8:
        string='E05B48'
    elif point < 9:
        string='CD3E43'
    else:
        string='B71D3E'
return string

st.title("Sismos en Perú de 1960-2021")
st.write("En esta página, podrá visualizar la ubicación y profundidad de los sismos percibidos por la población y registrados por la Red Sísmica Nacional entre 1960 a 2021. La información ha sido obtenido a partir del catálogo elaborado por el Instituto Geofísico del Perú (IGP), institución responsable del monitoreo de la actividad sísmica en el país.") 
st.write("A continuación, seleccione la magnitud y periodo de ocurrencia para visualizar la actividad sísmica en el mapa.")

#Lectura del dataframe
df = pd.read_excel('/app/streamlit_app/Catalogo1960_2021.xlsx')

#Magnitud
magnitudPosible = [3.0,4.0,5.0,6.0,7.0,8.0,9.0]
magInicio, magFin = st.select_slider("Magnitud:", options=magnitudPosible, value=(3.0,9.0))

#Fecha
fechaInicio = datetime(1960, 1, 1)
fechaFin = datetime(2021, 12, 31)
start_time, end_time = st.slider("Fechas:", fechaInicio, fechaFin, value=(fechaInicio,fechaFin))

#Ajustando los formatos de fecha y hora
df['FECHA_UTC_NEW']=df['FECHA_UTC'].apply(iguala_formato)
df['FECHA']=df['FECHA_UTC'].apply(only_year)
df['HORA_UTC_NEW']=df['HORA_UTC'].apply(format_time)

df['COLOR'] = df['MAGNITUD'].apply(color)

#Tamaño de los puntos
df['MAGNITUD_SIZE'] = df['MAGNITUD']*1000

#DF para el mapa
df = df[(df.MAGNITUD>=magInicio) & (df.MAGNITUD<=magFin) & (df.FECHA_UTC_NEW>=start_time) & (df.FECHA_UTC_NEW<=end_time)]

#DF para la tabla
df2 = df[(df.MAGNITUD>=magInicio) & (df.MAGNITUD<=magFin) & (df.FECHA_UTC_NEW>=start_time) & (df.FECHA_UTC_NEW<=end_time)]
df2 = df2.drop(["ID","FECHA_UTC","FECHA_UTC_NEW","HORA_UTC","FECHA_CORTE","MAGNITUD_SIZE"],axis=1)
df2 = df2.rename(columns={'HORA_UTC_NEW': 'HORA'})

#Descripción de la información mostrada
if magInicio == magFin:
    if df.empty:
        st.write("No ha ocurrido actividad sísmica de magnitud", magInicio, " entre", start_time, "a", end_time,".")
    else:
        st.write("Se muestran los sismos de magnitud ", magInicio,"ocurridos entre", start_time, "a", end_time,".")
        st.write ("Se ha registrado ", df2.shape[0], " sismos en total durante el periodo seleccionado.")
else:
    if df.empty:
        st.write("No ha ocurrido actividad sísmica en el rango de magnitud", magInicio, " y ", magFin, " entre", start_time, "a", end_time,".")
    else:
        st.write("Se muestran los sismos en el rango de magnitud ", magInicio, " y ", magFin, "ocurridos entre", start_time, "a", end_time,".")
        st.write ("Se ha registrado ", df2.shape[0], " sismos en total durante el periodo seleccionado.")

#Mostrar mapa
st.map(df, size='MAGNITUD_SIZE')
st.write("Datos de la actividad sísmica ocurrida:")
st.dataframe(df2, hide_index= True)

#Fuente:
st.write("Fuente: Catálogo Sísmico del Perú de 1960 a 2021. Link de acceso: https://www.datosabiertos.gob.pe/dataset/catalogo-sismico-1960-2021-igp")

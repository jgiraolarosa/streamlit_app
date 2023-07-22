import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

st.title("Título del proyecto Jorge 2")
st.write("Hola, ¿**cómo** estás?")
st.latex("\omega=x_2")

magnitud = st.slider("Magnitud:", 0, 9, step=1)
st.write("La magnitud es {}".format(magnitud))

appointment = st.slider("Programe la asesoria:", value=(time(11, 30), time(12, 45)))
st.write("Esta agendado para:", appointment)

df2 = pd.read_excel('/app/streamlit_app/Catalogo1960_2021.xlsx')
#df2 = df2.loc(df['MAGNITUD'] )
st.map(df2)
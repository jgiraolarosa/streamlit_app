import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

st.title("Título del proyecto Jorge 2")
st.write("Hola, ¿**cómo** estás?")
st.latex("\omega=x_2")

num = st.slider("num", 0, 100, step=1)
st.write("El número ingresado es {}".format(num))

appointment = st.slider("Programe la asesoria:", value=(time(11, 30), time(12, 45)))
st.write("Esta agendado para:", appointment)

n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)
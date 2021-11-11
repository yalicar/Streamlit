import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups - Entregas por Horas")
"""
### Cargar data
"""
data_source = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'
days = 'date/time'

@st.cache
def load_data(nrows):
    data = pd.read_csv(data_source, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[days] = pd.to_datetime(data[days])
    return data

data_load_state = st.text('Cargando data ...')
data = load_data(10000)

if st.checkbox('Mostrar data'):
    st.subheader('Data original')
    st.write(data)

st.subheader('Numero de Envios por Hora')
hist_values = np.histogram(data[days].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

"""
### Rango de datos
"""
hour_range = st.slider('hour', 0, 23, 17)
filtered_data = data[data[days].dt.hour == hour_range]

st.subheader('Mapa de envios a las %s:00' % hour_range)
st.map(filtered_data)



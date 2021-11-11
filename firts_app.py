import streamlit as st
import numpy as np
import pandas as pd

st.title("This is my first streamlit app, for Galileo Master!")

"""
## Operaciones Basicas
"""

x=4
st.write(x, 'square is', x*x)
x, 'square is', x*x

"""
## DataFrame
"""

df = pd.DataFrame({
    'column A': [1,2,3,4,5],
    'column B': ['A', 'B', 'C', 'D', 'E']
})
st.write(df)

"""
# Titulo
## Subtitul01
### Subtitul02
"""

df

"""
## Let's use some graphs
"""

chart_df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_df)

"""
## How about a map
"""

map_df = pd.DataFrame(
    np.random.randn(1000, 2) / [50,50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_df)

"""
## Show me some Widgets
"""

"""
### A checkbox
"""
if st.checkbox('show me the dataframe'):
    map_df
"""
## Slider test
"""

x = st.slider('Select value for X')
st.write(x, 'square is', x*x)

"""
## Options
"""

option = st.selectbox(
    'Which number do you like best?',
    [1,2,3,4,5,6,7,8,9,10]
)

'You selected the option', option

"""
## Progressbar
"""

import time
progress_bar_label = st.empty()
progress_bar = st.progress(0)
progress_bar_2 = st.sidebar.progress(0)

for i in range(100):
    progress_bar_label.text(f'Iteracion {i}')
    progress_bar.progress(i)
    time.sleep(0.001)

    for i in range(100):
        progress_bar_2.progress(i)
        time.sleep(0.001)

option_side = st.sidebar.selectbox('choose your weapon?', ['handgun', 'machinegun', 'knife'])
st.sidebar.write(' Your weapon of choice is:', option_side)

another_slider = st.sidebar.slider('Select the range',
                           0.0, 25.0, (25.0, 75.0))
st.sidebar.write('The range selected is', another_slider)

"""
## Progressbar
"""
import streamlit as st
import numpy as np
import holoviews as hv

st.title('Holoview Test')

img = hv.Image(np.random.rand(10, 10))

fig = hv.render(img, backend='bokeh')

st.bokeh_chart(fig)

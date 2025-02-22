import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


Incendios = pd.read_csv("C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/new/datascience_course/4_data_visualization/aula3/Incendios.csv", encoding='latin1')

print(Incendios.info())

st.title("Incendios no México")



# Mapa de localizações e causas dos incêndios
fig_map = px.scatter_mapbox(Incendios, lat="Latitud", lon="Longitud", hover_name="Estado", hover_data=["Municipio", "Causa"],
                            color="Causa", zoom=5, height=600, title="Mapa de Localizações e Causas dos Incêndios")
fig_map.update_layout(mapbox_style="open-street-map", mapbox_center={"lat": 23.6345, "lon": -102.5528}, mapbox_zoom=5)
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Mostrar o mapa no Streamlit
st.plotly_chart(fig_map)


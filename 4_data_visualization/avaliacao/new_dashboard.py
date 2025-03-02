import pandas as pd
import streamlit as st
import plotly.express as px
from geopy.geocoders import Nominatim


df = pd.read_csv("/home/anaraujo/Desktop/datascience_course/weather_update.csv")

tab1, tab2, tab3 = st.tabs(["Overview", "By location", "By date"])

recent_date = df['Date'].max()
df_recent = df[df['Date'] == recent_date]
print(recent_date)

with tab1:
    df_recent['Temperature_Text'] = df_recent['MaxTemp'].astype(str) + '°C  ' \
                                     + df_recent['MinTemp'].astype(str) + '°C'
    
    fig = px.scatter_map(df_recent, lat="Latitude", lon="Longitude", hover_name="Location",
                            hover_data=["MaxTemp", "MinTemp"],
                            text="Temperature_Text",
                            zoom=5, height=700)

    fig.update_traces(textfont=dict(color="blue", size=12))
    fig.update_layout(title='Sábado, 25 de Junho', mapbox_style="open-street-map")
    fig.show()

    st.plotly_chart(fig)
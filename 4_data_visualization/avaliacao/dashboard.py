import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("/home/acer/Desktop/datascience_course/4_data_visualization/avaliacao/rain/rain_aus/weatherAUS.csv")

tab1, tab2, tab3 = st.tabs(["Overview", "Temperatura", "Precepitação"])

df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

df_monthly_temp = df.groupby(['Year', 'Month'])['MaxTemp'].mean().reset_index()


month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


graph_temp = px.line(df_monthly_temp, x='Month', y='MaxTemp', color='Year', 
              title="Temperatura Média Mensal por Ano",
              labels={'MaxTemp': 'Temperatura Máxima (°C)', 'Month': 'Mês'},
              line_shape='linear')


graph_temp.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=list(range(1, 13)),
        ticktext=month_names
    )
)


df['dif_temp_max_min']=df['MaxTemp'] - df['MinTemp']
df_monthly_temp_max_min = df.groupby(['Year', 'Month'])['dif_temp_max_min'].mean().reset_index()

graph_temp_diff = px.line(df_monthly_temp, x='Month', y='MaxTemp', color='Year', 
              title="Média mensal da diferença entre temperatura máxima e minima por Ano",
              labels={'MaxTemp': 'diferença de temperatura (°C)', 'Month': 'Mês'},
              line_shape='linear')


graph_temp_diff.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=list(range(1, 13)),
        ticktext=month_names
    )
)

with tab2:
    st.plotly_chart(graph_temp)
    st.plotly_chart(graph_temp_diff)
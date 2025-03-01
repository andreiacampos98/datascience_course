import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Carregar os dados
df = pd.read_csv("/home/acer/Desktop/datascience_course/4_data_visualization/avaliacao/rain/rain_aus/weatherAUS.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['dif_temp_max_min'] = df['MaxTemp'] - df['MinTemp']

# Configuração da página
st.set_page_config(layout="wide")
st.sidebar.title("Dashboard Climático")

# Filtros na sidebar
aba = st.sidebar.radio("Escolha a análise:", ["Overview", "Temperatura", "Precipitação"])
locations = df['Location'].unique()
selected_location = st.sidebar.selectbox("Selecione a Localização:", locations)

anos_disponiveis = sorted(df['Year'].unique())
anos_selecionados = st.sidebar.multiselect("Selecione os anos:", anos_disponiveis, default=anos_disponiveis)
meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mes_selecionado = st.sidebar.slider("Selecione o mês:", 1, 12, (1, 12))

# Filtro base
df_filtered = df[(df['Location'] == selected_location) & (df['Year'].isin(anos_selecionados))]

def criar_grafico_linha(df, x, y, titulo, y_label):
    fig = px.line(df, x=x, y=y, color='Year', title=titulo,
                  labels={y: y_label, x: "Mês"}, line_shape='linear')
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=list(range(1, 13)), ticktext=meses))
    return fig

if aba == "Overview":
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperatura Máxima Média", f"{df_filtered['MaxTemp'].mean():.1f}°C")
    col2.metric("Dias > 35°C (Média)", f"{(df_filtered['MaxTemp'] > 35).sum()} dias")
    col3.metric("Precipitação Média", f"{df_filtered['Rainfall'].mean():.1f} mm")

elif aba == "Temperatura":
    tab1, tab2, tab3, tab4 = st.tabs(["Média Mensal", "Diferença Máx-Mín", "Dias > 35°C", "Dias < 0°C"])

    with tab1:
        df_temp = df_filtered.groupby(['Year', 'Month'])['MaxTemp'].mean().reset_index()
        st.plotly_chart(criar_grafico_linha(df_temp, 'Month', 'MaxTemp', "Temperatura Média Mensal por Ano", "Temperatura (°C)"))
    
    with tab2:
        df_diff = df_filtered.groupby(['Year', 'Month'])['dif_temp_max_min'].mean().reset_index()
        st.plotly_chart(criar_grafico_linha(df_diff, 'Month', 'dif_temp_max_min', "Média Mensal da Diferença de Temperatura", "Diferença (°C)"))
    
    with tab3:
        df_hot_days = df_filtered[df_filtered['MaxTemp'] > 35].groupby(['Year', 'Month'])['MaxTemp'].count().reset_index()
        df_hot_days.rename(columns={'MaxTemp': 'DaysAbove35'}, inplace=True)
        st.plotly_chart(criar_grafico_linha(df_hot_days, 'Month', 'DaysAbove35', "Dias Acima de 35°C", "Número de Dias"))
    
    with tab4:
        df_cold_days = df_filtered[df_filtered['MinTemp'] < 0].groupby(['Year', 'Month'])['MinTemp'].count().reset_index()
        df_cold_days.rename(columns={'MinTemp': 'DaysBelow0'}, inplace=True)
        st.plotly_chart(criar_grafico_linha(df_cold_days, 'Month', 'DaysBelow0', "Dias Abaixo de 0°C", "Número de Dias"))

elif aba == "Precipitação":
    tab1, tab2 = st.tabs(["Precipitação Média", "Dias Chuvosos (>20mm)"])

    with tab1:
        df_rain = df_filtered.groupby(['Year', 'Month'])['Rainfall'].mean().reset_index()
        st.plotly_chart(criar_grafico_linha(df_rain, 'Month', 'Rainfall', "Precipitação Média Mensal", "Precipitação (mm)"))
    
    with tab2:
        df_rain_days = df_filtered[df_filtered['Rainfall'] > 20].groupby(['Year', 'Month'])['Rainfall'].count().reset_index()
        df_rain_days.rename(columns={'Rainfall': 'DaysAbove20mm'}, inplace=True)
        st.plotly_chart(criar_grafico_linha(df_rain_days, 'Month', 'DaysAbove20mm', "Dias com Precipitação > 20mm", "Número de Dias"))

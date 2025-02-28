import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("/home/acer/Desktop/datascience_course/4_data_visualization/avaliacao/rain/rain_aus/weatherAUS.csv")

tab1, tab2, tab3 = st.tabs(["Overview", "Temperatura", "Precepitação"])

df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

with tab2:
    locations = df['Location'].unique()
    selected_location = st.selectbox("Selecione a Localização:", locations, key="location_filter")

    anos_disponiveis = sorted(df['Year'].unique())
    anos_selecionados = st.multiselect("Selecione os anos:", anos_disponiveis, default=anos_disponiveis)


    #Evolução da temperatura máxima média mensal ao longo do tempo
    df_monthly_temp = df.groupby(['Location','Year', 'Month'])['MaxTemp'].mean().reset_index()
    filtered_monthly_temp = df_monthly_temp[df_monthly_temp['Location'] == selected_location]
    filtered_monthly_temp = filtered_monthly_temp[filtered_monthly_temp['Year'].isin(anos_selecionados)]

    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


    graph_temp = px.line(filtered_monthly_temp, x='Month', y='MaxTemp', color='Year', 
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

    st.plotly_chart(graph_temp)
    
    df['dif_temp_max_min']=df['MaxTemp'] - df['MinTemp']
    df_monthly_temp_max_min = df.groupby(['Location','Year', 'Month'])['dif_temp_max_min'].mean().reset_index()
    filtered_monthly_max_min = df_monthly_temp_max_min[df_monthly_temp_max_min['Location'] == selected_location]
    filtered_monthly_max_min = filtered_monthly_max_min[filtered_monthly_max_min['Year'].isin(anos_selecionados)]


    graph_temp_diff = px.line(filtered_monthly_max_min, x='Month', y='dif_temp_max_min', color='Year', 
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
    st.plotly_chart(graph_temp_diff)


    #numero de dias com temperatura máxima 35
    dias_acima_35=df[df['MaxTemp'] > 35].groupby(['Location','Year', 'Month'])['MaxTemp'].count().reset_index()
    dias_acima_35.rename(columns={'MaxTemp': 'DaysAbove35'}, inplace=True)
    filtered_data_35 = dias_acima_35[dias_acima_35['Location'] == selected_location]
    filtered_data_35 = filtered_data_35[filtered_data_35['Year'].isin(anos_selecionados)]

    graph_acima_35 = px.line(filtered_data_35, 
                            x='Month', 
                            y='DaysAbove35', 
                            color='Year',  
                            title='Evolução do número de dias com temperatura acima de 35°C',
                            labels={'DaysAbove35': 'Número de dias com temperatura acima de 35°C', 'Month': 'Mês'},
                            line_shape='linear')

    graph_acima_35.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=month_names
        )
    )
    
    #numero de dias com temperatura abaixo de 0
    dias_abaixo_0=df[df['MinTemp'] < 0].groupby(['Location','Year', 'Month'])['MinTemp'].count().reset_index()
    dias_abaixo_0.rename(columns={'MinTemp': 'DaysBelow0'}, inplace=True)
    filtered_data_0 = dias_abaixo_0[dias_abaixo_0['Location'] == selected_location]
    filtered_data_0 = filtered_data_0[filtered_data_0['Year'].isin(anos_selecionados)]

    graph_abaixo_0 = px.line(filtered_data_0, 
                            x='Month', 
                            y='DaysBelow0', 
                            color='Year',  
                            title='Evolução do número de dias com temperatura abaixo de 0°C',
                            labels={'DaysBelow0': 'Número de dias com temperatura abaixo de 0°C', 'Month': 'Mês'},
                            line_shape='linear')

    graph_abaixo_0.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=month_names
        )
    )


    st.plotly_chart(graph_acima_35)
    st.plotly_chart(graph_abaixo_0)
import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("/home/acer/Desktop/datascience_course/4_data_visualization/avaliacao/rain/rain_aus/weatherAUS.csv")

st.set_page_config(layout="wide")
st.sidebar.title("Dashboard")
aba = st.sidebar.radio("Escolha a análise:", ["Overview", "Temperatura", "Precipitação"])


df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

if aba == "Temperatura":
    locations = df['Location'].unique()
    selected_location = st.selectbox("Selecione a Localização:", locations, key="location_filter")

    anos_disponiveis = sorted(df['Year'].unique())
    anos_selecionados = st.multiselect("Selecione os anos:", anos_disponiveis, default=anos_disponiveis)


    base_df = df[['Location', 'Year', 'Month']].drop_duplicates()

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

    # Evolução da diferença de temperatura maxima e minima no dia ao longo do tempo
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
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(graph_temp, use_container_width=True)
    with col2:
        st.plotly_chart(graph_temp_diff, use_container_width=True)



    #numero de dias com temperatura máxima 35
    dias_acima_35=df[df['MaxTemp'] > 35].groupby(['Location','Year', 'Month'])['MaxTemp'].count().reset_index()
    dias_acima_35.rename(columns={'MaxTemp': 'DaysAbove35'}, inplace=True)

    dias_acima_35 = base_df.merge(dias_acima_35, on=['Location', 'Year', 'Month'], how='left')
    dias_acima_35['DaysAbove35'] = dias_acima_35['DaysAbove35'].fillna(0)

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

    dias_abaixo_0 = base_df.merge(dias_abaixo_0, on=['Location', 'Year', 'Month'], how='left')
    dias_abaixo_0['DaysBelow0'] = dias_abaixo_0['DaysBelow0'].fillna(0)

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
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(graph_acima_35, use_container_width=True)
    with col2:
        st.plotly_chart(graph_abaixo_0, use_container_width=True)

elif aba == "Precipitação":
    locations = df['Location'].unique()
    selected_location = st.selectbox("Selecione a Localização:", locations, key="location_filter")

    anos_disponiveis = sorted(df['Year'].unique())
    anos_selecionados = st.multiselect("Selecione os anos:", anos_disponiveis, default=anos_disponiveis)
    base_df = df[['Location', 'Year', 'Month']].drop_duplicates()

    #Evolução da temperatura máxima média mensal ao longo do tempo
    df_monthly_rain = df.groupby(['Location','Year', 'Month'])['Rainfall'].mean().reset_index()
    filtered_monthly_rain = df_monthly_rain[df_monthly_rain['Location'] == selected_location]
    filtered_monthly_rain = filtered_monthly_rain[filtered_monthly_rain['Year'].isin(anos_selecionados)]

    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


    graph_prec = px.line(filtered_monthly_rain, x='Month', y='Rainfall', color='Year', 
                title="Precipitação em mm média Mensal por Ano",
                labels={'MaxTemp': 'Precipitação em mm', 'Month': 'Mês'},
                line_shape='linear')


    graph_prec.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=month_names
        )
    )


    dias_prec_20=df[df['Rainfall'] > 20].groupby(['Location','Year', 'Month'])['Rainfall'].count().reset_index()
    dias_prec_20.rename(columns={'Nb_days_prec_20': 'Rainfall'}, inplace=True)

    dias_prec_20 = base_df.merge(dias_prec_20, on=['Location', 'Year', 'Month'], how='left')
    dias_prec_20['Rainfall'] = dias_prec_20['Rainfall'].fillna(0)

    filtered_data_prec_20 = dias_prec_20[dias_prec_20['Location'] == selected_location]
    filtered_data_prec_20 = filtered_data_prec_20[filtered_data_prec_20['Year'].isin(anos_selecionados)]

    graph_prec_20 = px.line(filtered_data_prec_20, 
                            x='Month', 
                            y='Rainfall', 
                            color='Year',  
                            title='Evolução do número de dias com precipitação acima de 20 mm',
                            labels={'Rainfall': 'Número de dias com precipitação acima de 20 mm', 'Month': 'Mês'},
                            line_shape='linear')

    graph_prec_20.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=month_names
        )
    )
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(graph_prec, use_container_width=True)
    with col2:
        st.plotly_chart(graph_prec_20, use_container_width=True)
    
elif aba == "Overview":
    locations = df['Location'].unique()
    selected_location = st.selectbox("Selecione a Localização:", locations, key="location_filter")

    year = df['Year'].unique()
    selected_year = st.selectbox("Selecione o ano:", year, key="year_filter")

    col1, col2, col3 = st.columns(3)
    df_max_temp=df.groupby(['Location','Year'])['MaxTemp'].max().reset_index()
    #filtered_max_temp = df_max_temp[
    #    (df_max_temp['Location'] == selected_location) & 
    #    (df_max_temp['Year'] == selected_year)
    #]
    current_temp = df_max_temp[
        (df_max_temp['Location'] == selected_location) & 
        (df_max_temp['Year'] == selected_year)
    ]

    previous_temp = df_max_temp[
        (df_max_temp['Location'] == selected_location) & 
        (df_max_temp['Year'] == selected_year - 1)
    ]

    max_temp = current_temp['MaxTemp'].values[0] if not current_temp.empty else None
    prev_max_temp = previous_temp['MaxTemp'].values[0] if not previous_temp.empty else None

    # Calculate percentage change
    if max_temp is not None and prev_max_temp is not None and prev_max_temp != 0:
        temp_change = ((max_temp - prev_max_temp) / prev_max_temp) * 100
        temp_change_str = f"{temp_change:.1f}%"
        delta_color = "normal" if temp_change < 0 else "inverse"  # Red for decrease, Green for increase
    else:
        temp_change_str = "N/A"
        delta_color = "off"

    '''
    if not filtered_max_temp.empty:
        max_temp = filtered_max_temp['MaxTemp'].values[0]
    else:
        max_temp = "No data"
    '''


    df_min_temp=df.groupby(['Location','Year'])['MinTemp'].min().reset_index()
    filtered_min_temp = df_min_temp[
        (df_min_temp['Location'] == selected_location) & 
        (df_min_temp['Year'] == selected_year)
    ]
    if not filtered_min_temp.empty:
        min_temp = filtered_min_temp['MinTemp'].values[0]
    else:
        min_temp = "No data"


    col1.metric("Temperatura Máxima", f"{max_temp:.1f}°C", temp_change_str, delta_color=delta_color)
    #col1.metric("Temperatura Máxima", f"{max_temp}°C")
    col1.metric("Temperatura Minima", f"{min_temp}°C")
    #col2.metric("Dias > 35°C (Média)", f"{(df_filtered['MaxTemp'] > 35).sum()} dias")
    #col3.metric("Precipitação Média", f"{df_filtered['Rainfall'].mean():.1f} mm")

import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("/home/anaraujo/Desktop/datascience_course/weather_update.csv")

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

    col1, col2, col3 = st.columns([1, 1, 3]) 
    
    # Temperatura Máxima
    df_max_temp = df.groupby(['Location', 'Year'])['MaxTemp'].max().reset_index()
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

    if max_temp is not None and prev_max_temp is not None and prev_max_temp != 0:
        temp_change = ((max_temp - prev_max_temp) / prev_max_temp) * 100
        temp_change_str = f"{temp_change:.1f}%"
        delta_color = "normal" if temp_change > 0 else "inverse"
    else:
        temp_change_str = "N/A"
        delta_color = "off"
    
    # Exibir a métrica de temperatura máxima
    col1.metric("Temperatura Máxima", f"{max_temp:.1f}°C", temp_change_str, delta_color=delta_color)
    
    # Temperatura Mínima
    df_min_temp = df.groupby(['Location', 'Year'])['MinTemp'].min().reset_index()
    current_temp_min = df_min_temp[
        (df_min_temp['Location'] == selected_location) & 
        (df_min_temp['Year'] == selected_year)
    ]

    previous_temp_min = df_min_temp[
        (df_min_temp['Location'] == selected_location) & 
        (df_min_temp['Year'] == selected_year - 1)
    ]

    min_temp = current_temp_min['MinTemp'].values[0] if not current_temp_min.empty else None
    prev_min_temp = previous_temp_min['MinTemp'].values[0] if not previous_temp_min.empty else None

    if min_temp is not None and prev_min_temp is not None and prev_min_temp != 0:
        temp_change_min = ((min_temp - prev_min_temp) / prev_min_temp) * 100
        temp_change_min_str = f"{temp_change_min:.1f}%"
        delta_color_min = "normal" if temp_change_min > 0 else "inverse"
    else:
        temp_change_min_str = "N/A"
        delta_color_min = "off"
    
    # Exibir a métrica de temperatura mínima
    col2.metric("Temperatura Mínima", f"{min_temp:.1f}°C", temp_change_min_str, delta_color=delta_color_min)

    # Dias acima de 35°C
    df_nb_days_above_35 = df[df['MaxTemp'] > 35].groupby(['Location', 'Year'])['MaxTemp'].count().reset_index(name="DaysAbove35")
    current_nb_35 = df_nb_days_above_35[
        (df_nb_days_above_35['Location'] == selected_location) & 
        (df_nb_days_above_35['Year'] == selected_year)
    ]

    previous_nb_35 = df_nb_days_above_35[
        (df_nb_days_above_35['Location'] == selected_location) & 
        (df_nb_days_above_35['Year'] == selected_year - 1)
    ]

    nb_35 = current_nb_35['DaysAbove35'].values[0] if not current_nb_35.empty else 0
    prev_nb_35 = previous_nb_35['DaysAbove35'].values[0] if not previous_nb_35.empty else 0

    if prev_nb_35 != 0:
        var_nb_35 = ((nb_35 - prev_nb_35) / prev_nb_35) * 100
        nb_35_str = f"{var_nb_35:.1f}%"
        delta_color = "normal" if var_nb_35 > 0 else "inverse"
    else:
        nb_35_str = "N/A"
        delta_color = "off"

    # Exibir a métrica de dias acima de 35°C
    col1.metric("Dias > 35°C", f"{nb_35} dias", nb_35_str, delta_color=delta_color)

    # Dias com precipitação superior a 10 mm
    df_nb_prec_10 = df[df['Rainfall'] > 35].groupby(['Location', 'Year'])['Rainfall'].count().reset_index(name="DaysAbove35")
    current_prec_10 = df_nb_prec_10[
        (df_nb_prec_10['Location'] == selected_location) & 
        (df_nb_prec_10['Year'] == selected_year)
    ]

    previous_prec_10 = df_nb_prec_10[
        (df_nb_prec_10['Location'] == selected_location) & 
        (df_nb_prec_10['Year'] == selected_year - 1)
    ]

    nb_10 = current_prec_10['DaysAbove35'].values[0] if not current_prec_10.empty else 0
    prev_nb_10 = previous_prec_10['DaysAbove35'].values[0] if not previous_prec_10.empty else 0

    if prev_nb_10 != 0:
        var_nb_10 = ((nb_10 - prev_nb_10) / prev_nb_10) * 100
        nb_10_str = f"{var_nb_10:.1f}%"
        delta_color = "normal" if var_nb_10 > 0 else "inverse"
    else:
        nb_10_str = "N/A"
        delta_color = "off"

    # Exibir a métrica de dias com precipitação superior a 10 mm
    col2.metric("Dias > 10 mm", f"{nb_10} dias", nb_10_str, delta_color=delta_color)

    # Mapa da localização
    locations_coords = df[['Location', 'Latitude', 'Longitude']].drop_duplicates()
    if selected_location in locations_coords['Location'].values:
        coords = locations_coords.loc[locations_coords['Location'] == selected_location, ['Latitude', 'Longitude']].iloc[0]
        lat, lon = coords['Latitude'], coords['Longitude']
        
        # Criar o mapa com Plotly
        fig_map = px.scatter_map(
            pd.DataFrame({'City': [selected_location], 'Lat': [lat], 'Lon': [lon]}),
            lat="Lat",
            lon="Lon",
            hover_name="City",
            zoom=5
        )

        # Ajustar o estilo do mapa diretamente com `update_geos`
        fig_map.update_geos(
            visible=True,
            resolution=110,
            showcountries=True,
            showland=True,
            landcolor="lightgray",
            countrycolor="black",
            showlakes=True,
            lakecolor="white"
        )


        fig_map.update_layout(
            margin={"r":0,"t":0,"l":0,"b":0}
        )


        col3.plotly_chart(fig_map,use_container_height=True, use_container_width=True, config={"displayModeBar": False})

    else:
        col3.warning("Coordenadas não encontradas para esta cidade.")


    #col2.metric("Precipitação Média", f"{df_filtered['Rainfall'].mean():.1f} mm")

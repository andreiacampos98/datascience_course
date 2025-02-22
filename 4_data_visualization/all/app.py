import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(layout="wide")

# Carregar os dados
def load_data():
    file_path = 'fires/Fires.csv.zip'
    df = pd.read_csv(file_path, encoding='latin1')

    # Ajustar tipos de dados
    df['Start_Date'] = pd.to_datetime(df['Start_Date'], errors='coerce')
    df['End_Date'] = pd.to_datetime(df['End_Date'], errors='coerce')

    # Converter durações para segundos
    def duration_to_seconds(duration_str):
        try:
            h, m, s = map(int, duration_str.split(':'))
            return h * 3600 + m * 60 + s
        except:
            return None

    df['Detection_seconds'] = df['Detection'].apply(duration_to_seconds)
    df['Arrival_seconds'] = df['Arrival'].apply(duration_to_seconds)
    df['Duration_seconds'] = df['Duration'].apply(duration_to_seconds)

    # Adicionar tempo de resposta
    df['Response_Time_seconds'] = df['Detection_seconds'] + df['Arrival_seconds']
    return df

data = load_data()

# Título do Dashboard
st.title('Dashboard de Monitoramento de Incêndios Florestais')

# Filtros
st.sidebar.header('Filtros')
selected_year = st.sidebar.multiselect('Ano', options=data['Year'].unique(), default=data['Year'].unique())
selected_region = st.sidebar.multiselect('Região', options=data['Region'].unique(), default=data['Region'].unique())

# Filtrar os dados com base nos filtros
filtered_data = data[(data['Year'].isin(selected_year)) & (data['Region'].isin(selected_region))]

# Encontrar o ano mais recente
recent_year = filtered_data['Year'].max()

# Filtrar os dados para o ano mais recente
filtered_recent_data = filtered_data[filtered_data['Year'] == recent_year]

# Tabs para diferentes análises
tab_summary, tab1, tab2, tab3, tab4 = st.tabs(["Resumo Executivo", "Incêndios por Ano", "Incêndios por Região", "Vegetação Atingida", "Mapa dos Incêndios"])

# Resumo Executivo
with tab_summary:
    st.header('Resumo Executivo')
    
    # Exibir o ano mais recente
    st.subheader(f"Ano Mais Recente: {recent_year}")

    total_fires = filtered_recent_data.shape[0]
    total_area = filtered_recent_data['Total_hectares'].sum()
    avg_response = filtered_recent_data['Response_Time_seconds'].mean() / 60  # Converter para minutos
    avg_duration = filtered_recent_data['Duration_seconds'].mean() / 3600  # Converter para horas

    # Apresentar os valores com design mais apelativo
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total de Incêndios", value=total_fires)
    with col2:
        st.metric(label="Área Queimada (ha)", value=f"{total_area:,.2f}")
    with col3:
        st.metric(label="Tempo Médio de Resposta (min)", value=f"{avg_response:.2f}")
    with col4:
        st.metric(label="Duração Média do Fogo (h)", value=f"{avg_duration:.2f}")

    st.write("### Notas:")
    st.write("- A maior parte dos incêndios ocorre em regiões específicas. Use os gráficos para explorar.")
    st.write("- O tempo médio de resposta está dentro de limites aceitáveis, mas pode ser melhorado.")
    st.write("- Algumas regiões apresentam áreas queimadas significativamente maiores, exigindo atenção especial.")

# Gráfico 1: Incêndios por Ano
with tab1:
    st.header('Distribuição de Incêndios por Ano')
    fire_count_year = filtered_data.groupby('Year').size().reset_index(name='Count')
    fig1 = px.bar(fire_count_year, x='Year', y='Count', color='Count', color_continuous_scale='Oranges', title='Incêndios por Ano')
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Incêndios por Região
with tab2:
    st.header('Incêndios por Região')
    fire_count_region = filtered_data['Region'].value_counts().reset_index()
    fire_count_region.columns = ['Region', 'Count']
    fig2 = px.bar(fire_count_region, x='Count', y='Region', orientation='h', color='Count', color_continuous_scale='Oranges', title='Incêndios por Região')
    st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Tipo de Vegetação Atingida
with tab3:
    st.header('Tipo de Vegetação Mais Atingida')
    vegetation_count = filtered_data['Vegetation_type'].value_counts().reset_index()
    vegetation_count.columns = ['Vegetation_type', 'Count']
    fig3 = px.bar(vegetation_count, x='Count', y='Vegetation_type', orientation='h', color='Count', color_continuous_scale='Oranges', title='Tipos de Vegetação Atingida')
    st.plotly_chart(fig3, use_container_width=True)

# Mapa dos Incêndios
with tab4:
    st.header('Mapa dos Incêndios')
    map_data = filtered_data.dropna(subset=['Latitude', 'Longitude'])
    
    # Definir o valor máximo da duração para a escala de cores
    max_duration = 7.619900e+04  # Definido o valor máximo da escala de cor

    fig4 = px.scatter_mapbox(
        map_data,
        lat='Latitude',
        lon='Longitude',
        color='Duration_seconds',  # Cor pela duração
        size='Total_hectares',
        hover_name='Municipality',
        hover_data={
            'Year': True,
            'Start_Date': True,
            'End_Date': True,
            'Total_hectares': True,
            'Duration_seconds': True
        },
        color_continuous_scale='Viridis',  # Usar uma escala contínua para duração
        range_color=[0, max_duration],  # Limitar a escala de cores até o valor máximo
        title='Localização dos Incêndios no México'
    )
    fig4.update_layout(
        mapbox_style="open-street-map",
        margin={"r":0,"t":30,"l":0,"b":0}
    )
    st.plotly_chart(fig4, use_container_width=True)

import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Carregar os dados
Incendios = pd.read_csv("C:/Users/Andreia.CAMPOS/OneDrive - CLASQUIN SA/Desktop/new/datascience_course/4_data_visualization/aula3/Incendios.csv", encoding='latin1')

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Dashboard de Incêndios no México"),
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in Incendios['Región'].unique()],
        value='Centro'
    ),
    dcc.Graph(id='mapa-incendios'),
    dcc.Graph(id='grafico-causas')
])

# Callback para atualizar o mapa com base na região selecionada
@app.callback(
    Output('mapa-incendios', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_map(selected_region):
    filtered_data = Incendios[Incendios['Región'] == selected_region]
    fig = px.scatter_mapbox(filtered_data, lat="Latitud", lon="Longitud", hover_name="Estado", hover_data=["Municipio", "Causa"],
                            color="Causa", zoom=5, height=600, title="Mapa de Localizações e Causas dos Incêndios")
    fig.update_layout(mapbox_style="open-street-map", mapbox_center={"lat": 23.6345, "lon": -102.5528}, mapbox_zoom=5)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

# Callback para atualizar o gráfico de causas com base na região selecionada
@app.callback(
    Output('grafico-causas', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_cause_chart(selected_region):
    filtered_data = Incendios[Incendios['Región'] == selected_region]
    fig = px.histogram(filtered_data, y='Causa', title='Análise das Causas dos Incêndios', labels={'Causa':'Causa'})
    return fig

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)

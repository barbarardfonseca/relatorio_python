# import micropip
# await micropip.install(["pandas", "plotly"])

import pandas as pd
import plotly.express as px
from js import document
# from pyscript import display
from js import document, Plotly  # Importa o Plotly do JavaScript

import sys

# Verificar se o Pyodide está rodando corretamente
print(f"Versão do Python: {sys.version}")

# Carregar os dados do HTML
data_placeholder = document.querySelector("#data_placeholder").innerText
all_data = pd.read_json(data_placeholder)

# Processar os dados
MapSales = all_data.groupby(['CityName', 'Lat', 'Long'])['TotalSaleValue'].sum().reset_index()
# Corrigir a inversão de latitude e longitude
MapSales.rename(columns={"Lat": "lon_temp", "Long": "lat"}, inplace=True)
MapSales.rename(columns={"lon_temp": "lon"}, inplace=True)


# Criar o mapa com Plotly
fig = px.scatter_map(
    MapSales,
    lat="lat",
    lon="lon",
    size="TotalSaleValue",
    color="TotalSaleValue",
    hover_name="CityName",
    # hover_data={"lat": False, "lon": False},
    title="Mapa de Vendas por Cidade",
    color_continuous_scale=px.colors.sequential.Viridis,
    size_max=15,
    zoom=4
)

# Configurar o estilo do mapa

fig.update_layout(
    mapbox_style="open-street-map",
    margin={"r": 0, "t": 40, "l": 0, "b": 0},
    mapbox=dict(center=dict(lat=-14.2350, lon=-51.9253), zoom=4)  # Centro do Brasil
)

# Criar um gráfico de barras simples como teste
fig_teste = px.bar(MapSales, x="CityName", y="TotalSaleValue", title="Teste de Gráfico")

# Renderizar o gráfico simples antes do mapa
# Plotly.newPlot("graphicmap", fig_teste)


# Exibir o gráfico no HTML
# display(fig, target="graphicmap")
Plotly.newPlot("graphicmap", fig)
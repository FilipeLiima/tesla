from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from app import app

# Componentes
from _map import *
from _controllers import *


# Carregar o arquivo de dados
df_data = pd.read_csv("dataset/SuperchargeLocations.csv", encoding="ISO-8859-1")
state_counts = df_data.copy()

# Dividir a coluna 'GPS' em 'Latitude' e 'Longitude'
state_counts[["Latitude", "Longitude"]] = state_counts["GPS"].str.split(
    ",", expand=True
)

# Converter as colunas 'Latitude' e 'Longitude' em números (float)
state_counts["Latitude"] = state_counts["Latitude"].astype(float)
state_counts["Longitude"] = state_counts["Longitude"].astype(float)

# Criar a coluna "Supercharger_Count" com valor inicial 1
state_counts["Supercharger_Count"] = 1

# ================================
# Template
app.layout = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [controllers],
                    md=3,
                    style={
                        "padding-right": "25px",
                        "padding-left": "25px",
                        "padding-top": "50px",
                    },
                ),
                dbc.Col([map], md=9),
            ]
        )
    ],
    fluid=True,
)


# Callbacks
@app.callback([Output("map-graph", "figure")], [Input("dropdown-color", "value")])
def update_map(color_map):
    # Configuração do mapa
    px.set_mapbox_access_token(open("keys/mapbox_token").read())
    map_fig = px.scatter_mapbox(
        state_counts,
        lat="Latitude",
        lon="Longitude",
        hover_name="Supercharger_Count",
        color="Supercharger_Count",
        size_max=15,
        zoom=3,
        opacity=0.4,
        color_continuous_scale="blues",
        color_continuous_midpoint=state_counts["Supercharger_Count"].mean(),
    )

    map_fig.update_layout(
        mapbox=dict(
            center=go.layout.mapbox.Center(
                lat=39.8283,  # Latitude padrão
                lon=-98.5795,  # Longitude padrão
            ),
        ),
        template="plotly_dark",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        margin=go.layout.Margin(l=10, r=10, t=10, b=10),
    )

    return [map_fig]


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050")

from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

controllers = dbc.Row(
    [
        dcc.Store(id="store-global"),
        html.Img(
            id="logo", src=app.get_asset_url("logo_dark.png"), style={"width": "50%"}
        ),
        html.H2(
            "CARREGADORES SUPERCHARGER TESLA",
            style={"margin-top": "50px", "margin-left": "20px"},
        ),
        html.Img(
            id="logo2", src=app.get_asset_url("load.jpg"), style={"width": "100%"}
        ),
        html.P(
            """Através deste dashboard, é possível obter uma visão abrangente dos pontos de carregamento Tesla disponíveis. Isso é particularmente valioso para proprietários de veículos elétricos que desejam planejar suas viagens com facilidade, garantindo que haja carregadores acessíveis ao longo do caminho."""
        ),
        html.P("Variáveis de Análise", style={"margin-top": "20px"}),
        dcc.Dropdown(
            options=[
                {"label": "Ponto de recarga por cidade", "value": "City"},
            ],
            value="City",  # Valor padrão
            id="dropdown-color",
        ),
    ]
)

import dash_bootstrap_components as dbc
from dash import Dash

from dash_weather_app.server import app_flask


app_dash = Dash(__name__,
                server=app_flask,
                url_base_pathname='/dash/',
                external_stylesheets=[dbc.themes.BOOTSTRAP])

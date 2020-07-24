import dash_bootstrap_components as dbc
import dash_html_components as html

from dash_weather_app.layouts import navbar


error_layout = html.Div([
    navbar,
    dbc.Container(
        dbc.Alert("[404] Page not found!", color="danger"),
        style={'padding': 10}
    )
])
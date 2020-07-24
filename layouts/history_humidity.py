import datetime

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash_weather_app.layouts import navbar
from dash_weather_app.tools.plots import make_humi_plot


def days_diff_label(days_diff):
    return (datetime.datetime.now() - datetime.timedelta(days_diff)).strftime('%d/%m/%y')


def make_slider(days_range):
    days = range(days_range)

    slider = dbc.Container(
        dcc.Slider(
            id='hist-humi-slider',
            min=days[0],
            max=days[-1],
            value=days[-1],
            marks=dict(zip(days, [days_diff_label(x) for x in reversed(days)])),
            step=None
        )
    )

    return slider


body = dbc.Container([
    html.Br(),
    html.H1('Humidity history'),
    dcc.Graph(id='hist-humi-graph', figure=make_humi_plot(0)),
    dbc.Container(make_slider(5)),
])


hist_humi_layout = html.Div([
    navbar,
    body,
])

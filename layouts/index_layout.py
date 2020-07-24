import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from dash_weather_app.layouts import navbar


header = dbc.Row([
    dbc.Col([
        html.H1('Krakow', id='index-city-name'),
        html.H6('PL, (xxx N, yyy E)', id='index-city-details'),
    ]),
    dbc.Col([
        html.H6("Date", id='index-date', style={'text-align': 'right'}),
    ]),
], id='index-header')

body = html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H1('---', id='index-temperature', style={'font-size': '800%', 'text-align': 'right'})
        ], width=2),
        dbc.Col([
            html.Br(),
            html.H1('°C'),
            html.H6('Max: --- °C', id='index-temperature-max'),
            html.H6('Min: --- °C', id='index-temperature-min'),
        ], width=2, style={'text-align': 'left', 'padding-left': 10}),

        dbc.Col([
            html.Br(),
            html.Img(src='---',
                     height=125,
                     id='index-weather-icon'),
            html.Br(),
        ], width=4, style={'text-align': 'center'}),

        dbc.Col([
            html.Br(),
            html.Div([
                html.P('Pressure', style={'margin-bottom': 0}),
                html.H4('--- hPa', id='index-pressure', style={'margin-top': 0})
            ]),
            html.Div([
                html.P('Humidity', style={'margin-bottom': 0}),
                html.H4('--- %', id='index-humidity', style={'margin-top': 0})
            ]),
        ], width=4, style={'text-align': 'center'}),
    ], no_gutters=True),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(),
        dbc.Col([
            html.H6('---', id='index-forecast-day-name-day1'),
            html.Img(src='---', height=50, id='index-forecast-weather-day1'),
            html.H3('---', id='index-forecast-temp-day1'),
        ], style={'text-align': 'center'}),
        dbc.Col([
            html.H6('---', id='index-forecast-day-name-day2'),
            html.Img(src='---', height=50, id='index-forecast-weather-day2'),
            html.H3('---', id='index-forecast-temp-day2'),
        ], style={'text-align': 'center'}),
        dbc.Col([
            html.H6('---', id='index-forecast-day-name-day3'),
            html.Img(src='---', height=50, id='index-forecast-weather-day3'),
            html.H3('---', id='index-forecast-temp-day3'),
        ], style={'text-align': 'center'}),
        dbc.Col([
            html.H6('---', id='index-forecast-day-name-day4'),
            html.Img(src='---', height=50, id='index-forecast-weather-day4'),
            html.H3('---', id='index-forecast-temp-day4'),
        ], style={'text-align': 'center'}),
        dbc.Col([
            html.H6('---', id='index-forecast-day-name-day5'),
            html.Img(src='---', height=50, id='index-forecast-weather-day5'),
            html.H3('---', id='index-forecast-temp-day5'),
        ], style={'text-align': 'center'}),
        dbc.Col(),
    ]),
])


index_layout = html.Div([
    navbar,
    dbc.Container(header, id='index-header',),
    dbc.Container(body, id='index-body'),

    dcc.Interval(id='index-timer', interval=15 * 1000),
])

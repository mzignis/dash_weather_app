import datetime

import plotly.graph_objects as go
import requests
import pandas as pd


def make_temp_plot(days_diff):
    key = '2c2ce475d4e2a8ade19b434b2045ab19'
    start = int((datetime.datetime.now() - datetime.timedelta(days=days_diff)).timestamp())
    url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=50.08&lon=19.92&dt={start}&appid={key}'
    response = requests.get(url)

    data = response.json()['hourly']
    df = pd.DataFrame({'dt': [datetime.datetime.fromtimestamp(x['dt']).strftime('%H:%M') for x in data],
                       'values': [x['temp'] - 273.15 for x in data]})
    df = df.sort_values(by='dt').reset_index(drop=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['dt'], y=df['values'], line={'shape': 'spline'}))
    fig.update_xaxes(title_text='Hours', ticktext=df['dt'][1::2], tickvals=df['dt'][1::2])
    fig.update_yaxes(title_text='Temperature [°C]')
    fig.update_layout(transition_duration=1500)

    return fig


def make_pres_plot(days_diff):
    key = '2c2ce475d4e2a8ade19b434b2045ab19'
    start = int((datetime.datetime.now() - datetime.timedelta(days=days_diff)).timestamp())
    url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=50.08&lon=19.92&dt={start}&appid={key}'
    response = requests.get(url)

    data = response.json()['hourly']
    df = pd.DataFrame({'dt': [datetime.datetime.fromtimestamp(x['dt']).strftime('%H:%M') for x in data],
                       'values': [x['pressure'] for x in data]})
    df = df.sort_values(by='dt').reset_index(drop=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['dt'], y=df['values'], line={'shape': 'spline'}))
    fig.update_xaxes(title_text='Hours', ticktext=df['dt'][1::2], tickvals=df['dt'][1::2])
    fig.update_yaxes(title_text='Pressure [hPa]')
    fig.update_layout(transition_duration=1500)

    return fig


def make_humi_plot(days_diff):
    key = '2c2ce475d4e2a8ade19b434b2045ab19'
    start = int((datetime.datetime.now() - datetime.timedelta(days=days_diff)).timestamp())
    url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=50.08&lon=19.92&dt={start}&appid={key}'
    response = requests.get(url)

    data = response.json()['hourly']
    df = pd.DataFrame({'dt': [datetime.datetime.fromtimestamp(x['dt']).strftime('%H:%M') for x in data],
                       'values': [x['humidity'] for x in data]})
    df = df.sort_values(by='dt').reset_index(drop=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['dt'], y=df['values'], line={'shape': 'spline'}))
    fig.update_xaxes(title_text='Hours', ticktext=df['dt'][1::2], tickvals=df['dt'][1::2])
    fig.update_yaxes(title_text='Humidity [%]')
    fig.update_layout(transition_duration=1500)

    return fig

import datetime

from dash.dependencies import Input, Output
import requests
import pprint

from dash_weather_app.app import app_dash
from dash_weather_app.tools.constants import weather_icons
from dash_weather_app.tools.plots import make_temp_plot, make_pres_plot, make_humi_plot
from dash_weather_app.tools.data_processing import get_forecast


@app_dash.callback([Output("index-date", "children"),
                    Output('index-city-details', 'children')],
                   [Input("index-timer", "n_intervals")])
def update_date_and_time(*args):
    key = '2c2ce475d4e2a8ade19b434b2045ab19'
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Krakow&appid={key}'
    data = requests.get(url).json()
    country = data['sys']['country']
    lat = f"{abs(data['coord']['lat']):.2f} {'N' if data['coord']['lat'] else 'S'}"
    lon = f"{abs(data['coord']['lon']):.2f} {'E' if data['coord']['lon'] else 'W'}"
    city_details = f'{country}, ({lat}, {lon})'
    date = datetime.datetime.now().strftime('%A %d/%m/%Y')
    return date, city_details


@app_dash.callback([Output("index-temperature", "children"),
                    Output("index-temperature-max", "children"),
                    Output("index-temperature-min", "children"),
                    Output("index-weather-icon", "src"),
                    Output("index-pressure", "children"),
                    Output("index-humidity", "children")],
                   [Input("index-timer", "n_intervals")])
def update_temperature_pressure_humidity(*args):
    key = '2c2ce475d4e2a8ade19b434b2045ab19'
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Krakow&appid={key}'
    data = requests.get(url).json()

    temp = f'{int(data["main"]["temp"] - 273)}'
    temp_max = f'Max: {int(data["main"]["temp_max"] - 273)} °C'
    temp_min = f'Min: {int(data["main"]["temp_min"] - 273)} °C'
    weather_icon = weather_icons[data['weather'][0]['description']]
    pressure = f'{data["main"]["pressure"]} hPa'
    humidity = f'{data["main"]["humidity"]} %'

    return temp, temp_max, temp_min, weather_icon, pressure, humidity


@app_dash.callback(
    Output('hist-temp-graph', 'figure'), [Input('hist-temp-slider', 'value')])
def update_temp_figure(selected_day):
    return make_temp_plot(4-selected_day)


@app_dash.callback(
    Output('hist-pres-graph', 'figure'), [Input('hist-pres-slider', 'value')])
def update_temp_figure(selected_day):
    return make_pres_plot(4 - selected_day)


@app_dash.callback(
    Output('hist-humi-graph', 'figure'), [Input('hist-humi-slider', 'value')])
def update_temp_figure(selected_day):
    return make_humi_plot(4 - selected_day)


@app_dash.callback([Output('index-forecast-day-name-day1', 'children'),
                    Output("index-forecast-weather-day1", "src"),
                    Output("index-forecast-temp-day1", "children"),
                    Output('index-forecast-day-name-day2', 'children'),
                    Output("index-forecast-weather-day2", "src"),
                    Output("index-forecast-temp-day2", "children"),
                    Output('index-forecast-day-name-day3', 'children'),
                    Output("index-forecast-weather-day3", "src"),
                    Output("index-forecast-temp-day3", "children"),
                    Output('index-forecast-day-name-day4', 'children'),
                    Output("index-forecast-weather-day4", "src"),
                    Output("index-forecast-temp-day4", "children"),
                    Output('index-forecast-day-name-day5', 'children'),
                    Output("index-forecast-weather-day5", "src"),
                    Output("index-forecast-temp-day5", "children")],
                   [Input("index-timer", "n_intervals")])
def update_forecast(*args):
    city = 'Krakow'
    days = [(datetime.datetime.now() + datetime.timedelta(days=x+1)).strftime('%Y-%m-%d') for x in range(5)]
    forecasts = []
    for day in days:
        weather, temp = get_forecast(day, city)
        weekday_name = datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%A')
        forecasts.extend([weekday_name, weather_icons[weather], temp])
    pprint.pprint(forecasts)

    return forecasts

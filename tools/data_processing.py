from collections import Counter

import numpy as np
import requests

KEY = '2c2ce475d4e2a8ade19b434b2045ab19'


def get_forecast(date, city):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={KEY}'
    response = requests.get(url)
    data = response.json()

    day_forecast = [data['list'][x] for x in range(len(data['list'])) if date in data['list'][x]['dt_txt']]
    temp = np.mean([day_forecast[x]['main']['temp'] for x in range(len(day_forecast))]) - 273.15
    weather_descriptions = [day_forecast[x]['weather'][0]['description'] for x in range(len(day_forecast))]
    weather = Counter(weather_descriptions).most_common(1)[0][0]

    return weather, f'{int(temp)} °C'

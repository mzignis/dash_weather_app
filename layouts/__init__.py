from dash_weather_app.layouts import index_layout
from dash_weather_app.layouts import error_layout
from dash_weather_app.layouts.history_temperature import hist_temp_layout
from dash_weather_app.layouts.history_pressure import hist_pres_layout
from dash_weather_app.layouts import hist_humi_layout


layouts = {
    'index': index_layout,
    'hist_temp': hist_temp_layout,
    'hist_pres': hist_pres_layout,
    'hist_humi': hist_humi_layout,
    '404': error_layout
}
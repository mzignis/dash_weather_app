import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from dash_weather_app.app import app_dash
from dash_weather_app.layouts import layouts
from dash_weather_app.server import app_flask

app_dash.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app_dash.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dash/':
        return layouts['index']
    elif pathname == '/dash/hist/temp':
        return layouts['hist_temp']
    elif pathname == '/dash/hist/pres':
        return layouts['hist_pres']
    elif pathname == '/dash/hist/humi':
        return layouts['hist_humi']
    else:
        return layouts['404']


if __name__ == '__main__':
    app_flask.run(debug=True)

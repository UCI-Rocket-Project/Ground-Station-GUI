import datetime

import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly
from components import gauges
import random
import dash_daq as daq
import time
import sys

app = dash.Dash(__name__)


def serve_layout():
    return html.Div([     
        dcc.Interval(
            id='interval-component',
            interval=1000,  # in milliseconds
            n_intervals=0
        ),
        html.Div(children=[
            html.Div(html.H2('TC Sensors'),),
            html.Div(buildGauges(), id='guageChildren')], className="tc-gauges"),
    ])
    
def buildGauges():
    return html.Div(children=[daq.Gauge(
        showCurrentValue=True,
        color={"gradient": True,
               "ranges": {"green": [0, 200], "blue": [200, 500], "yellow": [500, 800], "red": [800, 1000]}},
        label='COPV TC',
        labelPosition='top',
        id='download-gauge',
        max=1000,
        size=300,
        units='unit',
        style={'display': 'block'},
        value=random.randint(1, 999)
    ),
        daq.Gauge(
        showCurrentValue=True,
        color={"gradient": True,
               "ranges": {"green": [0, 200], "blue": [200, 500], "yellow": [500, 800], "red": [800, 1000]}},
        label='COPV TC II',
        labelPosition='top',
        id='download-gauge1',
        max=1000,
        size=300,
        units='unit',
        style={'display': 'block'},
        value=random.randint(1, 999)
    ),
        daq.Gauge(
        showCurrentValue=True,
        color={"gradient": True,
               "ranges": {"green": [0, 200], "blue": [200, 500], "yellow": [500, 800], "red": [800, 1000]}},
        label='LOX TC',
        labelPosition='top',
        id='download-gauge2',
        max=1000,
        size=300,
        units='unit',
        style={'display': 'block'},
        value=random.randint(1, 999)
    ),
        daq.Gauge(
        showCurrentValue=True,
        color={"gradient": True,
               "ranges": {"green": [0, 200], "blue": [200, 500], "yellow": [500, 800], "red": [800, 1000]}},
        label='LNG TC',
        labelPosition='top',
        id='download-gauge3',
        max=1000,
        size=300,
        units='unit',
        style={'display': 'block'},
        value=random.randint(1, 999)
    ),
    ], className="gauges")

app.layout = serve_layout

@app.callback(Output('guageChildren', 'children'),
              Input('interval-component', 'n_intervals'))
def update_metrics(n):
    return buildGauges()

def update_output(value):
    return value


if __name__ == '__main__':
    app.run(debug=True)
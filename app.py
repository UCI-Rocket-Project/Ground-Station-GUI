# Import packages
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from dash import html
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import dash_daq as daq
from components import gauges
from collections import OrderedDict
import plotly.io as pio
import plotly.express as px

# Incorporate data

df = pd.DataFrame(dict(
    solenoid = ["he", "lox", "lng", "pv1", "pv2", "mvas"],
    value = [1, 100, 1, 100, 1, 100]))

df3 = pd.DataFrame(dict(
    curr_sensor = ["curr1", "curr2", "curr3", "curr4", "curr5", "curr6"],
    value = [60, 100, 50, 100, 90, 1]))

solenoids = OrderedDict(
    [
        ("he", ["open"],),
        ("lox", ["closed"],),
        ("lng", ["open"],),
        ("pv1", ["closed"],),
        ("pv2", ["open"],),
        ("mvas", ["closed"],),
    ]
)

df2 = pd.DataFrame(solenoids)

fig = px.bar(df, x = 'solenoid', y = 'value',
             color = 'solenoid', height=300, width= 400)

image_path = 'assets/download.png'

fig2 = px.bar(df3, x = 'curr_sensor', y = 'value',
             color = 'curr_sensor', height=300, width= 400,)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

pio.templates.default = "plotly_dark"


# Initialize the app - incorporate a Dash Mantine theme
# external_stylesheets = [dmc.theme.DEFAULT_COLORS]
# app = Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = html.Div([
    # header
    html.Div(children=[
        html.Img(src=image_path),
        html.Div(
            html.H1('UCI Rocket Project Dashboard'),
        className='titlePage'),
    ], className="headerClass"),
    
    # solenoid + current titles
    html.Div(children=[
    # solenoid title
    html.Div(
        html.H2('Solenoids Status'),
    ),
    
    # current sensors title
    html.Div(
        html.H2('Current Sensors'),
    ),
    ], className="sol-curr-titles"),
    
    # first solenoid graph
    html.Div(children=[
    html.Div(children=[
    # html.Div(
    #     dcc.Graph(id='solenoid-chart', figure=fig),
    # ),
    html.Div(children=[
        dbc.Alert("Solenoid he is currently open!", color="success"),
        dbc.Alert("Solenoid lox is about to open.", color="warning"),
        dbc.Alert("Solenoid lng closing...", color="danger"),
    ], id="alerts"),
    
    html.Div(
        dash_table.DataTable(
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
                'lineHeight': '20px',
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white',
            },
            style_header={
                'backgroundColor': 'rgb(30, 30, 30)',
                'color': 'white'
            },
            style_cell={'textAlign': 'center', 'font_family': 'sans-serif',},
            style_data_conditional=[
                {
                'if': {'column_id': 'pv2'},
                'color': 'rgb(0,128,0)',
                },
                {
                'if': {'column_id': 'he'},
                'color': 'rgb(0,128,0)',
                },
                {
                'if': {'column_id': 'lng'},
                'color': 'rgb(0,128,0)',
                },  
                {
                'if': {'column_id': 'lox'},
                'color': 'rgb(255, 0, 0) ',
                }, 
                {
                'if': {'column_id': 'pv1'},
                'color': 'rgb(255, 0, 0) ',
                }, 
                {
                'if': {'column_id': 'mvas'},
                'color': 'rgb(255, 0, 0)',
                }, 
            ],
            data=df2.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df2.columns],
            id="solenoid-on",
    )),
    ], id="solenoid-div"),
  
    html.Div(
        dcc.Graph(id='sensor-chart', figure=fig2),
    )], id="top-row"),
    
    html.Div(children=[
    dcc.ConfirmDialogProvider(
        children=html.Button('Click Me!',),
        id='danger-danger-provider',
        message='Are you sure you wanted to press this button?'
    ),
    html.Div(id='output-provider'),
    ], id="some-button"),
    
    #PT + TC Title
    html.Div(children=[
    html.Div(
        html.H2('TCs Status'),
    ),
    html.Div(
        html.H2('PTs Status'),
    ),
    ], className="gauge-titles"),
    
    
    
    html.Div(children=[
    # first gauge
    html.Div(children=[
        gauges.gauge1,
        gauges.gauge2,
        gauges.gauge3,
        gauges.gauge4,
    ], className="gauges"),
    
    html.Div(children=[
        gauges.gauge5,
        gauges.gauge6,
        gauges.gauge7,
        gauges.gauge8,
    ], className="gauges"),
    ], className="all gauges"),
])

@callback(
    Output('output-provider', 'children'),
    # Output('solenoid-id', 'data'),
    Input('danger-danger-provider', 'submit_n_clicks'))

def update_output(submit_n_clicks):
    if not submit_n_clicks:
        return ''
    
    
    return """
        Pressed {} times
    """.format(submit_n_clicks)

# def graphs(submit_n_clicks):
#     if not submit_n_clicks:
#         return ''
    
#     solenoids = OrderedDict(
#     [
#         ("he", ["open"],),
#         ("lox", ["closed"],),
#         ("lng", ["open"],),
#         ("pv1", ["closed"],),
#         ("pv2", ["open"],),
#         ("mvas", ["closed"],),
#     ]
#     )
    
#     df2 = pd.DataFrame(solenoids)
    
#     return df2


fig.update_layout(title_text='solenoid on/off', title_x=0.5,)
fig.update_layout(template='plotly_dark')

fig2.update_layout(title_text='current sensors status', title_x=0.5,)
fig2.update_layout(template='plotly_dark')


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
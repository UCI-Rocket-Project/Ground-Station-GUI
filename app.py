# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import dash_daq as daq
from components import gauges

# Incorporate data
df = pd.DataFrame(dict(
    solenoid = ["he", "lox", "lng", "pv1", "pv2", "mvas"],
    value = [1, 100, 1, 100, 1, 100]))

fig = px.bar(df, x = 'solenoid', y = 'value',
             color = 'solenoid', height=300, width= 400)

image_path = 'assets/download.png'


# Initialize the app - incorporate a Dash Mantine theme
# external_stylesheets = [dmc.theme.DEFAULT_COLORS]
# app = Dash(__name__, external_stylesheets=external_stylesheets)
app = Dash(__name__)

# App layout
app.layout = html.Div([
    # header
    html.Img(src=image_path),
    
    html.Div(
        html.H1('UCI Rocket Project Dashboard'),
    ),
    
    # solenoid header
    html.Div(
        html.H2('Solenoids Status'),
    ),
    
    # first solenoid graph
    html.Div(
        dcc.Graph(id='solenoid-chart', figure=fig),
    ),
    
    # TC title
    html.Div(
        html.H2('TC Sensors'),
    ),
    
    # first gauge
    html.Div(children=[
        gauges.gauge1,
        gauges.gauge2,
        gauges.gauge3,
        gauges.gauge4,
    ], className="gauges"),
    
    # PT title
    html.Div(
        html.H2('PT Sensors'),
    ),
    
    html.Div(children=[
        gauges.gauge5,
        gauges.gauge6,
        gauges.gauge7,
        gauges.gauge8,
    ], className="gauges"),

])

fig.update_layout(title_text='solenoid open/close', title_x=0.5,)


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
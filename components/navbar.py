from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
import dash_daq as daq

# component
gauge1 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='TC1',
        max=4000,
        min=0,
        id="some-gauge")

gauge2 = daq.Gauge(
        showCurrentValue=True,
        units="unit",
        value=400,
        label='TC1',
        max=4000,
        min=0,
        id="some-gauge2")

navbar = dmc.Navbar(
    p="md",                  #providing medium padding all side
    fixed=False,             #Setting fixed to false
    width={"base": 300},     #Initial size of navbar ie. 300px
    hidden=True,             #we want to hide for smaller screen
    hiddenBreakpoint='md',   #after past medium size navbar will be hidden.
    height='100vh',          #providing height of navbar
    id='sidebar',
    children=[
      html.Div([
              dmc.NavLink(
                  label="Home",
                  icon=DashIconify(icon="bi:house-door-fill", height=16, color="#c2c7d0")
              ),
              dmc.NavLink(
                  opened=False,
                  label="Solenoids",
                  icon=DashIconify(icon="tabler:gauge", height=16, color="#c2c7d0"),
              ),
              dmc.NavLink(
                  label="PTs/TCs",
                icon=DashIconify(icon="tabler:gauge", height=16, color="#c2c7d0"),
              ),
              dmc.NavLink(
                  label="Current Sensors",
                  icon=DashIconify(icon="tabler:activity", height=16, color="#c2c7d0"),
                  variant="subtle",
                  active=True,
              ),
          ])
    ]
)

btn1 =  dmc.Button(
            children=[DashIconify(icon="ci:hamburger-lg", width=24, height=24,color="#c2c7d0")],
            variant="subtle", 
            p=1,
            id='sidebar-button'
        )

# @callback (
#     Output("sidebar", "width"),          #what we wanted to change
#     Input("sidebar-button", "n_clicks"), #width will change when btn is triggered
#     State('sidebar','width'),            #store inital width
#     prevent_initial_call=True,
#     )

# def sidebar(opened, width):
#     if opened:
#         if width['base'] == 300:         #if initial width is 300 then return 70
#             return {"base": 70}
#         else:
#             return {'base':300}
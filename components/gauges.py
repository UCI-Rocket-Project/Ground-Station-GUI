from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import dash_daq as daq

# tc gauges
gauge1 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='COPV TC',
        max=4000,
        min=0,
        id="some-gauge",
        size=150)

gauge2 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='COPV TC II',
        max=4000,
        min=0,
        id="some-gauge2",
        size=150)

gauge3 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='LOX TC',
        max=4000,
        min=0,
        id="some-gauge3",
        size=150)

gauge4 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=800,
        label='LNG TC',
        max=4000,
        min=0,
        id="some-gauge4",
        size=150)

# pt gauges
gauge5 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=4000,
        label='COPV PT',
        max=4000,
        min=0,
        id="some-gauge5",
        size=150)

gauge6 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='LNG PT',
        max=4000,
        min=0,
        id="some-gauge6",
        size=150)

gauge7 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='LOX PT',
        max=4000,
        min=0,
        id="some-gauge7",
        size=150)

gauge8 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='GSE PT',
        max=4000,
        min=0,
        id="some-gauge8",
        size=150)
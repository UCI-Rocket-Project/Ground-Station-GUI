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
        label='TC1',
        max=4000,
        min=0,
        id="some-gauge")

gauge2 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='TC2',
        max=4000,
        min=0,
        id="some-gauge2")

gauge3 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='TC3',
        max=4000,
        min=0,
        id="some-gauge3")

gauge4 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=800,
        label='TC4',
        max=4000,
        min=0,
        id="some-gauge4")

# pt gauges
gauge5 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=4000,
        label='PT1',
        max=4000,
        min=0,
        id="some-gauge5")

gauge6 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='PT2',
        max=4000,
        min=0,
        id="some-gauge6")

gauge7 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='PT3',
        max=4000,
        min=0,
        id="some-gauge7")

gauge8 = daq.Gauge(
        showCurrentValue=True,
        color={"gradient":True,"ranges":{"green":[0,1500],"yellow":[1500,3000],"red":[3000, 4000]}},
        units="unit",
        value=400,
        label='PT4',
        max=4000,
        min=0,
        id="some-gauge8")
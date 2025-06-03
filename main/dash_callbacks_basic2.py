# -*- coding: utf-8 -*-
"""
Section4_dash_callbacks_Basic2
"""

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

import numpy as np
import plotly.graph_objects as go

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Label("Input Random Number"),
        html.Br(),
        html.Div(
            id="Input Div", children=[dcc.Input(id="Input RandomNumber", value=5)]
        ),
        html.Br(),
        html.Br(),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output(component_id="graph", component_property="figure"),
    [Input(component_id="Input RandomNumber", component_property="value")],
)
def random_fig(N):
    N = int(N)
    random_x = np.random.randint(0, 500, N)
    random_y = np.random.randint(0, 1500, N)

    trace = go.Scatter(x=random_x, y=random_y, mode="markers", name="Random Number")
    layout = go.Layout(title="Random Number Graph N:{}".format(N))

    fig = go.Figure(data=trace, layout=layout)

    return fig


if __name__ == "__main__":
    app.run()

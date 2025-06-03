# -*- coding: utf-8 -*-
"""
Section4_dash_callbacks_basic3
"""
# %%

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

import numpy as np
import plotly.graph_objects as go

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Label("Input Number"),
        html.Br(),
        dcc.Input(id="input randomNumber", value=5),
        html.Br(),
        html.Br(),
        dcc.Graph(id="graph"),
        html.Br(),
        html.Br(),
        html.H3("Random X Avg"),
        html.Div(id="random x avg", children=["None"]),
    ]
)


@app.callback(
    Output(component_id="graph", component_property="figure"),
    [Input(component_id="input randomNumber", component_property="value")],
)
def radnom_fig(N):
    N = int(N)
    random_x = np.random.randint(0, 1000, N)
    random_y = np.random.randint(0, 1500, N)

    trace1 = go.Scatter(
        x=random_x,
        y=random_y,
        mode="markers",
        marker={"size": 10},
        name="Random Number {}".format(N),
    )

    random_x_avg = [np.sum(random_x) / N]
    random_y_avg = [np.sum(random_y) / N]

    trace2 = go.Scatter(
        x=random_x_avg,
        y=random_y_avg,
        mode="markers",
        marker={"size": 15, "color": "red"},
        name="Random Avg X: {} & Y: {}".format(random_x_avg, random_y_avg),
    )

    data = [trace1, trace2]

    layout = go.Layout(title="Random Number {}".format(N))

    fig = go.Figure(data=data, layout=layout)

    return fig


@app.callback(
    Output(component_id="random x avg", component_property="children"),
    [Input(component_id="input randomNumber", component_property="value")],
)
def random_x_avg(N):
    N = int(N)
    random_x = np.random.randint(0, 1000, N)
    random_x_avg = np.sum(random_x) / N
    return random_x_avg


if __name__ == "__main__":
    app.run(debug=True, port=8050)

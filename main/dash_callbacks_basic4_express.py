# -*- coding: utf-8 -*-
"""
Section4_dash_callbacks_basic4_express.py
"""
# %%

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

import numpy as np
import plotly.graph_objects as go
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.H4("Interactive scatter plot with Iris DataSet"),
        html.Br(),
        dcc.Graph(id="graph"),
        html.Br(),
        html.P("Filter by petal width:"),
        dcc.RangeSlider(
            id="range-slider",
            min=0,
            max=2.5,
            step=0.1,
            marks={0: "0", 2.5: "2.5"},
            value=[0.5, 2],
        ),
    ]
)


@app.callback(
    Output(component_id="graph", component_property="figure"),
    [Input(component_id="range-slider", component_property="value")],
)
def update_graph(slider_range):

    df = px.data.iris()
    low, high = slider_range
    condition = (df["petal_width"] > low) & (df["petal_width"] < high)

    fig = px.scatter(
        df[condition],
        x="sepal_width",
        y="sepal_length",
        color="species",
        size="petal_length",
    )
    return fig


if __name__ == "__main__":
    app.run()

# %% 변수 확인하는 방법 예제


# from dash import Dash, html, dcc, Input, Output
# import dash_bootstrap_components as dbc

# from dash.dependencies import Input, Output

# # import plotly.express as px

# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app.layout = html.Div(
#     [
#         html.Br(),
#         html.Br(),
#         html.H4("Interactive scatter plot with Iris DataSet"),
#         html.Br(),
#         dcc.Graph(id="graph"),
#         html.Br(),
#         html.P("Filter by petal width:"),
#         dcc.RangeSlider(
#             id="range-slider",
#             min=0,
#             max=2.5,
#             step=0.1,
#             marks={0: "0", 2.5: "2.5"},
#             value=[0.5, 2],
#         ),
#         html.Br(),
#         html.Div(id="check div", children=["None"]),
#     ]
# )


# @app.callback(
#     Output(component_id="check div", component_property="children"),
#     [Input(component_id="range-slider", component_property="value")],
# )
# def update_graph(slider_range):

#     df = px.data.iris()
#     low, high = slider_range

#     return low


# if __name__ == "__main__":
#     app.run()

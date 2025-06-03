# -*- coding: utf-8 -*-
"""
Section4_dash_callbacks_MultipleInputs_basic1
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
        html.H4("Input Number"),
        dcc.Input(id="input word1", value="word1"),
        dcc.Input(id="input word2", value="word2"),
        html.Br(),
        html.Div(id="Div2", children=["None"]),
        # dcc.Input(id="input 3", value=""),
        html.Br(),
    ]
)


@app.callback(
    Output(component_id="Div2", component_property="children"),
    [
        Input(component_id="input word1", component_property="value"),
        Input(component_id="input word2", component_property="value"),
    ],
)
def update_div(input_value1, input_value2):
    print("callback update_div {} {}".format(input_value1, input_value2))
    result_word = "{} + {} = {} 입니다".format(
        input_value1, input_value2, input_value1 + input_value2
    )
    return result_word


if __name__ == "__main__":
    app.run()

# %%

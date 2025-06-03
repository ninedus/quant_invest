# -*- coding: utf-8 -*-
"""
Section4 _ dash_callbacks_MultipleOutputs_basic 1
"""
# %%

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.H4("Input Number"),
        dcc.Input(id="input value", value="숫자를 입력하세요."),
        html.Br(),
        html.Br(),
        html.H4("Div1"),
        html.Div(id="Div1", children=["None"]),
        html.Br(),
        html.Br(),
        html.H4("Div2"),
        html.Div(id="Div2", children=["None"]),
    ]
)


@app.callback(
    [
        Output(component_id="Div1", component_property="children"),
        Output(component_id="Div2", component_property="children"),
    ],
    [Input(component_id="input value", component_property="value")],
)
def update_div(input_value):

    input_value = int(input_value)

    result_div1 = input_value + 100
    result_div2 = input_value - 100

    format_div1 = "{} + 100 = {} 입니다".format(input_value, result_div1)
    format_div2 = "{} - 100 = {} 입니다".format(input_value, result_div2)

    return format_div1, format_div2


if __name__ == "__main__":
    app.run()

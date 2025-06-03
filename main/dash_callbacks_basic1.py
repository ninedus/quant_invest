# -*- coding: utf-8 -*-
"""
Section4_Dash_callbacks_basic1
"""
#%%

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    
    #Input
    html.Br(),
    html.Br(),
    html.Label('Input Layout'),
    html.Br(),
    dcc.Input(id = 'input',
              value = '종목이름을 입력해주세요',
              type = 'text'),
    
    html.Br(),
    html.Br(),
    html.Label('Output Layout'),
    html.Div(id = 'div',
             children = ['아직 아무것도 입력되지 않았습니다.'])
    
    ])
@app.callback(
    Output(component_id = 'div',
           component_property = 'children'),
    [Input(component_id = 'input',
           component_property = 'value')]
    )
def update_layout_value(input_value):
    return "종목: {}".format(input_value)

if __name__=='__main__':
    app.run()
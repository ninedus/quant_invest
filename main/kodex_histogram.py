import numpy as np
import plotly.graph_objects as go
import pandas as pd
from dash import html
from dash import dcc

df = pd.read_excel("data/df_etf.xlsx", index_col=0)
df_copy = df.copy()

# ARIRANG BOND FUTURE 10Y
condition_kodex = [
    df_copy.columns[i]
    for i in range(len(df_copy.columns))
    if df_copy.columns[i].startswith("KODEX")
]

df_copy_kodex = df_copy.loc[:, condition_kodex]

kind = "KODEX 200"
df_copy_kodex_sample = df_copy_kodex.loc[:, [kind]]

# 가격 histogram
trace1 = go.Histogram(
    x=df_copy_kodex_sample[kind],
    name=kind,
    xbins=dict(
        start=df_copy_kodex_sample[kind].min(),
        end=df_copy_kodex_sample[kind].max(),
        size=100,
    ),
)


# 수익률 histogram
df_copy_kodex_sample_return = df_copy_kodex_sample.pct_change(periods=1).dropna()
df_copy_kodex_sample_return = np.round(df_copy_kodex_sample_return * 100, 1)

trace2 = go.Histogram(
    x=df_copy_kodex_sample_return[kind],
    name=kind,
    xbins=dict(
        start=df_copy_kodex_sample_return[kind].min(),
        end=df_copy_kodex_sample_return[kind].max(),
        size=0.1,
    ),
)


layout = go.Layout(title="Histogram of {} Price".format(kind))
fig1 = go.Figure(data=[trace1], layout=layout)

layout = go.Layout(title="Histogram of {} Return".format(kind))
fig2 = go.Figure(data=[trace2], layout=layout)

layout_kodex_histogram = html.Div(
    [
        html.Div([html.H3(kind), dcc.Graph(figure=fig1)]),
        html.Div([dcc.Graph(figure=fig2)]),
    ]
)

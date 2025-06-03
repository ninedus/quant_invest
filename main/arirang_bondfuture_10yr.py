import numpy as np
import plotly.graph_objects as go
import pandas as pd
from dash import html
from dash import dcc

df = pd.read_excel("data/df_etf.xlsx", index_col=0)
df_copy = df.copy()

# ARIRANG BOND FUTURE 10Y
condition_arirang = [
    df_copy.columns[i]
    for i in range(len(df_copy.columns))
    if df_copy.columns[i].startswith("ARIRANG")
]

df_copy_arirang = df_copy.loc[:, condition_arirang]

kind = "ARIRANG 국채선물10년"
startDate = "2021-06-01"
endDate = "2022-03-31"

df_copy_arirang_sample = df_copy_arirang.loc[startDate:endDate, [kind]]


trace1 = go.Box(y=df_copy_arirang_sample[kind], name=kind, jitter=0.2, boxpoints="all")

data = [trace1]
layout = go.Layout(title="{} Box Plot, {} - {}".format(kind, startDate, endDate))
fig = go.Figure(data=data, layout=layout)

layout_arirang_bondfuture_10yr = html.Div(
    [
        html.H3(kind),
        dcc.Graph(figure=fig),
    ]
)

import numpy as np
import plotly.graph_objects as go
import pandas as pd
from dash import html
from dash import dcc

df = pd.read_excel("data/df_etf.xlsx", index_col=0)
df_copy = df.copy()

np.random.seed(42)
random_x = np.random.randint(1, 100, 5)
idx = ["A", "B", "C", "D", "E"]
df = pd.DataFrame(random_x)
df.index = idx
df.columns = ["Random variable"]

trace = go.Pie(
    labels=df.index, values=df["Random variable"], hole=0.2, pull=[0, 0, 0.2, 0, 0]
)
layout = go.Layout(title="Pie Chart Example")
fig = go.Figure(data=[trace], layout=layout)

layout_piechart = html.Div(
    [
        html.H3("Pie Chart"),
        dcc.Graph(figure=fig),
    ]
)

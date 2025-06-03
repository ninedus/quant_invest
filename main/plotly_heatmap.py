import numpy as np
import plotly.graph_objects as go
from dash import html
from dash import dcc
import pandas as pd

df = pd.read_excel("data/df_etf.xlsx", index_col=0)
df_copy = df.copy()

condition_kodex = [
    df_copy.columns[i]
    for i in range(len(df_copy.columns))
    if df_copy.columns[i].startswith("KODEX")
]

df_copy_kodex = df_copy.loc[:, condition_kodex]
df_copy_kodex["YEAR"] = df_copy_kodex.index.year
df_copy_kodex["MONTH"] = df_copy_kodex.index.month
YEAR = 2021
df_copy_kodex_2021 = df_copy_kodex[df_copy_kodex["YEAR"] == YEAR]

# 무시
pd.set_option("mode.chained_assignment", None)
df_copy_kodex_2021["MONTH(SHIFT)-1)"] = df_copy_kodex_2021["MONTH"].shift(-1)  # .copy()

df_copy_kodex_2021_cond = df_copy_kodex_2021[
    (df_copy_kodex_2021["MONTH"] - df_copy_kodex_2021["MONTH(SHIFT)-1)"]) != 0
]

df_copy_kodex_2021_cond_return = df_copy_kodex_2021_cond.pct_change(
    periods=1, fill_method=None
)  # .dropna()
df_copy_kodex_2021_cond_return = np.round(df_copy_kodex_2021_cond_return * 100, 2)

df_copy_kodex_2021_cond_return = df_copy_kodex_2021_cond_return.drop(
    ["YEAR", "MONTH", "MONTH(SHIFT)-1)"], axis=1
)

data = go.Heatmap(
    x=df_copy_kodex_2021_cond_return.columns,
    y=df_copy_kodex_2021_cond_return.index,
    z=df_copy_kodex_2021_cond_return.values,
    coloraxis="coloraxis",
    colorscale="Viridis",
    colorbar=dict(title="Return (%)"),
)
layout = go.Layout(title="KODEX 2021 Return (%)")
fig = go.Figure(data=[data], layout=layout)

layout_heatmap = html.Div(
    [
        html.H3("Heatmap"),
        dcc.Graph(figure=fig),
    ],
    style={
        "border": "green solid",
    },
)

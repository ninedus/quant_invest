import numpy as np
import plotly.graph_objects as go
import pandas as pd
from dash import html
from dash import dcc

style_colors = {"background": "#111111", "text": "#7fdbff"}

np.random.seed(42)

random_x1 = np.random.randint(0, 100, 100)
random_x2 = np.random.randint(50, 150, 100)

# print(random_x1)
# print(random_x2)


trace1 = go.Box(y=random_x1, name="Box 1")
trace2 = go.Box(y=random_x2, name="Box 2")

data = [trace1, trace2]
layout = go.Layout(
    title="Random variable",
    plot_bgcolor=style_colors["background"],
    paper_bgcolor=style_colors["background"],
    font_color=style_colors["text"],
)
fig = go.Figure(data=data, layout=layout)

# print(np.quantile(random_x1, [0.25, 0.5, 0.75]))
df = pd.read_excel("data/df_etf.xlsx", index_col=0)
df_copy = df.copy()
condition_kodex = [
    df_copy.columns[i]
    for i in range(len(df_copy.columns))
    if df_copy.columns[i].startswith("KODEX")
]
df_copy_kodex = df_copy.loc[:, condition_kodex]

bubble_layout = html.Div(
    [
        html.Div(
            style={"display": "flex", "flex-direction": "row", "padding": "10px"},
            children=[
                html.Div(
                    html.H3(
                        children="Bubble Plot",
                        style={
                            "textAlign": "center",
                            "color": style_colors["text"],
                        },
                    ),
                    style={"flex": "1", "padding": "10px"},
                ),
                html.Div(
                    id="dropdown-container",
                    children=[
                        dcc.Dropdown(
                            id="dropdown",
                            options=[
                                {"label": i, "value": i} for i in df_copy_kodex.columns
                            ],
                            # value="box1",
                            placeholder="Select a stock",
                            multi=True,
                        ),
                    ],
                    style={"flex": "1", "padding": "10px"},
                ),
            ],
        ),
        # html.H3(
        #     children="Bubble Plot",
        #     style={"textAlign": "center", "color": style_colors["text"]},
        # ),
        dcc.Graph(figure=fig),
    ]
)

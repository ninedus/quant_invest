import numpy as np
import plotly.graph_objects as go
from dash import html
from dash import dcc

random_matrix = np.random.randint(0, 100, (3, 3))

trace = go.Heatmap(z=random_matrix, colorscale="Viridis")
layout = go.Layout(title="Random Matrix Heatmap")
fig = go.Figure(data=[trace], layout=layout)

layout_heatmap = html.Div(
    [
        html.H3("Heatmap"),
        dcc.Graph(figure=fig),
    ]
)

from dash import html
import plotly.express as px
from dash import dcc

# Example scatter plot
fig = px.scatter(
    x=[1, 2, 3, 4, 5],
    y=[10, 11, 12, 13, 14],
    labels={"x": "X-axis", "y": "Y-axis"},
    title="Scatter Plot Example",
)

# Scatter plot layout
scatter_plot_layout = html.Div(
    [
        html.H3("Scatter Plot"),
        dcc.Graph(figure=fig),
    ]
)

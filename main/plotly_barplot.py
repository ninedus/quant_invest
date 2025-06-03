from dash import html
import plotly.express as px
from dash import dcc

# Example bar plot
fig = px.bar(
    x=["A", "B", "C", "D"],
    y=[5, 10, 15, 20],
    labels={"x": "Categories", "y": "Values"},
    title="Bar Plot Example",
)

# Bar plot layout
bar_plot_layout = html.Div(
    [
        html.H3("Bar Plot"),
        dcc.Graph(figure=fig),
    ]
)

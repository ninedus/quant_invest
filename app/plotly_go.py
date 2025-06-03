import plotly.graph_objs as go
import numpy as np

# 1. data
random_x = np.random.randint(500, 2000, 100)
random_y = np.random.randint(200, 400, 100)

# 2. scatter definition
trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode="markers",
    name="trade",
    marker=dict(
        size=10, color="blue", symbol="circle", line=dict(width=2, color="black")
    ),
)

# 3. layout definition
layout = go.Layout(
    title="Trace Scatter Plot",
    xaxis=dict(title="X Axis Title"),
    yaxis=dict(title="Y Axis Title"),
    hovermode="closest",
)

# 4. figure definition
fig = go.Figure(data=[trace], layout=layout)
fig.show()

import numpy as np
import plotly.graph_objects as go
import pandas as pd

np.random.seed(42)

random_x1 = np.random.randint(0, 100, 100)
random_x2 = np.random.randint(50, 150, 100)

print(random_x1)
print(random_x2)


trace1 = go.Box(y=random_x1, name="Box 1")
trace2 = go.Box(y=random_x2, name="Box 2")

data = [trace1, trace2]
layout = go.Layout(title="Random variable")
fig = go.Figure(data=data, layout=layout)
fig.show()

print(np.quantile(random_x1, [0.25, 0.5, 0.75]))

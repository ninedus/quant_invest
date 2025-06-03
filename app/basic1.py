import numpy as np
import plotly.graph_objs as go
import pandas as pd

trend = True

np.random.seed(1)

datetime_index = pd.date_range("2022-05-17", "2022-11-12")
random_x = np.random.randint(50, 100, 180)
timeSeries_data = []

if trend:
    trend_factor = np.linspace(1, 180, 180)
    timeSeries_data = random_x + trend_factor
else:
    timeSeries_data = random_x

df = pd.DataFrame(timeSeries_data)
df.index = datetime_index
df.columns = ["Stock A"]

trace = go.Scatter(x=df.index, y=df["Stock A"], mode="lines", name="Stock A")
layout = go.Layout(
    title="Stock A Price", xaxis=dict(title="Date"), yaxis=dict(title="Stock A")
)
fig = go.Figure(data=[trace], layout=layout)
fig.show()

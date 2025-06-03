import numpy as np
import plotly.graph_objs as go
import pandas as pd

trend = True

np.random.seed(1)

datetime_index = pd.date_range("2022-05-17", "2022-11-12")
random_x1 = np.random.randint(50, 100, 180)
random_x2 = np.random.randint(30, 190, 180)
timeSeries_data1 = []
timeSeries_data2 = []

if trend:
    trend_factor = np.linspace(1, 180, 180)
    timeSeries_data1 = random_x1 + trend_factor
    timeSeries_data2 = random_x2 + trend_factor
else:
    timeSeries_data1 = random_x1
    timeSeries_data2 = random_x2

df = pd.DataFrame({"Stock A": timeSeries_data1, "Stock B": timeSeries_data2})
df.index = datetime_index
df.columns = ["Stock A", "Stock B"]

# trace1 = go.Scatter(x=df.index, y=df["Stock A"], mode="lines", name="Stock A")
# trace2 = go.Scatter(x=df.index, y=df["Stock B"], mode="lines", name="Stock B")

# 간결한 코드
data = [
    go.Scatter(x=df.index, y=df["{}".format(i)], mode="lines", name="{}".format(i))
    for i in df.columns
]

layout = go.Layout(
    title="Stock A & Stock B", xaxis=dict(title="Date"), yaxis=dict(title="Stock")
)

# fig = go.Figure(data=[trace1, trace2], layout=layout)
fig = go.Figure(data=data, layout=layout)
fig.show()

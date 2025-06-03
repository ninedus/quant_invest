import numpy as np
import plotly.graph_objects as go
import pandas as pd

salesGrowth = np.random.random(5) * 100
opm = np.round(np.random.random(5) * 100, 2)

df = pd.DataFrame({"salesGrowth": salesGrowth, "OPM": opm})
df.index = ["AAPL", "MS", "TSLA", "MT", "GOOL"]

trace1 = go.Bar(x=df.index, y=df["salesGrowth"], name="Sales Growth")
trace2 = go.Bar(x=df.index, y=df["OPM"], name="OPM")

trace1_h = go.Bar(y=df.index, x=df["salesGrowth"], name="Sales Growth", orientation="h")
trace2_h = go.Bar(y=df.index, x=df["OPM"], name="OPM", orientation="h")

layout = go.Layout(title="Company IS")
fig = go.Figure(data=[trace1_h, trace2_h], layout=layout)
fig.update_layout(barmode="group")
fig.show()

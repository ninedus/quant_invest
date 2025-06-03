import pandas as pd
import plotly.graph_objs as go

import numpy as np

df = pd.read_excel("data/df_etf.xlsx", index_col=0)
df_copy = df.copy()

condition_tiger = [
    df_copy.columns[i]
    for i in range(len(df_copy.columns))
    if df_copy.columns[i].startswith("TIGER")
]

df_copy_tiger = df_copy.loc[:, condition_tiger]

date = "2022-02-14"

oneday_return_1d = np.round(df_copy_tiger.pct_change(periods=1) * 100, 1)
oneday_return_7d = np.round(df_copy_tiger.pct_change(periods=7) * 100, 1)
oneday_return_1d_sample = oneday_return_1d.loc[date]
oneday_return_7d_sample = oneday_return_7d.loc[date]

return_std_1d = np.round(np.std(oneday_return_1d.tail(180)), 1)
return_std_7d = np.round(np.std(oneday_return_7d.tail(180)), 1)
df_tiger_return = pd.DataFrame(
    {
        "1d return": oneday_return_1d_sample,
        "1d std": return_std_1d,
        "7d return": oneday_return_7d_sample,
        "7d std": return_std_7d,
    }
)
df_tiger_return.sort_values("1d return", ascending=False, inplace=True)
oneday_return_1d_sample = df_tiger_return.iloc[:10]
# oneday_return_7d_sample = df_tiger_return.iloc[:10]
print(oneday_return_1d_sample)

data = [
    go.Scatter(
        x=oneday_return_1d_sample.index,
        y=oneday_return_1d_sample["1d return"],
        mode="markers",
        marker=dict(
            size=oneday_return_1d_sample["1d std"] * 20,
            color=oneday_return_1d_sample["7d std"],
            colorscale="Viridis",
            showscale=True,
        ),
        text=oneday_return_1d_sample["1d std"],
    )
]

layout = go.Layout(
    title="TIGER ETF Return {}".format(date),
    xaxis_title="ETF",
    yaxis_title="1d return",
    hovermode="closest",
)
fig = go.Figure(data=data, layout=layout)
fig.show()

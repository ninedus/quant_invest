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

date = "2022-03-15"

tiger_oneday_return = df_copy_tiger.pct_change(periods=1)
tiger_week_return = df_copy_tiger.pct_change(periods=5)
tiger_month_return = df_copy_tiger.pct_change(periods=22)

oneday_return_values = np.round(tiger_oneday_return.loc[date] * 100, 1)
week_return_values = np.round(tiger_week_return.loc[date] * 100, 1)
month_return_values = np.round(tiger_month_return.loc[date] * 100, 1)

df_tiger_return = pd.DataFrame(
    {
        "1d return": oneday_return_values,
        "7d return": week_return_values,
        "30d return": month_return_values,
    }
)
df_tiger_return = df_tiger_return.sort_values("1d return", ascending=False)

N = 10  # Number of top ETFs to display
df_tiger_return_sample = df_tiger_return.iloc[:N]
# print(df_tiger_return_sample)

# data = [
#     go.Bar(
#         x=df_tiger_return_sample.index,
#         y=df_tiger_return_sample["1d return"],
#         name="1d return",
#         orientation="h",
#     ),
#     go.Bar(
#         x=df_tiger_return_sample.index,
#         y=df_tiger_return_sample["7d return"],
#         name="7d return",
#         orientation="h",
#     ),
#     go.Bar(
#         x=df_tiger_return_sample.index,
#         y=df_tiger_return_sample["30d return"],
#         name="30d return",
#         orientation="h",
#     ),
# ]

data = [
    go.Bar(
        y=df_tiger_return_sample.index,
        x=df_tiger_return_sample["{}".format(i)],
        name="{}".format(i),
        orientation="h",
    )
    for i in df_tiger_return_sample.columns
]

layout = go.Layout(title="TIGER ETF RETURN")
fig = go.Figure(data=[data], layout=layout)
fig.show()

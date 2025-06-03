import pandas as pd
import plotly.graph_objs as go

# ETF data
df = pd.read_excel("data/df_etf.xlsx", index_col=0)
df_copy = df.copy()

condition_kodex = [
    df_copy.columns[i] for i in range(df_copy.shape[1]) if "KODEX" in df_copy.columns[i]
]

df_copy_kodex = df_copy.loc[:, condition_kodex]


def cumreturn_line_plot(df, kind1, kind2, startDate, endDate):
    pass


kind1 = "KODEX 200"
kind2 = "KODEX Fn성장"

df_copy_kodex_set = df_copy_kodex.loc[:, [kind1, kind2]]
df_copy_kodex_set = df_copy_kodex_set.dropna()

startDate = "2021-01-12"
endDate = "2022-03-15"
df_copy_kodex_set_sample = df_copy_kodex_set.loc[startDate:endDate, :]

# print(df_copy_kodex_set_sample)

# df_copy_kodex_set_sample.iloc[0]: 기준날짜
df_copy_kodex_set_sample_return = (
    (df_copy_kodex_set_sample - df_copy_kodex_set_sample.iloc[0])
    / df_copy_kodex_set_sample.iloc[0]
) * 100

# print(df_copy_kodex_set_sample_return)

data = [
    go.Scatter(
        x=df_copy_kodex_set_sample_return.index,
        y=df_copy_kodex_set_sample_return["{}".format(i)],
        mode="lines",
        name="{}".format(i),
    )
    for i in df_copy_kodex_set_sample_return.columns
]
layout = go.Layout(
    title="{} & {} cumReturn".format(kind1, kind2),
    xaxis=dict(title="Date"),
    yaxis=dict(title="Return"),
)

fig = go.Figure(data=data, layout=layout)
fig.show()

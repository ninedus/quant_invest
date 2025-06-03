import pandas as pd
import plotly.graph_objs as go


df = pd.read_excel("data/df_etf.xlsx", index_col=0)

df_copy = df.copy()

# kodex etf 추출
condition_kodex_col = [
    df_copy.columns[i]
    for i in range(len(df_copy.columns))
    if df_copy.columns[i].startswith("KODEX")
]
# print(condition_kodex_col)
df_copy_kodex = df_copy.loc[:, condition_kodex_col]
# print(df_copy_kodex.head())


# df_kodex_kind = df_copy_kodex.loc[:, [kind1, kind2]]
# df_copy_kodex = df_kodex_kind.dropna()

# x_value = df_copy_kodex[kind1]
# y_value = df_copy_kodex[kind2]

# trace = go.Scatter(x=x_value, y=y_value, mode="markers", marker=dict(size=4))
# layout = go.Layout(
#     title="{} & {} Correlation".format(kind1, kind2),
#     xaxis=dict(title="{}".format(kind1), tickformat=","),
#     yaxis=dict(title="{}".format(kind2), tickformat=","),
# )

# fig = go.Figure(data=[trace], layout=layout)
# fig.show()


def corr_scatter_plot(df, kind1, kind2):
    df_copy = df.copy()

    df_kodex_kind = df_copy.loc[:, [kind1, kind2]]
    df_copy_kodex = df_kodex_kind.dropna()

    x_value = df_copy_kodex[kind1]
    y_value = df_copy_kodex[kind2]

    trace = go.Scatter(x=x_value, y=y_value, mode="markers", marker=dict(size=4))
    layout = go.Layout(
        title="{} & {} Correlation".format(kind1, kind2),
        xaxis=dict(title="{}".format(kind1), tickformat=","),
        yaxis=dict(title="{}".format(kind2), tickformat=","),
    )

    fig = go.Figure(data=[trace], layout=layout)
    fig.show()


kind1 = "KODEX 200"
kind2 = "KODEX 반도체"
corr_scatter_plot(df_copy_kodex, kind1, kind2)

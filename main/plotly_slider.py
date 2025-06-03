from dash import html
import plotly.express as px
from dash import dcc


layout_slider = html.Div(
    [
        html.Label("Slider"),
        html.Div(
            id="Slider",
            children=[
                dcc.Slider(
                    id="slider",
                    min=-5,
                    max=10,
                    step=1,
                    value=0,
                    marks={i: str(i) for i in range(-5, 11)},
                )
            ],
        ),
        html.Br(),
        html.Label("Radio Items"),
        dcc.RadioItems(
            id="radio",
            options=[
                {"label": "Option 1", "value": "option1"},
                {"label": "Option 2", "value": "option2"},
                {"label": "Option 3", "value": "option3"},
            ],
            value="option1",
        ),
        html.Br(),
        html.Label("Checklist"),
        dcc.Checklist(
            id="check - list",
            options=[
                {"label": "S&P 500", "value": "S&P 500"},
                {"label": "KOSPI", "value": "KOSPI"},
                {"label": "KOSDAQ", "value": "KOSDAQ"},
            ],
            value=["S&P 500", "KOSPI"],
        ),
        html.Br(),
        html.Label("DatePickerRange"),
        dcc.DatePickerRange( # 많이 불편
            id="date-picker-range",
            start_date="2021-01-03",
            end_date="2022-04-30",
            display_format="YYYY-MM-DD",
            min_date_allowed="2021-01-03",
            max_date_allowed="2022-04-30",
        ),
    ]
)

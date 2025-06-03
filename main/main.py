from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from plotly_scatter_plot import scatter_plot_layout
from plotly_barplot import bar_plot_layout
from plotly_bubble import bubble_layout
from arirang_bondfuture_10yr import layout_arirang_bondfuture_10yr
from kodex_histogram import layout_kodex_histogram
from plotly_piechart import layout_piechart
from plotly_heatmap import layout_heatmap
from plotly_slider import layout_slider

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "12rem",
    "padding": "2rem 1rem",
    # "background-color": "#f8f9fa",
    "background-color": "#2b2b2b",
    "color": "#cfcfcf",
    "font-family": "Arial, sans-serif",
    "font-size": "0.9rem",
    "boxShadow": "4px  4px 4px 4px lightgrey",
}

# Define the sidebar layout
sidebar = html.Div(
    [
        html.H2("Stat", className="display-4"),  # main header
        html.Hr(),
        html.P("Select a plot type:", className="lead"),  # sub header
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    "Scatter Plot",
                    href="/scatterplot",
                    active="exact",
                ),
                dbc.NavLink("Bar Plot", href="/barplot", active="exact"),
                dbc.NavLink("Bubble Plot", href="/bubbleplot", active="exact"),
                dbc.NavLink(
                    "ARIRANG 국채선물 10년",
                    href="/arirang_bondfuture_10yr",
                    active="exact",
                ),
                dbc.NavLink(
                    "KODEX Histogram",
                    href="/kodex_histogram",
                    active="exact",
                ),
                dbc.NavLink("Pie Chart", href="/piechart", active="exact"),
                dbc.NavLink("Heatmap", href="/heatmap", active="exact"),
                dbc.NavLink("Slider", href="/slider", active="exact"),
                dbc.DropdownMenu(
                    [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
                    label="Dropdown",
                    nav=True,
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

CONTENT_STYLE = {
    "margin-left": "16rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Define the main content area
content = html.Div(
    id="page-content",
    style=CONTENT_STYLE,
)

# Define the app layout
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

http_404 = html.Div(
    dbc.Container(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(className="my-2"),
            html.P(
                "The pathname was not recognised.",
                className="lead",
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-body-secondary rounded-3",
)


# Define the callback to update the content based on the selected menu
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")],
)
def display_page(pathname):
    if pathname == "/":
        return html.H3(children="Welcome! Please select a menu item from the sidebar.")
    elif pathname == "/scatterplot":
        return scatter_plot_layout
    elif pathname == "/barplot":
        return bar_plot_layout
    elif pathname == "/bubbleplot":
        return bubble_layout
    elif pathname == "/arirang_bondfuture_10yr":
        return layout_arirang_bondfuture_10yr
    elif pathname == "/kodex_histogram":
        return layout_kodex_histogram
    elif pathname == "/piechart":
        return layout_piechart
    elif pathname == "/heatmap":
        return layout_heatmap
    elif pathname == "/slider":
        return layout_slider

    return http_404


# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=8050)

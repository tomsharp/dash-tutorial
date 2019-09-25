import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)


app.layout = html.Div([
    
    # Dash HTML Components - https://dash.plot.ly/dash-html-components
    html.Div("Hello World"),

    html.Br(), html.Br(),

    html.H1("Echo"),
    html.H2("Echo"),
    html.H3("Echo"),

    html.Br(), html.Br(),

    html.Ul([
        html.Li("milk"),
        html.Li("eggs"),
        html.Li("braed"),
    ]),

    html.Ol(id="grocery-list", children=[
        html.Li("milk"),
        html.Li("eggs"),
        html.Li("bread"),
    ]),

    html.Br(), html.Br(),

    html.Button("Button")

])


if __name__ == '__main__':
    app.run_server(debug=True)

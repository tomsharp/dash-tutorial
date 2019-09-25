import dash
import dash_core_components as dcc
import dash_html_components as html


# add Bootstrap as an external stylesheet
external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"]

# pass in external stylesheets when app is instantiated 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([

    # using my custom class from custom.css here
    html.Div(className="my-class", children=[
        "Hello"
    ]),

    html.Br(), html.Br(),

    # using Bootstrap classes from the external stylesheets here
    html.Div(id='buttons', className='d-flex justify-content-center', children=[
        html.Button(className='btn btn-primary', children=["Primary"]),
        html.Button(className='btn btn-secondary', children=["Secondary"]),
        html.Button(className='btn btn-success', children=["Success"]),
    ])

])


if __name__ == '__main__':
    app.run_server(debug=True)

import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)


app.layout = html.Div([
    
    # Dash Core Components - src = https://dash.plot.ly/dash-core-components
    dcc.Textarea(
        placeholder='Enter a value...',
        value='This is a TextArea component',
        style={'width': '100%'}
    ),

    html.Br(), html.Br(),

    dcc.Input(
        placeholder='Enter a value...',
        type='text',
        value=''
    ),

    html.Br(), html.Br(),

    html.Button('Submit', id='button'),
    
    html.Br(), html.Br(),

    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        value=-3
    ),

    html.Br(), html.Br(),

    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Br(), html.Br(),

    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )  

])


if __name__ == '__main__':
    app.run_server(debug=True)

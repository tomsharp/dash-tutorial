
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import numpy as np

# import data 
import pandas as pd
df = pd.read_csv("data/sample.csv")


######### Dash App ###########
app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'}) # CSS style sheet

app.layout = html.Div([
    html.Div(style={'width':'2000px'}, children=[
            dcc.Graph(
                id='scatter-plot',
                className='six columns',
                figure={
                    'data': [go.Scatter(
                        x = df['year'],
                        y = df['total'],
                        mode = 'markers'
                    )],
                    'layout': go.Layout(
                        title='Does anybody care about my ideas?',
                        xaxis={'title':'Minutes I spent talking'},
                        yaxis={'title':'People who listened to me'}
                    )
                },
            )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)

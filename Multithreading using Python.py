import dash
import dash_core_components as dcc
from dash import html
import random
import threading
NUM_NUMBERS = 5

# Define the layout of the dashboard
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Random Number Dashboard'),
    html.Div(children=[
        html.Div(children=[
            html.H2(children='Random Numbers 1 - 1 sec Refresh'),
            dcc.Interval(id='interval1', interval=1000, n_intervals=0),
            html.Ul(id='list1'),
        ], className='four columns'),
        html.Div(children=[
            html.H2(children='Random Numbers 2 - 2 sec Refresh'),
            dcc.Interval(id='interval2', interval=2000, n_intervals=0),
            html.Ul(id='list2'),
        ], className='four columns'),
        html.Div(children=[
            html.H2(children='Random Numbers 3 - 3 sec Refresh'),
            dcc.Interval(id='interval3', interval=3000, n_intervals=0),
            html.Ul(id='list3'),
        ], className='four columns'),
    ], className='row')
])

# Define the callback functions to generate random numbers and update the dashboard
def generate_random_numbers(num_list):
    for i in range(NUM_NUMBERS):
        rand_num = random.randint(1, 100)
        num_list.append(rand_num)

@app.callback(dash.dependencies.Output('list1', 'children'),
              [dash.dependencies.Input('interval1', 'n_intervals')])
def update_list1(n):
    num_list = []
    thread = threading.Thread(target=generate_random_numbers, args=(num_list,))
    thread.start()
    thread.join()
    return [html.Li(str(num)) for num in num_list]

@app.callback(dash.dependencies.Output('list2', 'children'),
              [dash.dependencies.Input('interval2', 'n_intervals')])
def update_list2(n):
    num_list = []
    thread = threading.Thread(target=generate_random_numbers, args=(num_list,))
    thread.start()
    thread.join()
    return [html.Li(str(num)) for num in num_list]

@app.callback(dash.dependencies.Output('list3', 'children'),
              [dash.dependencies.Input('interval3', 'n_intervals')])
def update_list3(n):
    num_list = []
    thread = threading.Thread(target=generate_random_numbers, args=(num_list,))
    thread.start()
    thread.join()
    return [html.Li(str(num)) for num in num_list]

# Start the dashboard server
if __name__ == '__main__':
    app.run_server(debug=True)
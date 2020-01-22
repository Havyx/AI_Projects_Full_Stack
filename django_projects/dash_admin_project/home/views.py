from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objects as go

# def home(request):
#     x_data = [0,1,2,3]
#     y_data = [x**2 for x in x_data]
#     plot_div = plot([Scatter(x=x_data, y=y_data,
#                         mode='lines', name='test', 
#                         opacity=0.8, marker_color='green')],output_type='div')

#     return render(request, "index.html", context={'plot_div': plot_div})

# def home(request):
#     fig = go.Figure()

#     fig.add_trace(go.Scatter(
#         x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
#         y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
#     ))

#     fig.update_layout(
#         autosize=False,
#         width=500,
#         height=500,
#         margin=go.layout.Margin(
#             l=50,
#             r=50,
#             b=100,
#             t=100,
#             pad=4
#         ),
#         paper_bgcolor="LightSteelBlue",
#     )
#     return render(request, "index.html", context={'plot_div': plot_div})

import dash
import dash_core_components as dcc
import dash_html_components as html

from django_plotly_dash import DjangoDash

def home(request):
    app = DjangoDash('simpleexample')

    app.layout = html.Div([
        dcc.RadioItems(
            id='dropdown-color',
            options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
            value='red'
        ),
        html.Div(id='output-color'),
        dcc.RadioItems(
            id='dropdown-size',
            options=[{'label': i, 'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
            value='medium'
        ),
        html.Div(id='output-size')

    ])

    @app.callback(
        dash.dependencies.Output('output-color', 'children'),
        [dash.dependencies.Input('dropdown-color', 'value')])
    def callback_color(dropdown_value):
        return "The selected color is %s." % dropdown_value

    @app.callback(
        dash.dependencies.Output('output-size', 'children'),
        [dash.dependencies.Input('dropdown-color', 'value'),
        dash.dependencies.Input('dropdown-size', 'value')])
    def callback_size(dropdown_color, dropdown_size):
        return "The chosen T-shirt is a %s %s one." %(dropdown_size,
                                                    dropdown_color)

    return render(request, "index.html", context={'SimpleExample': app})





def base(request):
    app = DjangoDash('simpleexample')

    app.layout = html.Div([
        dcc.RadioItems(
            id='dropdown-color',
            options=[{'label': c, 'value': c.lower()} for c in ['Red', 'Green', 'Blue']],
            value='red'
        ),
        html.Div(id='output-color'),
        dcc.RadioItems(
            id='dropdown-size',
            options=[{'label': i, 'value': j} for i, j in [('L','large'), ('M','medium'), ('S','small')]],
            value='medium'
        ),
        html.Div(id='output-size')

    ])

    @app.callback(
        dash.dependencies.Output('output-color', 'children'),
        [dash.dependencies.Input('dropdown-color', 'value')])
    def callback_color(dropdown_value):
        return "The selected color is %s." % dropdown_value

    @app.callback(
        dash.dependencies.Output('output-size', 'children'),
        [dash.dependencies.Input('dropdown-color', 'value'),
        dash.dependencies.Input('dropdown-size', 'value')])
    def callback_size(dropdown_color, dropdown_size):
        return "The chosen T-shirt is a %s %s one." %(dropdown_size,
                                                    dropdown_color)

    return render(request, "base.html", context={'SimpleExample': app})
# Import packages

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Plotly graphs: https://plotly.com/python/
fig = px.histogram(df, x='continent', y='pop', histfunc='avg')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(id = 'title', children={}),
    html.Hr(),
    dcc.Input(id = 'input', type = 'text', value = 'New title'),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='column-options'),
    dag.AgGrid(
        id="grid",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
    ),
    dcc.Graph(figure=fig, id='graph1'),
    
])

# Add controls to build the interaction
@callback(
    Output(component_id='graph1', component_property='figure'),
    Output(component_id='title', component_property='children'),
    Input(component_id='column-options', component_property='value'),
    Input(component_id='input', component_property='value')
)
def update_graph(col_chosen, user_typing):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig, col_chosen



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
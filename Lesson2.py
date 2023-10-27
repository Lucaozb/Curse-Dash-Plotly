#%%Roteiro
#Exercício A: Incorpore o conjunto de dados 2011_us_ag_exports.csv na sua aplicação.  
##E crie o seguinte esquema num ficheiro de aplicação:


#1. Um menu suspenso que usa a coluna estado como opções do menu suspenso. 
## Em seguida, atribua "Alabama" como o valor inicial. O ID do dropdown deve ser igual a "state-dropdown".

#2. Acima do menu pendente, adicione um html.Div e atribua à propriedade id a cadeia de caracteres "my-title". 
##Adicione seu próprio título à propriedade children da html.Div. 
##Abaixo do menu suspenso, adicione um dcc.Graph vazio. O id do componente gráfico deve ser "graph1".


#%% Bibliotecas
import pandas as pd
from dash import Dash, html, dcc, html, callback
import plotly.express as px
import dash_ag_grid as dag

#%%

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

app =  Dash(__name__)
#Layout
app.layout = html.Div([
    html.Div(children = "Exercicio 2"),
    dcc.Dropdown(id="state-dropdown", options=df.state.unique(), value="Alabama"),
    dcc.Graph(id='graph1')
        
])

#@callback()

if __name__ == '__main__':
  app.run(debug=True)

# Aula - Build app with python and dashplotly library
#%%Exercício A 
# incorpore o conjunto de dados shades.csv na sua aplicação. E crie o seguinte esquema num ficheiro da aplicação:

#1. Um menu pendente que utiliza a coluna marca como opções do menu pendente. 
# Certifique-se de que os nomes das marcas são únicos (não se repetem). De seguida, atribua "Revlon" como valor inicial.

#2. Um componente RadioItems em que os valores da coluna denominada grupo são atribuídos à propriedade options. 
# As opções devem ser únicas e ordenadas de 0 a 7.

#3. Actualize a propriedade options do componente RadioItems de modo a que os valores (das opções) representem números de 0 a 7, 
# mas as etiquetas sejam as respectivas cadeias de caracteres (ver Readme-shades para as cadeias de caracteres).

import pandas as pd
from dash import Dash, html, dcc, html, callback
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')
brand = df['brand'].unique()
group = df['group'].unique()


app =  Dash(__name__)
app.layout = html.Div([
    html.Div(children = "Exercicio 1"),
        html.Div([
            
            dcc.Dropdown(
                options= brand,
                value='Revlon'
            ),
            dcc.RadioItems(
                #options = sorted(group) usado para responder o exercicio 2
                options=[{"label": "Fenty Beauty's PRO FILT'R Foundation Only", "value": 0},
                           {"label": "Make Up For Ever's Ultra HD Foundation Only", "value": 1},
                           {"label": "US Best Sellers", "value": 2},
                           {"label": "BIPOC-recommended Brands with BIPOC Founders", "value": 3},
                           {"label": "BIPOC-recommended Brands with White Founders", "value": 4},
                           {"label": "Nigerian Best Sellers", "value": 5},
                           {"label": "Japanese Best Sellers", "value": 6},
                           {"label": "Indian Best Sellers", "value": 7}])
            
        ]),
])

#if __name__ == '__main__':
   # app.run(debug=True)

#%%Exercicio B e C
#Exercício B: utilizando os mesmos shades.csv, crie outra aplicação que incorpore a grid Dash AG no layout:

#1. A grid do Dash AG deve representar o conjunto de dados completo com todas as suas colunas.

#2. Utilizando Paginação, adicione paginação automática do grid Dash AG e 
# certifique-se de que todas as colunas cabem na tela sem barra de deslocamento horizontal 
# (utilizando a propriedade columnSize).
#Exercício C: usando o mesmo shades.csv, crie um novo aplicativo, em que o layout tenha dois novos componentes do Dash Core que você não usou até agora.

#Não haverá uma solução publicada para o exercício C. O objetivo é escolher os componentes com que prefere praticar.



import pandas as pd
from dash import Dash, html, dcc, html, callback
import plotly.express as px
import dash_ag_grid as dag

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')
brand = df['brand'].unique()
group = df['group'].unique()


app =  Dash(__name__)
app.layout = html.Div([
    html.Div(children = "Exercicio 1"),
        html.Div([
            
            dcc.Dropdown(
                options= brand,
                value='Revlon'
            ),
            
            dcc.RadioItems(
                #options = sorted(group) usado para responder o exercicio 2
                options=[{"label": "Fenty Beauty's PRO FILT'R Foundation Only", "value": 0},
                           {"label": "Make Up For Ever's Ultra HD Foundation Only", "value": 1},
                           {"label": "US Best Sellers", "value": 2},
                           {"label": "BIPOC-recommended Brands with BIPOC Founders", "value": 3},
                           {"label": "BIPOC-recommended Brands with White Founders", "value": 4},
                           {"label": "Nigerian Best Sellers", "value": 5},
                           {"label": "Japanese Best Sellers", "value": 6},
                           {"label": "Indian Best Sellers", "value": 7}]),
            
            dcc.Slider(0, 7, 1, value = 0),
            
            dcc.Input(placeholder='Enter a value...', type='text', value=''),
            
            dag.AgGrid(
                id="my-table",
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
                columnSize="sizeToFit",
                defaultColDef={"resizable": True, "sortable": True, "filter": True},
                dashGridOptions={"pagination": True, "paginationAutoPageSize": True, })

        ]),
])

#if __name__ == '__main__':
    #app.run(debug=True)
#%% Exercicio D
#Utilizando o seguinte exemplo de gráfico de dispersão, 
# adicione um gráfico de dispersão à sua aplicação que apresenta V (valor/brilho) no eixo x e S (saturação) no eixo y.

#Dica: para exibir o gráfico no layout, lembre-se de atribuir seu gráfico à propriedade figure do dcc.Graph, 
# por exemplo: dcc.Graph(figure=my_scatter_plot)

import pandas as pd
from dash import Dash, html, dcc, html, callback
import plotly.express as px
import dash_ag_grid as dag

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')
brand = df['brand'].unique()
group = df['group'].unique()

#graficos
fig = px.scatter(df, x='V', y='S')

app =  Dash(__name__)
app.layout = html.Div([
    html.Div(children = "Exercicio 1"),
        html.Div([
            
            dcc.Dropdown(
                options= brand,
                value='Revlon'
            ),
            
            dcc.RadioItems(
                #options = sorted(group) usado para responder o exercicio 2
                options=[{"label": "Fenty Beauty's PRO FILT'R Foundation Only", "value": 0},
                           {"label": "Make Up For Ever's Ultra HD Foundation Only", "value": 1},
                           {"label": "US Best Sellers", "value": 2},
                           {"label": "BIPOC-recommended Brands with BIPOC Founders", "value": 3},
                           {"label": "BIPOC-recommended Brands with White Founders", "value": 4},
                           {"label": "Nigerian Best Sellers", "value": 5},
                           {"label": "Japanese Best Sellers", "value": 6},
                           {"label": "Indian Best Sellers", "value": 7}]),
            
            dcc.Slider(0, 7, 1, value = 0),
            
            dcc.Input(placeholder='Enter a value...', type='text', value=''),
            
            dag.AgGrid(
                id="my-table",
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
                columnSize="sizeToFit",
                defaultColDef={"resizable": True, "sortable": True, "filter": True},
                dashGridOptions={"pagination": True, "paginationAutoPageSize": True, }),
            
            dcc.Graph(figure=fig)

        ]),
])

if __name__ == '__main__':
    app.run(debug=True)
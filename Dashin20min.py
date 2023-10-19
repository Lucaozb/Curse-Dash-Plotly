#%%from dash import Dash, html

#Ao criar aplicativos Dash, 
# você quase sempre usará a instrução de importação acima. 
# Ao criar aplicativos Dash mais avançados, você importará mais pacotes.


#app = Dash(__name__)

#Essa linha é conhecida como o construtor do Dash e é responsável pela inicialização do aplicativo. 
# Ela é quase sempre a mesma para qualquer aplicativo Dash que você criar.

#app.layout = html.Div([
#    html.Div(children='Hello World')
#])

#layout do aplicativo representa os componentes do aplicativo que serão exibidos no navegador da Web, 
# normalmente contidos em um 'html.Div'. Neste exemplo, um único componente foi adicionado: outro 'html.Div'. 
# O Div tem algumas propriedades, como 'children' que usamos para adicionar conteúdo de texto à página: "Hello World".


#if __name__ == '__main__':
#    app.run(debug=True)

#Essas linhas servem para executar o aplicativo e são quase sempre as mesmas para qualquer aplicativo Dash que você criar.

#%% Conectando o banco de dados
#Há muitas maneiras de adicionar dados a um aplicativo: APIs, bancos de dados externos, arquivos .txt locais, arquivos JSON e muito mais. 
# Neste exemplo, destacaremos uma das formas mais comuns de incorporar dados de uma planilha CSV.

#Substitua o código app.py da seção anterior pelo código abaixo. 
# Em seguida, instale o pandas (pip install pandas) e inicie o aplicativo.

#importando pacotes
#from dash import Dash, html, dash_table, dcc
#import pandas as pd
#import plotly.express as px

#Importamos o módulo dcc (DCC significa Dash Core Components). 
# Esse módulo inclui um componente Graph chamado dcc.Graph, que é usado para renderizar gráficos interativos.

#Também importamos a biblioteca plotly.express para criar os gráficos interativos.

#Leitura dos dados
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

#Importamos o módulo dash_table para exibir os dados em uma Dash DataTable. 
# Também importamos a biblioteca pandas para ler os dados da planilha CSV.

#Aqui, lemos a planilha CSV em um dataframe do pandas. Isso facilitará a divisão, o filtro e a inspeção dos dados.

#Se preferir usar uma planilha CSV que esteja em seu computador (e não on-line), certifique-se de salvá-la na mesma pasta que contém o arquivo app.py. 
# Em seguida, atualize a linha de código para: df = pd.read_csv('NameOfYourFile.csv')

#Se estiver usando uma planilha do Excel, certifique-se de instalar o openpyxl pelo pip. 
# Em seguida, atualize a linha de código para: df = pd.read_excel('NameOfYourFile.xlsx', sheet_name='Sheet1')

#A biblioteca de gráficos do Plotly tem mais de 50 tipos de gráficos para você escolher. Neste exemplo, usaremos o gráfico de histograma.


#Inicicializar o dash
#app = Dash(__name__)

#Layout
#app.layout = html.Div([
#    html.Div(children = "Meu Primeiro Dashboard"),
#    dash_table.DataTable(data = df.to_dict('records'), page_size = 10),
#    dcc.Graph(figure = px.histogram(df, x = 'continent', y='lifeExp', histfunc = 'avg'))
#])

#Além do título do aplicativo, adicionamos o componente DataTable e lemos o dataframe do pandas na tabela.
#Usando a biblioteca plotly.express, criamos o gráfico de histograma e o atribuímos à propriedade figure do dcc.Graph. 
# Isso exibe o histograma em nosso aplicativo.

#Inicializar a aplicação
#if __name__ == '__main__':
#    app.run(debug=True)
    
    
# %% Segundo exemplo Controles e Retornos
#Até agora, você criou um aplicativo estático que exibe dados tabulares e um gráfico. 
# No entanto, ao desenvolver aplicativos Dash mais sofisticados, 
# você provavelmente desejará dar ao usuário do aplicativo mais liberdade para interagir com o aplicativo e explorar os dados com mais profundidade. 
# Para isso, será necessário adicionar controles ao aplicativo usando a função callback.

#Neste exemplo, adicionaremos botões de rádio ao layout do aplicativo. 
# Em seguida, criaremos o retorno de chamada para criar a interação entre os botões de opção e o gráfico de histograma.
#Import packages
#from dash import Dash, html, dash_table, dcc, callback, Output, Input
#import pandas as pd
#import plotly.express as px

#Importamos o dcc como fizemos na seção anterior para usar o dcc.Graph. 
# Neste exemplo, precisamos do dcc para o dcc.Graph e também para o componente de botões de seleção, dcc.RadioItems.

#Para trabalhar com o retorno de chamada em um aplicativo Dash, 
# importamos o módulo de retorno de chamada e os dois argumentos normalmente usados no retorno de chamada: Output e Input.


# Incorporate data
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
#app = Dash(__name__)

# App layout
#app.layout = html.Div([
#    html.Div(children='My First App with Data, Graph, and Controls'),
#    html.Hr(),
#    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
#    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
#    dcc.Graph(figure={}, id='controls-and-graph')
#])


#Observe que adicionamos o componente RadioItems ao layout, diretamente acima da DataTable. 
# Há três opções, uma para cada botão de rádio. 
# A opção lifeExp é atribuída à propriedade value, tornando-a o valor selecionado no momento.

#Os componentes RadioItems e Graph receberam nomes de id: eles serão usados pela chamada de retorno para identificar os componentes.

# Add controls to build the interaction
#@callback(
#    Output(component_id='controls-and-graph', component_property='figure'),
#    Input(component_id='controls-and-radio-item', component_property='value')
#)
#def update_graph(col_chosen):
#    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#    return fig

#As entradas e saídas do nosso aplicativo são as propriedades de um componente específico. 
# Neste exemplo, nossa entrada é a propriedade de valor do componente que tem o ID "controls-and-radio-item". 
# Se você observar o layout novamente, verá que ele é atualmente lifeExp. 
# Nossa saída é a propriedade figure do componente com o ID "controls-and-graph", que atualmente é um dicionário vazio (gráfico vazio).

#O argumento col_chosen da função de retorno de chamada refere-se à propriedade de componente do lifeExp de entrada. 
# Criamos o gráfico de histograma dentro da função de retorno de chamada, 
# atribuindo o item selecionado ao atributo do eixo y do histograma. 
# Isso significa que toda vez que o usuário seleciona um novo item, 
# a figura é reconstruída e o eixo y da figura é atualizado.

#Por fim, retornamos o histograma no final da função. 
# Isso atribui o histograma à propriedade figure do dcc.Graph, exibindo assim a figura no aplicativo.


# Run the app
#if __name__ == '__main__':
#    app.run(debug=True)
#%% Quarta Parte HTML and CSS

#HTML e CSS são o nível mais baixo de interface para renderização de conteúdo na Web. 
# O HTML é um conjunto de componentes, e o CSS é um conjunto de estilos aplicados a esses componentes. 
# Os estilos CSS podem ser aplicados dentro dos componentes por meio da propriedade style 
# ou podem ser definidos como um arquivo CSS separado em referência com a propriedade className, como no exemplo abaixo.

# Import packages
#from dash import Dash, html, dash_table, dcc, callback, Output, Input
#import pandas as pd
#import plotly.express as px

# Incorporate data
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app - incorporate css
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = Dash(__name__, external_stylesheets=external_stylesheets)

#adicionando um elemento no external_stylesheets. o codigo css pode ser acessado no link

# App layout
#app.layout = html.Div([
#    html.Div(className='row', children='My First App with Data, Graph, and Controls',
#             style={'textAlign': 'center', 'color': 'black', 'fontSize': 40}),

 #   html.Div(className='row', children=[
  #      dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
   ##                   inline=True,
     #                  id='my-radio-buttons-final')
    #]),

    #html.Div(className='row', children=[
     #   html.Div(className='six columns', children=[
      #      dash_table.DataTable(data=df.to_dict('records'), page_size=15, style_table={'overflowX': 'auto'})
       # ]),
        #html.Div(className='six columns', children=[
         #   dcc.Graph(figure={}, id='histo-chart-final')
        #])
    #])
#])

# Add controls to build the interaction
#@callback(
#    Output(component_id='histo-chart-final', component_property='figure'),
#    Input(component_id='my-radio-buttons-final', component_property='value')
#)
#def update_graph(col_chosen):
#    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
 #   return fig

# Run the app
#if __name__ == '__main__':
 #   app.run(debug=True)
 
 #%%Design kit
 
#O Dash Design Kit é a nossa estrutura de UI de alto nível criada especificamente para o Dash. 
# Com o Dash Design Kit, você não precisa usar HTML ou CSS. Os aplicativos são responsivos para dispositivos móveis por padrão e tudo é tematizável. 
# O Dash Design Kit é licenciado como parte do Dash Enterprise e tem o suporte oficial da Plotly.

#Veja um exemplo do que você pode fazer com o Dash Design Kit (observe que você não poderá executar esse exemplo sem uma licença do Dash Enterprise).
#%% Dash Bootstrap
#
#O Dash Bootstrap é uma biblioteca mantida pela comunidade, criada a partir do sistema de componentes bootstrap.
# Embora não seja oficialmente mantida ou suportada pelo Plotly, a Dash Bootstrap é uma maneira poderosa de criar layouts de aplicativos elegantes. 
# Observe que primeiro definimos uma linha e, em seguida, a largura das colunas dentro da linha, usando os componentes dbc.Row e dbc.Col.

#Para que o aplicativo abaixo seja executado com êxito, certifique-se de instalar a biblioteca Dash Bootstrap Components: pip install dash-bootstrap-components
# link da documentação https://dash-bootstrap-components.opensource.faculty.ai/docs/components/
# Import packages
#from dash import Dash, html, dash_table, dcc, callback, Output, Input
#import pandas as pd
#import plotly.express as px
#import dash_bootstrap_components as dbc

# Incorporate data
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app - incorporate a Dash Bootstrap theme
#external_stylesheets = [dbc.themes.CERULEAN]
#app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
#app.layout = dbc.Container([
#    dbc.Row([
#        html.Div('My First App with Data, Graph, and Controls', className="text-primary text-center fs-3")
#    ]),

#    dbc.Row([
#        dbc.RadioItems(options=[{"label": x, "value": x} for x in ['pop', 'lifeExp', 'gdpPercap']],
#                       value='lifeExp',
#                       inline=True,
#                       id='radio-buttons-final')
#    ]),

#    dbc.Row([
#        dbc.Col([
#            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
#        ], width=6),
#
#        dbc.Col([
#            dcc.Graph(figure={}, id='my-first-graph-final')
#        ], width=6),
#    ]),

#], fluid=True)

## Add controls to build the interaction
#@callback(
#    Output(component_id='my-first-graph-final', component_property='figure'),
#    Input(component_id='radio-buttons-final', component_property='value')
#)
#def update_graph(col_chosen):
#    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#    return fig

# Run the app
#if __name__ == '__main__':
#    app.run(debug=True)
#%% Dash Mantine
#O Dash Mantine é uma biblioteca mantida pela comunidade, criada a partir do sistema de componentes Mantine. 
# Embora não seja oficialmente mantido ou suportado pela equipe do Plotly, o Dash Mantine é outra maneira poderosa de personalizar layouts de aplicativos. 
# Os componentes do Dash Mantine usam o módulo Grid para estruturar o layout. 
# Em vez de definir uma linha, definimos um dmc.Grid, dentro do qual inserimos dmc.Cols e definimos sua largura atribuindo um número à propriedade span.

#Para que o aplicativo abaixo seja executado com êxito, certifique-se de instalar a biblioteca Dash Mantine Components: pip install dash-mantine-components
#link documentação https://www.dash-mantine-components.com/

# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dmc.Container([
    dmc.Title('My First App with Data, Graph, and Controls', color="blue", size="h3"),
    dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in  ['pop', 'lifeExp', 'gdpPercap']],
            id='my-dmc-radio-item',
            value='lifeExp',
            size="sm"
        ),
    dmc.Grid([
        dmc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], span=6),
        dmc.Col([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6),
    ]),

], fluid=True)

# Add controls to build the interaction
@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-dmc-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the App
if __name__ == '__main__':
    app.run(debug=True)

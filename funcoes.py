## Requirements
"""
pandas==1.3.5
plotly==5.5.0
"""
#Bibliotecas
import pandas as pd
import plotly.express as px

#Funções

def tabela_frequencia(df,coluna):

    '''
    Esta função tem como objetivo criar uma tabela de frequência de acordo com 
    as respostas indicadas.
    df = Dataframe do conjunto de dados
    coluna = Coluna com as respectivas respostas 
    '''
    df_tabela_frequencia = pd.DataFrame((df[coluna].value_counts(normalize=True)*100).round(1)).reset_index()
    
    titulo_coluna = coluna.split("'")[3]

    df_tabela_frequencia.columns = [titulo_coluna,'%']

    return df_tabela_frequencia



def percentual_colunas_multiplas_respostas(df,lista_posicao_colunas,titulo_coluna):

    '''
    Esta função tem como objetivo criar uma tabela de frequência de acordo com 
    as multiplas respostas indicadas em várias colunas no conjunto de dados.
    df = Dataframe do conjunto de dados.
    lista_posicao_colunas = Lista com todas as posições das colunasnecesárias 
                            no dataset.
    titulo_coluna = Título da coluna que as respostas terão na tabela de 
                    frequência.
    '''
    
    df_selecionado = df.iloc[:,lista_posicao_colunas]
        
    total = df_selecionado.sum().sum()

    df_percentual = ((df_selecionado.sum().sort_values(ascending=False) / total)*100).round(1)
    
    df_percentual = pd.DataFrame(df_percentual,columns=['%'])
    
    df_percentual.index = [i.split(',')[1].split("'")[1] for i in df_percentual.index]
    
    df_percentual = df_percentual.reset_index()

    df_percentual.columns = [titulo_coluna, '%']
    
    return df_percentual



def grafico_barras(tabela,rotulo_eixo_y,titulo,quantidade_cores,quantidade_barras):

    '''
    Esta função tem como objetivo criar um gráfico de barras horizontais,
    a partir da tabela de frequência criada. 
    Ele irá variar a cor de acordo com a relevância das respostas.
    Por exemplo:
      Caso apenas haja uma única resposta mais relevante, apenas uma barra 
      (a primeira) terá a cor azul marinho, as demais ficarão na cor cinza.
    
    tabela = Tabela de frequência criada.
    rotulo_eixo_y = Rótulo do eixo y do gráfico
    titulo = Título do gráfico
    quantidade_cores = Quantidade de cores que serão mostradas na barra de acordo
                        com o dicinário "cores".
    quantidade_barras = Quantidade de barras totais do gráfico.
    '''

    cores = {
        'cores_uma_barra': ['navy'] + ['gray'] * (len(tabela) - 1),
        'cores_duas_barras': ['navy']*2 + ['gray'] * (len(tabela) - 2),
        'cores_tres_barras': ['navy']*3 + ['gray'] * (len(tabela) - 3),
        'cores_todas_barras': ['navy']
    }
  


    fig = px.bar(tabela[:quantidade_barras],x='%',y=tabela.columns[0],
            width=1200,
            color=tabela.columns[0],
            color_discrete_sequence = cores[quantidade_cores])

    fig.update_layout(
        title=titulo,
        title_font_size=20,
        yaxis_title=rotulo_eixo_y,
        showlegend=False)
    
    fig.show()

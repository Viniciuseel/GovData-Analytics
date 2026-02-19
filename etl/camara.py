import requests
import pandas as pd

def extrair_deputados_brutos():
    dados = []
    url ='https://dadosabertos.camara.leg.br/api/v2/deputados'
    response = requests.get(url)
    response.raise_for_status()

    return response.json()['dados']

def tratar_deputados(dados_brutos):
    df = pd.DataFrame(dados_brutos)

    colunas_desejadas = ['id','nome','siglaUf','siglaPartido','urlFoto']
    df_limpo = df[ colunas_desejadas]
    df_limpo = df_limpo.rename(columns = {
        'siglaUf':'Estado',
    'siglaPartido':'Partido'
    }
    )
    return df_limpo

def salvar_dados(df_limpo):
    with open('camara.csv', 'w') as arquivo:
        df_limpo.to_csv(arquivo)

    return arquivo

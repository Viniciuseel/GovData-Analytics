import requests
import pandas as pd
from database.db import engine

def extrair_deputados_brutos():
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
    'siglaPartido':'Partido',
    'urlFoto' : 'foto'
    }
    )
    return df_limpo
def salvar_dados_banco(df_limpo):
    df_limpo.to_sql('banco_de_deputados',con=engine, if_exists='append', index=False )
    print('salvando a banco_de_deputados')

# def salvar_dados(df_limpo):
#         df_limpo.to_csv("deputados.csv", index=False)



import uuid

import requests
import pandas as pd
from database.db import engine
from uuid import uuid4

def extrair_deputados_brutos():
    url ='https://dadosabertos.camara.leg.br/api/v2/deputados'
    response = requests.get(url)
    response.raise_for_status()

    return response.json()['dados']

def tratar_deputados(dados_brutos):
    df = pd.DataFrame(dados_brutos)

    # criar Id unico e separar do id da API , colunas em minusculo
    colunas_desejadas = ['id','nome','siglaUf','siglaPartido','urlFoto']
    df_limpo = df[ colunas_desejadas].copy
    df_limpo = df_limpo.rename(columns = {
        'id':'id_camara',
        'siglaUf':'estado',
    'siglaPartido':'partido',
    'urlFoto' : 'foto'
    }
    )

    df_limpo.columns = df_limpo.columns.str.strip().str.lower()

    df_limpo['nome'] = df_limpo['nome'].str.strip().str.title()

    df_limpo = df_limpo.dropna(subset=['nome'])
    df_limpo = df_limpo.dropna(subset=['id_camara'])

    df_limpo['id'] = [str(uuid.uuid4()) for _ in range(len(df_limpo))]

    df_limpo = df_limpo[['id','id_camara','nome','estado','partido','foto']]

    df_limpo['estado'] = df_limpo['estado'].astype('category'
                              )
    return df_limpo

def salvar_dados_banco(df_limpo):
    df_limpo.to_sql('banco_de_deputados',con=engine, if_exists='replace', index=False )

    print('salvando a banco_de_deputados')




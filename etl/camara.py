import uuid
import logging
import requests
import pandas as pd
from database.db import engine
from uuid import uuid4

logger = logging.getLogger(__name__)

def extrair_deputados_brutos():
    logger.info('Extraindo os deputados da API')
    try:
        url ='https://dadosabertos.camara.leg.br/api/v2/deputados'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()['dados']

    except requests.exceptions.RequestException as e:
        logger.exception(f'Falha critica ao tentar baixar os dados da Camâra')

        raise e

def tratar_deputados(dados_brutos):
    logger.info(f'Iniciando tratamento de {len(dados_brutos)} registros vindo da API'

                )
    df = pd.DataFrame(dados_brutos)
    logger.debug('DataFrame inicial montado na memoria')

    df['Extraido em'] = pd.Timestamp.now(tz='America/Fortaleza')
    logger.debug(f"Timestamp de extração aplicado")

    colunas_desejadas = ['id','nome','siglaUf','siglaPartido','urlFoto']
    df_limpo = df[ colunas_desejadas].copy()
    df_limpo = df_limpo.rename(columns = {

        'id':'id_camara',
        'siglaUf':'estado',
    'siglaPartido':'partido',
    'urlFoto' : 'foto'
    }

    )

    df_limpo.columns = df_limpo.columns.str.strip().str.lower()
    df_limpo['nome'] = df_limpo['nome'].str.strip().str.title()

    qtd_antes = len(df_limpo)

    df_limpo = df_limpo.dropna(subset=['nome'])
    df_limpo = df_limpo.dropna(subset=['id_camara'])

    qtd_depois = len(df_limpo)

    if qtd_antes > qtd_depois:
        deputados_perdidos = qtd_depois - qtd_antes
        logger.warning(f"A quantidade de deputadoe atual {qtd_depois} é menor que a anterior {qtd_antes} a diferença é: {deputados_perdidos}")


    df_limpo['id'] = [str(uuid.uuid4()) for _ in range(len(df_limpo))]

    df_limpo = df_limpo[['id','id_camara','nome','estado','partido','foto']]

    df_limpo['estado'] = df_limpo['estado'].astype('category'
                              )
    return df_limpo

def salvar_dados_banco(df_limpo):

    logger.info('Iniciando persistencia dos dados')
    df_limpo.to_sql('banco_de_deputados',con=engine, if_exists='replace', index=False )
    logger.info(f'Sucesso:{len(df_limpo)} deputados salvos com sucesso ')

    logger.debug(f'Amostra de dados\n {df_limpo.head(3)}')
    





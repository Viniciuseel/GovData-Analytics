from etl.camara import tratar_deputados, extrair_deputados_brutos, salvar_dados_banco
from utils.log import configure_log
import logging

configure_log()
logger=logging.getLogger("Main")

def iniciar_pipeline():

    logger.info("Iniciando pipeline de deputados")

    try:
        dados_sujos = extrair_deputados_brutos()
        dados_limpos = tratar_deputados(dados_sujos)

        salvar_dados_banco(dados_limpos)
        logger.info("pipeline finalizado com sucesso")
    except Exception as e:
        logger.error(f'Pipeline Falhou Detalhes: {e}', exc_info=True  )

if __name__ == '__main__':
    iniciar_pipeline()



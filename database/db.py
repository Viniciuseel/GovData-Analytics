import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import logging

logger = logging.getLogger(__name__)

load_dotenv()

usuario = os.getenv("POSTGRES_USER")
senha = os.getenv("POSTGRES_PASSWORD")
banco = os.getenv("POSTGRES_DB")
port = os.getenv("POSTGRES_PORT", 5432)
host = os.getenv("POSTGRES_HOST",)

if senha is None:
    raise ValueError("A variavel de ambiente POSTGRES_PASSWORD não está definida por favor verifique o arquivo .env ")

if usuario is None:
    raise ValueError('Variavel de ambiente POSTGRES_USER não está definida, por favor verifique o arquivo .env ')

credenciais = [usuario, senha, banco, port]

string_conexao = f"postgresql+psycopg2://{usuario}:{senha}@{host}:{port}/{banco}"
engine = create_engine(string_conexao)

try:
    logger.debug(f'testando conexão com o banco de dados {banco}, usuario: {usuario}, porta: {port}  ')
    with engine.connect() as conexao:
        logger.info(f'Sucesso ao conectar ao banco:  {banco}')
except Exception as e:
    raise ConnectionError(f'Impossivel Prosseguir: o banco de dados recusou a conexão DetalheS: {e}')

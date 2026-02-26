import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

usuario = os.getenv("POSTGRES_USER")
senha = os.getenv("POSTGRES_PASSWORD")
banco = os.getenv("POSTGRES_DB")
port = os.getenv("POSTGRES_PORT")

string_conexao = f"postgresql+psycopg2://{usuario}:{senha}@localhost:{port}/{banco}"
engine = create_engine(string_conexao)


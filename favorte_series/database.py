# Importa os componentes
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Definindo o arquivo do banco SQLite
DATABASE_URL = "sqlite:///./series.db"

# Cria a conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Criando a fábrica para intereafir com o banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Criando a classe
class Base(DeclarativeBase):
    pass
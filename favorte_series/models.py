# Importando os tipos de coluna
from sqlalchemy import Column, Integer, String

# Importando a classe 
from database import Base


# Definindo a tabela de séries favoritas
class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    seasons = Column(Integer, nullable=False)
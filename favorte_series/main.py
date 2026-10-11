# Importa a configuração do banco
from database import engine, Base, SessionLocal

# Importa o modelo para registrar a tabela
from models import Series

# Importa o CRUD
from crud import (
    create_series,
    list_series,
    get_series,
    update_series,
    delete_series
)

# Cria as tabelas caso não existam
Base.metadata.create_all(bind=engine)

# Abre uma sessão com o banco
session = SessionLocal()

try:
    # CREATE: cadastra três séries
    print("\n=== CREATE ===")

    serie1 = create_series(
        session, "Breaking Bad", "Drama", 5
    )
    serie2 = create_series(
        session, "Stranger Things", "Ficção científica", 4
    )
    serie3 = create_series(
        session, "The Office", "Comédia", 9
    )

    print(f"Cadastrada: {serie1.title} (ID: {serie1.id})")
    print(f"Cadastrada: {serie2.title} (ID: {serie2.id})")
    print(f"Cadastrada: {serie3.title} (ID: {serie3.id})")

    # READ: lista todas as séries
    print("\n=== READ ===")

    for serie in list_series(session):
        print(serie.id, serie.title, serie.genre, serie.seasons)

    # READ BY ID: busca a primeira série
    print("\n=== READ BY ID ===")

    encontrada = get_series(session, serie1.id)

    if encontrada:
        print(
            encontrada.id,
            encontrada.title,
            encontrada.genre,
            encontrada.seasons
        )
    else:
        print("Série não encontrada.")

    # UPDATE: atualiza a primeira série
    print("\n=== UPDATE ===")

    atualizada = update_series(
        session,
        serie1.id,
        "Breaking Bad",
        "Drama e suspense",
        5
    )

    if atualizada:
        print(
            "Série atualizada:",
            atualizada.title,
            atualizada.genre,
            atualizada.seasons
        )
    else:
        print("Série não encontrada para atualização.")

    # DELETE: remove a segunda série
    print("\n=== DELETE ===")

    excluida = delete_series(session, serie2.id)

    if excluida:
        print(f"Série {serie2.title} removida com sucesso.")
    else:
        print("Série não encontrada para exclusão.")

    # READ FINAL: mostra o estado final do banco
    print("\n=== READ FINAL ===")

    for serie in list_series(session):
        print(serie.id, serie.title, serie.genre, serie.seasons)

finally:
    # Fecha a sessão mesmo se ocorrer um erro
    session.close()
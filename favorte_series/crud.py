from models import Series


# CREATE: cadastra uma nova série
def create_series(session, title, genre, seasons):
    nova_serie = Series(
        title=title,
        genre=genre,
        seasons=seasons
    )

    session.add(nova_serie)
    session.commit()
    session.refresh(nova_serie)

    return nova_serie


# READ: lista todas as séries
def list_series(session):
    return session.query(Series).all()


# READ BY ID: busca uma série pelo ID
def get_series(session, series_id):
    return session.query(Series).filter(
        Series.id == series_id
    ).first()


# UPDATE: atualiza uma série existente
def update_series(session, series_id, title, genre, seasons):
    db_serie = get_series(session, series_id)

    if db_serie is None:
        return None

    db_serie.title = title
    db_serie.genre = genre
    db_serie.seasons = seasons

    session.commit()
    session.refresh(db_serie)

    return db_serie


# DELETE: remove uma série existente
def delete_series(session, series_id):
    db_serie = get_series(session, series_id)

    if db_serie is None:
        return False

    session.delete(db_serie)
    session.commit()

    return True
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./books.db"

# check_same_thread=False : nécessaire car FastAPI peut traiter les requêtes
# sur des threads différents, ce que SQLite interdit par défaut.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# sessionmaker = une "usine" à sessions : chaque requête HTTP obtient
# sa propre session, plutôt qu'une session unique partagée par toute
# l'application (risque de conflits entre requêtes simultanées).
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe mère dont héritera Book (models.py), pour que SQLAlchemy
# sache la relier à une vraie table SQL.
Base = declarative_base()


def get_db():
    """
    Générateur utilisé avec Depends(get_db) dans routes.py.
    yield fournit la session à la route ; finally garantit sa fermeture
    même si une erreur survient pendant le traitement de la requête.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
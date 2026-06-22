from fastapi import FastAPI

from .database import Base, engine
from .routes import router

# Crée la table books si elle n'existe pas encore. N'écrase jamais
# les données existantes : ne fait rien si la table est déjà présente.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Books API")

# Sans cette ligne, les routes existeraient dans le code mais
# resteraient inaccessibles depuis l'extérieur.
app.include_router(router)
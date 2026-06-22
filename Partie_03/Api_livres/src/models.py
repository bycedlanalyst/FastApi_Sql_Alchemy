from sqlalchemy import Column, Integer, String
from .database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    # nullable=False : contrainte au niveau de la base elle-même,
    # en complément de la validation Pydantic (schemas.py). Protège
    # l'intégrité des données même si un bug contournait la validation API.
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
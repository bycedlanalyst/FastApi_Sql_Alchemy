from pydantic import BaseModel, Field, ConfigDict


class BookCreate(BaseModel):
    """
    Données envoyées par le client (POST/PUT). Ne contient jamais l'id,
    puisque celui-ci est généré par la base, pas fourni par l'utilisateur.
    """
    title: str = Field(..., min_length=2)
    author: str = Field(..., min_length=2)
    year: int = Field(..., ge=1900)
    rating: int = Field(..., ge=0, le=5)


class BookResponse(BaseModel):
    """
    Données renvoyées par l'API. Séparé de BookCreate car cette
    réponse inclut l'id, contrairement à ce que le client envoie.
    """
    id: int
    title: str
    author: str
    year: int
    rating: int

    # Permet à Pydantic de lire un objet SQLAlchemy via ses attributs
    # (book.title) plutôt qu'un simple dict, pour convertir vers du JSON.
    model_config = ConfigDict(from_attributes=True)


class BookStatus(BaseModel):
    """
    Schéma dédié à /books/{id}/status. Pas de validation Field ici :
    ces valeurs sont calculées par notre propre code (compute_status),
    pas saisies par un client, donc pas besoin de les revalider.
    """
    id: int
    status: str
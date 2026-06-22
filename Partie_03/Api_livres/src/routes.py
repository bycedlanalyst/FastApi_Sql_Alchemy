from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .database import get_db
from .schemas import BookCreate, BookResponse, BookStatus
from .services import (
    create_book,
    get_all_books,
    get_book_by_id,
    update_book,
    delete_book,
    compute_status
)

router = APIRouter()


@router.get("/")
def home():
    return {"message": "API Books OK"}


@router.get("/books", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):
    return get_all_books(db)


# response_model=BookResponse : FastAPI valide aussi la sortie, pas
# seulement l'entrée (payload), et filtre les champs renvoyés au client.
@router.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def add_book(payload: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, payload)


@router.get("/books/{book_id}", response_model=BookResponse)
def get_one_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book_by_id(db, book_id)
    if not book:
        # services.py a renvoyé None ; c'est ici qu'on traduit
        # cette absence en une vraie erreur HTTP.
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/books/{book_id}", response_model=BookResponse)
def edit_book(book_id: int, payload: BookCreate, db: Session = Depends(get_db)):
    book = update_book(db, book_id, payload)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_book(book_id: int, db: Session = Depends(get_db)):
    deleted = delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    # 204 No Content : succès, mais rien à renvoyer (le livre n'existe
    # plus), convention HTTP standard pour un DELETE réussi.
    return None


@router.get("/books/{book_id}/status", response_model=BookStatus)
def get_status(book_id: int, db: Session = Depends(get_db)):
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "id": book.id,
        "status": compute_status(book)
    }
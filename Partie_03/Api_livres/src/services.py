from sqlalchemy.orm import Session
from .models import Book
from .schemas import BookCreate


def create_book(db: Session, payload: BookCreate):
    book = Book(
        title=payload.title,
        author=payload.author,
        year=payload.year,
        rating=payload.rating
    )
    db.add(book)
    db.commit()
    # refresh recharge l'objet depuis la base pour récupérer l'id
    # généré par SQLite, inconnu de l'objet Python avant cet appel.
    db.refresh(book)
    return book


def get_all_books(db: Session):
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int):
    # Renvoie None si introuvable plutôt que de lever une exception :
    # c'est à routes.py, pas à services.py, de décider du code HTTP (404).
    # services.py reste ainsi indépendant du protocole HTTP.
    return db.query(Book).filter(Book.id == book_id).first()


def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if not book:
        return False

    db.delete(book)
    db.commit()
    return True


def update_book(db: Session, book_id: int, payload: BookCreate):
    book = get_book_by_id(db, book_id)
    if not book:
        return None

    book.title = payload.title
    book.author = payload.author
    book.year = payload.year
    book.rating = payload.rating

    db.commit()
    db.refresh(book)
    return book


def compute_status(book: Book):
    # Règle métier : >=4 d'abord, sinon un rating de 5 tomberait
    # dans "average" si on testait >=2 en premier (ordre important).
    if book.rating >= 4:
        return "recommended"
    elif book.rating >= 2:
        return "average"
    else:
        return "bad"
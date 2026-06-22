import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database import Base
from src.models import Book
from src.schemas import BookCreate
from src.services import (
    create_book,
    get_all_books,
    get_book_by_id,
    update_book,
    delete_book,
    compute_status
)


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    yield session
    session.close()


def test_create_book_ajoute_un_livre(db_session):
    payload = BookCreate(title="1984", author="George Orwell", year=1949, rating=5)
    book = create_book(db_session, payload)

    assert book.id is not None
    assert book.title == "1984"
    assert len(get_all_books(db_session)) == 1


def test_get_book_by_id_retourne_le_bon_livre(db_session):
    payload = BookCreate(title="Clean Code", author="Robert C. Martin", year=2008, rating=5)
    created = create_book(db_session, payload)

    found = get_book_by_id(db_session, created.id)

    assert found is not None
    assert found.title == "Clean Code"


def test_get_book_by_id_retourne_none_si_introuvable(db_session):
    result = get_book_by_id(db_session, 999)
    assert result is None


def test_update_book_modifie_le_livre(db_session):
    payload = BookCreate(title="1984", author="George Orwell", year=1949, rating=3)
    created = create_book(db_session, payload)

    new_payload = BookCreate(title="1984", author="George Orwell", year=1949, rating=5)
    updated = update_book(db_session, created.id, new_payload)

    assert updated is not None
    assert updated.rating == 5


def test_delete_book_supprime_le_livre(db_session):
    payload = BookCreate(title="1984", author="George Orwell", year=1949, rating=5)
    created = create_book(db_session, payload)

    result = delete_book(db_session, created.id)

    assert result is True
    assert get_book_by_id(db_session, created.id) is None


def test_compute_status_recommended():
    book = Book(title="X", author="Y", year=2000, rating=5)
    assert compute_status(book) == "recommended"


def test_compute_status_average():
    book = Book(title="X", author="Y", year=2000, rating=3)
    assert compute_status(book) == "average"


def test_compute_status_bad():
    book = Book(title="X", author="Y", year=2000, rating=1)
    assert compute_status(book) == "bad"


@pytest.mark.skip(reason="Pagination de GET /books pas encore implémentée")
def test_get_all_books_avec_pagination(db_session):
    pass
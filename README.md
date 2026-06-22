# FastApi_Sql_Alchemy

Regroupement des trois parties du projet :
- `Partie_01` : réponses théoriques sur la programmation et l'architecture logicielle.
- `Partie_02` : mini-module bancaire Python avec tests unitaires.
- `Partie_03` : API REST de gestion de livres avec FastAPI, SQLAlchemy et SQLite.

## Structure du projet

- `Partie_01/`
  - `reponses_partie_1.md` : réponses aux questions de cours sur la programmation procédurale, la POO, les classes, objets, attributs, méthodes, modules, packages et les opérations CRUD.

- `Partie_02/module_bacaire/`
  - `src/compte.py` : implémentation de `CompteBancaire` avec dépôt, retrait, consultation du solde et représentation.
  - `src/exceptions.py` : exceptions métier personnalisées `MontantInvalideError` et `SoldeInsuffisantError`.
  - `tests/test_compte.py` : tests unitaires du module bancaire avec `pytest`.
  - `README.md` : description fonctionnelle et choix techniques du module bancaire.

- `Partie_03/Api_livres/`
  - `src/database.py` : configuration de la base SQLite et gestion des sessions SQLAlchemy.
  - `src/models.py` : définition du modèle `Book` pour la table `books`.
  - `src/schemas.py` : schémas Pydantic `BookCreate`, `BookResponse`, `BookStatus`.
  - `src/services.py` : logique métier pour créer, lire, modifier, supprimer des livres et calculer le statut métier.
  - `src/routes.py` : routes FastAPI pour exposer l'API REST.
  - `src/main.py` : application FastAPI et initialisation de la base.
  - `requirements.txt` : dépendances Python nécessaires au projet API.
  - `tests/test_books.py` : tests unitaires de l'API livres.
  - `README.md` : documentation locale de l'API livres.

## Partie 1 — Réponses de cours

Le fichier `Partie_01/reponses_partie_1.md` couvre :
- La différence entre programmation procédurale et programmation orientée objet.
- La distinction entre classe et objet.
- La différence entre attribut et méthode.
- Le rôle de `__init__` et de `self` en Python.
- La différence entre module Python et package Python.
- Les opérations CRUD et leurs méthodes HTTP associées.
- Le rôle de `schemas.py`, `services.py` et `models.py` dans une application web.
- La définition d'un test unitaire et le concept de régression logicielle.

## Partie 2 — Module bancaire

### Fonctionnalités

- Création d'un compte bancaire avec titulaire et solde initial.
- Dépôt d'argent avec validation du montant positif.
- Retrait d'argent avec vérification du solde disponible.
- Consultation du solde.
- Gestion des erreurs métier via exceptions personnalisées.

### Fichiers principaux

- `Partie_02/module_bacaire/src/compte.py`
- `Partie_02/module_bacaire/src/exceptions.py`
- `Partie_02/module_bacaire/tests/test_compte.py`

### Tests

Exécuter depuis `Partie_02/module_bacaire/` :

```bash
pytest
```

## Partie 3 — API livres

### Fonctionnalités

- `GET /books` : liste tous les livres.
- `POST /books` : crée un livre.
- `GET /books/{book_id}` : récupère un livre par son ID.
- `PUT /books/{book_id}` : modifie un livre.
- `DELETE /books/{book_id}` : supprime un livre.
- `GET /books/{book_id}/status` : renvoie le statut métier d'un livre (`recommended`, `average`, `bad`) selon sa note.

### Architecture

- `src/database.py` : connexion SQLite et session SQLAlchemy.
- `src/models.py` : modèle `Book` représentant la table SQL.
- `src/schemas.py` : validation des entrées/sorties via Pydantic.
- `src/services.py` : logique métier séparée du code HTTP.
- `src/routes.py` : routes FastAPI et gestion des codes HTTP.
- `src/main.py` : initialisation de l'application et création des tables.

### Démarrage

Depuis `Partie_03/Api_livres/` :

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

L'API est ensuite accessible sur `http://127.0.0.1:8000`.
La documentation interactive Swagger est disponible sur `http://127.0.0.1:8000/docs`.

### Tests

Depuis `Partie_03/Api_livres/` :

```bash
pytest
```

## Technologies utilisées

- Python 3
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- pytest

## Principaux choix techniques

- Séparation nette entre la logique métier (`services.py`) et les routes HTTP (`routes.py`).
- Utilisation de schémas Pydantic pour valider les données entrantes et sortantes.
- Exceptions métier spécifiques dans le module bancaire pour bien distinguer les erreurs de domaine.
- Tests unitaires avec `pytest` pour valider le comportement des deux applications.

## Limites connues

- Partie 2 : pas de gestion de devises ni d'historique des transactions.
- Partie 3 : pas d'authentification, pas de pagination et pas de gestion des utilisateurs.

## Remarques

Ce README global complète les README spécifiques de chaque sous-projet et fournit une vue d'ensemble des trois parties de l'exercice.

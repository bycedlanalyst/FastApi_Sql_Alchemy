# API Livres — FastAPI + SQLAlchemy + SQLite

## Description

API REST de gestion de livres permettant de créer, lire, modifier, supprimer
des livres et de consulter leur statut métier (recommended / average / bad)
selon leur note.

## Lancement

Depuis le dossier `Partie_03/api_livres/` :

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

L'API est accessible sur `http://127.0.0.1:8000`, la documentation
interactive sur `http://127.0.0.1:8000/docs`.

## Choix techniques

- **Architecture en couches** : `routes.py` (HTTP) → `services.py` (logique
  métier) → `models.py` (structure SQL) → `database.py` (connexion). Chaque
  couche ignore le fonctionnement de celle qui la précède, ce qui permet de
  faire évoluer une couche sans impacter les autres.
- **SQLite** choisi pour sa simplicité (un seul fichier `books.db`, aucun
  serveur de base de données à installer), suffisant pour ce projet.
  `connect_args={"check_same_thread": False}` est nécessaire car FastAPI
  peut traiter les requêtes sur des threads différents, ce que SQLite
  interdit par défaut.
- **Pydantic (`schemas.py`)** valide les données dès leur entrée dans
  l'API (avant même l'exécution du code métier), avec des messages d'erreur
  HTTP 422 explicites pour le client.
- **`BookCreate` et `BookResponse` séparés** : le client n'envoie jamais
  l'`id` (généré par la base), donc le schéma d'entrée ne le contient pas,
  contrairement au schéma de sortie.
- **`services.py` ne lève jamais d'exception HTTP** : il renvoie `None`
  ou `False` quand une ressource n'existe pas, laissant `routes.py`
  seul responsable de traduire ça en code HTTP (404). Ce découplage permet
  de réutiliser la logique métier hors d'un contexte HTTP si besoin.

## Limites connues

- Pas d'authentification ni de gestion des utilisateurs.
- Pas de pagination sur `GET /books` : tous les livres sont renvoyés en
  une seule fois.
- Les erreurs de validation Pydantic renvoient le format d'erreur par
  défaut de FastAPI plutôt qu'un message personnalisé.

## Régression simulée

Dans `services.py`, la fonction `compute_status` teste les conditions
dans l'ordre `rating >= 4` puis `rating >= 2`. Si on inversait l'ordre
(`rating >= 2` testé avant `rating >= 4`), un livre noté 5 serait
incorrectement classé `"average"` au lieu de `"recommended"`, car la
première condition vraie rencontrée (`>= 2`) arrête l'évaluation avant
d'atteindre la bonne règle. Un test vérifiant `compute_status` avec une
note de 5 détecterait immédiatement cette régression.
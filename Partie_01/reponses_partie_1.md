# Partie 1 — Réponses aux questions de cours

## 1. Différence entre programmation procédurale et programmation orientée objet

La programmation procédurale organise le code autour de **fonctions** qui
manipulent des données passées en paramètres, sans lien permanent entre les
données et les fonctions qui les traitent (ex : les fonctions de
`services.py`, qui reçoivent un `book` ou un `db` en paramètre).

La programmation orientée objet (POO) regroupe les données (attributs) et
les comportements (méthodes) qui les manipulent à l'intérieur d'une même
entité, l'objet (ex : `CompteBancaire`, où `solde` et `deposer()` vivent
ensemble dans la même classe). L'objet porte son propre état et les
règles qui le font évoluer.

## 2. Différence entre une classe et un objet

Une **classe** est un modèle, un plan de construction (ex : `CompteBancaire`
décrit ce que doit avoir tout compte bancaire : un titulaire, un solde,
des méthodes pour déposer/retirer).

Un **objet** est une instance concrète créée à partir de ce plan
(ex : `compte = CompteBancaire("Alice", 100)` crée un objet réel, avec ses
propres valeurs pour `titulaire` et `solde`). Plusieurs objets peuvent être
créés à partir de la même classe, chacun avec son propre état.

## 3. Différence entre un attribut et une méthode

Un **attribut** est une donnée stockée dans l'objet (ex : `self.solde`,
`self.titulaire`) : il représente l'état de l'objet à un instant donné.

Une **méthode** est une fonction définie dans la classe, qui agit sur les
attributs de l'objet (ex : `deposer()`, `retirer()`) : elle représente un
comportement, une action que l'objet peut effectuer.

## 4. Rôle de `__init__` et de `self`

`__init__` est le **constructeur** : la méthode automatiquement appelée
lors de la création d'un objet (`CompteBancaire("Alice", 100)`), qui
initialise ses attributs et peut y appliquer des règles de validation
dès la création (ex : refuser un solde initial négatif).

`self` représente **l'instance elle-même** à l'intérieur d'une méthode :
il permet d'accéder et de modifier les attributs propres à cet objet
précis (`self.solde`), et de distinguer cet objet des autres instances de
la même classe.

## 5. Différence entre un module Python et un package Python

Un **module** est un simple fichier `.py` contenant du code réutilisable
(ex : `compte.py`, `exceptions.py`).

Un **package** est un dossier contenant plusieurs modules, regroupés sous
un même espace de noms, et reconnu comme tel par Python grâce à la
présence d'un fichier `__init__.py` (ex : le dossier `src/`, qui contient
`database.py`, `models.py`, `routes.py`, etc.). Un package permet
d'organiser plusieurs modules liés entre eux et de les importer comme un
ensemble cohérent (`from src.models import Book`).

## 6. Les quatre opérations CRUD et leur méthode HTTP associée

| Opération | Méthode HTTP | Exemple dans le projet |
|---|---|---|
| Create (créer) | POST | `POST /books` |
| Read (lire) | GET | `GET /books`, `GET /books/{id}` |
| Update (modifier) | PUT | `PUT /books/{id}` |
| Delete (supprimer) | DELETE | `DELETE /books/{id}` |

## 7. Rôle de `schemas.py`, `services.py` et `models.py`

- **`models.py`** décrit la structure d'une table SQL sous forme de classe
  Python (via SQLAlchemy), pour que l'ORM sache à quelle table et quelles
  colonnes correspond chaque objet (ex : `Book`).
- **`schemas.py`** définit la forme des données qui entrent et sortent de
  l'API, et applique leur validation (via Pydantic), indépendamment de la
  structure de la base (ex : `BookCreate`, `BookResponse`).
- **`services.py`** contient la logique métier : créer, lire, modifier,
  supprimer une ressource, calculer une règle (ex : `compute_status`). Il
  ne connaît rien du protocole HTTP ; il dialogue uniquement avec la base
  via SQLAlchemy.

Cette séparation permet à chaque fichier de n'avoir qu'une seule
responsabilité, et de pouvoir faire évoluer une couche sans impacter
les autres.

## 8. Qu'est-ce qu'un test unitaire ? Qu'est-ce qu'une régression ?

Un **test unitaire** est un test automatisé qui vérifie qu'une fonction
ou une méthode précise se comporte comme attendu, de façon isolée, pour
un scénario donné (ex : `test_deposer_augmente_le_solde` vérifie que
`deposer()` fait bien ce qu'elle doit faire, sans dépendre du reste du
programme).

Une **régression** est un bug introduit involontairement dans du code qui
fonctionnait auparavant, généralement à l'occasion d'une modification
ultérieure. Les tests unitaires existants permettent de la détecter
rapidement : si un test qui passait avant se met à échouer après une
modification, c'est le signe d'une régression.
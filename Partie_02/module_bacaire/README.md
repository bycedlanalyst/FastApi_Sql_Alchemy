# Module bancaire

## Description

Mini-module bancaire indépendant permettant de créer un compte, déposer,
retirer de l'argent et consulter le solde, avec gestion des erreurs métier
via des exceptions personnalisées.

## Lancement des tests

Depuis le dossier `Partie_02/module_bancaire/` :

```bash
pytest
```

## Choix techniques

- **Exceptions personnalisées (`MontantInvalideError`, `SoldeInsuffisantError`)**
  plutôt que des exceptions natives Python (`ValueError`) : cela permet
  d'intercepter précisément une erreur métier bancaire sans risquer
  d'attraper par erreur d'autres `ValueError` sans rapport avec la logique
  du compte.
- **Vérification dans `__init__`** : le solde initial est contrôlé dès la
  création de l'objet, pour qu'un `CompteBancaire` invalide ne puisse
  jamais exister, même un court instant.
- **`isinstance(montant, (int, float))`** dans `deposer` et `retirer` :
  protège contre un montant non numérique (ex : une chaîne de caractères),
  conformément à la règle métier de `MontantInvalideError`.
- **`afficher()` retourne un dictionnaire** plutôt qu'un objet, pour
  faciliter l'affichage ou une éventuelle sérialisation future (JSON, etc.).

## Limites connues

- Pas de gestion de devises multiples (le solde est un simple nombre).
- Pas d'historique des transactions.

## Régression simulée

Si la méthode `retirer()` ajoutait le montant au solde au lieu de le
soustraire (par exemple `self.solde += montant` au lieu de
`self.solde -= montant`), le test vérifiant qu'un retrait valide diminue
le solde échouerait : il s'attend à un solde plus bas après l'opération,
mais obtiendrait un solde plus élevé. Le test sur `SoldeInsuffisantError`
échouerait également, car un retrait supérieur au solde ne lèverait
jamais l'exception puisque la condition `montant > self.solde` ne serait
plus jamais déclenchée de la même façon après l'ajout incorrect.# Module bancaire

## Description

Mini-module bancaire indépendant permettant de créer un compte, déposer,
retirer de l'argent et consulter le solde, avec gestion des erreurs métier
via des exceptions personnalisées.

## Lancement des tests

Depuis le dossier `Partie_02/module_bancaire/` :

```bash
pytest
```

## Choix techniques

- **Exceptions personnalisées (`MontantInvalideError`, `SoldeInsuffisantError`)**
  plutôt que des exceptions natives Python (`ValueError`) : cela permet
  d'intercepter précisément une erreur métier bancaire sans risquer
  d'attraper par erreur d'autres `ValueError` sans rapport avec la logique
  du compte.
- **Vérification dans `__init__`** : le solde initial est contrôlé dès la
  création de l'objet, pour qu'un `CompteBancaire` invalide ne puisse
  jamais exister, même un court instant.
- **`isinstance(montant, (int, float))`** dans `deposer` et `retirer` :
  protège contre un montant non numérique (ex : une chaîne de caractères),
  conformément à la règle métier de `MontantInvalideError`.
- **`afficher()` retourne un dictionnaire** plutôt qu'un objet, pour
  faciliter l'affichage ou une éventuelle sérialisation future (JSON, etc.).

## Limites connues

- Pas de gestion de devises multiples (le solde est un simple nombre).
- Pas d'historique des transactions.

## Régression simulée

Si la méthode `retirer()` ajoutait le montant au solde au lieu de le
soustraire (par exemple `self.solde += montant` au lieu de
`self.solde -= montant`), le test vérifiant qu'un retrait valide diminue
le solde échouerait : il s'attend à un solde plus bas après l'opération,
mais obtiendrait un solde plus élevé. Le test sur `SoldeInsuffisantError`
échouerait également, car un retrait supérieur au solde ne lèverait
jamais l'exception puisque la condition `montant > self.solde` ne serait
plus jamais déclenchée de la même façon après l'ajout incorrect.# Module bancaire

## Description

Mini-module bancaire indépendant permettant de créer un compte, déposer,
retirer de l'argent et consulter le solde, avec gestion des erreurs métier
via des exceptions personnalisées.

## Lancement des tests

Depuis le dossier `Partie_02/module_bancaire/` :

```bash
pytest
```

## Choix techniques

- **Exceptions personnalisées (`MontantInvalideError`, `SoldeInsuffisantError`)**
  plutôt que des exceptions natives Python (`ValueError`) : cela permet
  d'intercepter précisément une erreur métier bancaire sans risquer
  d'attraper par erreur d'autres `ValueError` sans rapport avec la logique
  du compte.
- **Vérification dans `__init__`** : le solde initial est contrôlé dès la
  création de l'objet, pour qu'un `CompteBancaire` invalide ne puisse
  jamais exister, même un court instant.
- **`isinstance(montant, (int, float))`** dans `deposer` et `retirer` :
  protège contre un montant non numérique (ex : une chaîne de caractères),
  conformément à la règle métier de `MontantInvalideError`.
- **`afficher()` retourne un dictionnaire** plutôt qu'un objet, pour
  faciliter l'affichage ou une éventuelle sérialisation future (JSON, etc.).

## Limites connues

- Pas de gestion de devises multiples (le solde est un simple nombre).
- Pas d'historique des transactions.

## Régression simulée

Si la méthode `retirer()` ajoutait le montant au solde au lieu de le
soustraire (par exemple `self.solde += montant` au lieu de
`self.solde -= montant`), le test vérifiant qu'un retrait valide diminue
le solde échouerait : il s'attend à un solde plus bas après l'opération,
mais obtiendrait un solde plus élevé. Le test sur `SoldeInsuffisantError`
échouerait également, car un retrait supérieur au solde ne lèverait
jamais l'exception puisque la condition `montant > self.solde` ne serait
plus jamais déclenchée de la même façon après l'ajout incorrect.
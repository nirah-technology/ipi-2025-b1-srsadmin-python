
# **TP Complet : Le Zoo de Pythonia**

## Objectif général

Concevoir, structurer et programmer un mini-système de gestion de zoo en Python, en appliquant les bases du langage (variables, conditions, boucles), la POO (classes, héritage, surcharge), la manipulation de fichiers, la gestion d’erreurs et l’utilisation d’un gestionnaire de contexte.

---

# Contexte du projet

Le **Zoo de Pythonia** vient d’ouvrir ses portes.
Votre mission est de créer un programme Python capable de :

* gérer un ensemble d’animaux,
* enregistrer ces animaux dans un fichier,
* charger les animaux depuis ce fichier,
* faire “parler” les animaux,
* nourrir les animaux,
* ajouter de nouveaux animaux créés par l’utilisateur,
* et exécuter tout cela via un petit menu interactif en console.

Vous devez produire **un programme propre, organisé, et structuré en plusieurs fichiers Python**.

---

# Contraintes techniques obligatoires

Votre projet **doit impérativement contenir** :

### A – **Programmation orientée objet**

* Une classe `Animal` (classe de base)
* Au moins **trois classes enfants** (`Lion`, `Monkey`, `Snake`, etc.)
* Chaque animal doit :

  * avoir un attribut `name`
  * avoir un attribut `species`
  * avoir une méthode `make_sound()`
  * avoir une méthode `feed()`

→ Chaque classe enfant doit **surcharger** `make_sound()` et `feed()`.

---

### B – **Une classe Zoo**

La classe `Zoo` doit obligatoirement :

* contenir une liste d’animaux
* fournir :

  * `add_animal(animal)`
  * `list_animals()`
  * `make_all_sounds()`
  * `feed_all()`
  * `save_to_file(filename)`
  * `load_from_file(filename)`

---

### C – **Gestion des fichiers**

* L'enregistrement des animaux se fait **dans un fichier texte JSON**.
* Le chargement doit être robuste :

  * gérer un fichier manquant,
  * gérer un fichier illisible,
  * gérer un fichier mal formaté.
* Utilisation obligatoire du **gestionnaire de contexte** :

  ```python
  with open("fichier.json", "r") as f:
      …
  ```

---

### D – **Gestion des erreurs**

Le programme doit gérer proprement :

* `FileNotFoundError`
* `JSONDecodeError`
* mauvaise saisie utilisateur (ex : choix de menu non valide)
* tout autre problème que vous jugez pertinent

---

### E – **Structures de contrôle**

Obligatoires :

* au moins une **boucle while** (menu principal)
* au moins une **boucle for** (parcours des liste d’animaux)
* conditions `if / elif / else`
* tests d’appartenance (`in`)
* une compréhension de liste est un plus bienvenue

---

### F – **Portée des variables**

* variables locales (dans les fonctions/méthodes)
* variables d’instance (attributs)
* éventuellement une variable globale **justifiée** (optionnel)

Vous devez comprendre et être capables d'expliquer la différence.

---

# Énoncé : fonctionnalités attendues

Votre programme doit proposer le menu suivant :

```
=== ZOO DE PYTHONIA ===

1. Ajouter un animal
2. Afficher tous les animaux
3. Faire parler tout le zoo
4. Nourrir tous les animaux
5. Sauvegarder le zoo dans un fichier
6. Charger le zoo depuis un fichier
7. Quitter

Votre choix : 
```

---

## 3.1 – Ajouter un animal

* L’utilisateur saisit :

  * le type (Lion / Monkey / Snake / etc.)
  * le nom
* Vous créez l’objet correspondant.
* Vous l’ajoutez au zoo via `add_animal`.

Si l’utilisateur saisit un type inconnu → afficher une erreur claire et continuer.

---

## 3.2 – Afficher tous les animaux

* Afficher la liste :

  ```
  1. Simba (Lion)
  2. Kiko (Monkey)
  3. Nagini (Snake)
  ```
* S’il n’y a aucun animal → afficher un message adapté.

---

## 3.3 – Faire parler tout le zoo

Utilise `make_all_sounds()`
Exemple :

```
Simba (Lion) : Grrraaaou !
Kiko (Monkey) : Oooh aaah !
Nagini (Snake) : Ssssss !
```

---

## 3.4 – Nourrir tous les animaux

Utilise `feed_all()`
Exemples de comportements :

* Lion → “Le lion dévore sa viande.”
* Monkey → “Le singe mange sa banane.”
* Snake → “Le serpent avale un rat entier.”

---

## 3.5 – Sauvegarder le zoo

* L’utilisateur saisit un nom de fichier.
* Le zoo écrit un fichier JSON contenant :

  ```json
  [
      {"species": "Lion", "name": "Simba"},
      {"species": "Monkey", "name": "Kiko"}
  ]
  ```
* Utilisation obligatoire du gestionnaire de contexte.

---

## 3.6 – Charger un zoo

* Lire le fichier JSON
* Pour chaque entrée :

  * recréer l’objet Python correspondant
  * l'ajouter au zoo

Gestion obligatoire des erreurs :

* fichier inexistant
* JSON incorrect
* espèce inconnue → ignorer proprement et afficher un avertissement

---

# Travail demandé (livrable)

Vous devez remettre :

## Le code source complet

* `animals.py`
* `zoo.py`
* `app.py`

## Un fichier exemple `zoo.json`

Contenant au moins 5 animaux.

## Un fichier `README.md`

Expliquant :

* comment exécuter le programme,
* l'organisation du code,
* ce que vous avez appris ou découvert.

## Une **classe enfant supplémentaire inventée par vous**

Exemples :

* `Giraffe`
* `Tiger`
* `Parrot`
* `Frog`

Avec un `make_sound()` et un `feed()` cohérents.

---

# Bonus (facultatif mais recommandé)

Pour les plus motivés :

- Ajouter une **ABC Feedable** ou un **Protocol**
- Ajouter une interface graphique (tkinter, simple)
- Ajouter des enclos, des soigneurs
- Gérer des animaux malades
- Transformer le menu en API Flask (avancé)

---

# Recommandations pédagogiques

* Commentez votre code : **précis, utile, pas excessif**.
* Respectez une indentation propre (4 espaces).
* Testez régulièrement, petit bout par petit bout.
* Concentrez-vous sur la lisibilité : des noms explicites, pas de magie.
* En cas de doute : imprimez des valeurs pour comprendre.

---

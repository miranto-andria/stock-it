# Workflow Git - Gestion de stock

## 1. Branches

- `main` : version stable et finale.
- `dev` : branche commune d'intégration et de tests.
- `feat/***` : une branche par fonctionnalité.

Exemples : `feat/produits`, `feat/entrees`, `feat/sorties`, `feat/rapports`.

Chaque membre travaille sur sa branche `feat/...`, puis propose ses modifications dans `dev` via une **Pull Request (PR)**.

## 2. Avant de commencer

```bash
git switch dev
git pull origin dev
git switch -c feat/produits
```

Remplacez `produits` par le nom de votre fonctionnalité.

## 3. Pendant le développement

```bash
git status
git add .
git commit -m "feat(produits): ajouter la gestion des produits"
git push -u origin feat/produits
```

Pour les commits suivants :

```bash
git add .
git commit -m "fix(produits): corriger la validation du formulaire"
git push
```

## 4. Convention des commits

Format : **`type(scope): description courte`**

| Type | Utilisation | Exemple |
|---|---|---|
| `feat` | Nouvelle fonctionnalité | `feat(produits): ajouter la recherche` |
| `fix` | Correction de bug | `fix(stock): empêcher les stocks négatifs` |
| `refactor` | Réorganisation sans changer le comportement | `refactor(database): simplifier la connexion` |
| `style` | Mise en forme uniquement | `style(produits): uniformiser l'indentation` |
| `docs` | Documentation | `docs(readme): expliquer le workflow Git` |
| `test` | Ajout ou modification de tests | `test(stock): tester les sorties` |
| `build` | Dépendances / build | `build: mettre à jour requirements.txt` |
| `chore` | Tâches d'entretien | `chore(git): ignorer les fichiers cache` |
| `perf` | Amélioration des performances | `perf(stock): optimiser le calcul du stock` |

**Règles :**

- Utiliser le bon type.
- Écrire une description claire et concise.
- Commencer par un verbe à l'infinitif en français, ou utiliser une formulation cohérente en anglais. Garder la même langue dans tout le projet.
- Ne pas mettre de point final.
- Faire des commits ciblés plutôt qu'un gros commit.
- Ne pas utiliser `feat` pour un simple bug.

## 5. Créer une Pull Request

1. Pousser sa branche `feat/...` sur GitHub.
2. Créer une PR de `feat/...` vers `dev`.
3. Décrire les changements et les tests effectués.
4. Faire relire par un autre membre.
5. Corriger les éventuels problèmes.
6. Fusionner après validation.

Ne jamais fusionner directement dans `main` pendant le développement.

## 6. Synchroniser sa branche

```bash
git switch dev
git pull origin dev
git switch feat/produits
git merge dev
```

En cas de conflit : résoudre les fichiers, tester, puis enregistrer et pousser les modifications.

## 7. Fichiers Qt Designer

- Chaque membre travaille sur ses propres fichiers `.ui`.
- Éviter de modifier en même temps le même fichier `.ui`.
- Conserver les noms de widgets (`objectName`) convenus.
- Après modification d'un `.ui`, régénérer le fichier Python correspondant avec `pyside6-uic`.
- Ne pas modifier manuellement les fichiers générés par `pyside6-uic`.
- Tester l'interface après chaque modification importante.

## 8. Finaliser le projet

1. Vérifier que toutes les fonctionnalités de `dev` fonctionnent.
2. Tester l'application complète et corriger les bugs.
3. Créer une PR de `dev` vers `main`.
4. Faire vérifier et valider la PR.
5. Fusionner après validation.

`main` contient alors la version stable du projet.

## 9. Règles générales

- Ne jamais développer directement sur `main`.
- Créer une branche `feat/...` par fonctionnalité.
- Faire des commits réguliers et compréhensibles.
- Synchroniser régulièrement sa branche avec `dev`.
- Ne jamais pousser de mots de passe, de secrets (`.env`) ou de fichiers temporaires.
- Communiquer avec l'équipe avant de modifier un fichier partagé.
- Tester avant de créer une PR.

---

## 10. Initialiser et peupler la base de données

### Fichiers concernés

Les fichiers suivants se trouvent dans le dossier `database/`.

| Fichier | Rôle |
|---|---|
| `schema.sql` | Contient la création de la base `stock_it` et des tables. |
| `init.py` | Crée la base et les tables en exécutant `schema.sql`. |
| `run.bat` | Lance `init.py` sous Windows. |
| `seed.py` | Génère des données de test : produits, bons d'entrée et de sortie. |
| `seed.bat` | Lance `seed.py` sous Windows. |

### Prérequis

- **XAMPP** lancé avec le module **MySQL** démarré.
- **Python 3** installé.
- Le module `mysql-connector-python` installé :

```bash
pip install mysql-connector-python
```

### Étape 1 - Créer la base et les tables

Double-cliquez sur `database/run.bat` ou exécutez cette commande depuis la racine du projet :

```bash
python database/init.py
```

Cette commande crée :

- La base `stock_it` avec le jeu de caractères `utf8mb4`.
- Les tables `Produit`, `BondeEntree` et `BondeSortie`.

### Étape 2 - Ajouter des données de test

Double-cliquez sur `database/seed.bat` ou exécutez :

```bash
python database/seed.py
```

Le script génère :

- Des produits avec des désignations variées.
- Des bons d'entrée qui alimentent le stock.
- Des bons de sortie dont les quantités ne dépassent pas le stock disponible.
- Les valeurs du champ `Stock` de chaque produit, afin de conserver la cohérence des données.

### Connexion à MySQL

Le projet utilise les paramètres par défaut de MySQL sous XAMPP.

| Paramètre | Valeur |
|---|---|
| Hôte | `127.0.0.1` |
| Port | `3306` |
| Utilisateur | `root` |
| Mot de passe | Vide par défaut |
| Base de données | `stock_it` |

Si votre serveur MySQL utilise un mot de passe ou un autre port, modifiez les constantes `DB_*` au début de `init.py` et de `seed.py`.

### Résultat attendu après `seed.py`

```text
==================================================
  RESUME DU PEUPLEMENT
==================================================
  Produits       :   25   (stock cumule : 2712)
  Bons d'entree  :   48   (quantite    : 1187)
  Bons de sortie :   42   (quantite    : 794)
==================================================
[SUCCES] Base 'stock_it' peuplee.
```

Ces nombres correspondent à un exemple de sortie attendu. Les résultats réels dépendent des données générées par le script.

### Réinitialisation de la base

Relancer `run.bat`, puis `seed.bat`, réinitialise les données selon le comportement prévu des scripts :

- `run.bat` recrée ou initialise la structure de la base.
- `seed.bat` vide d'abord les tables concernées, puis génère de nouvelles données de test.

Les scripts peuvent être relancés pour réinitialiser l'environnement de développement. **Attention :** vérifiez leur contenu avant de les exécuter sur une base contenant des données à conserver, car les données existantes peuvent être supprimées.

---

## Exemple de workflow complet

```bash
git switch dev
git pull origin dev
git switch -c feat/produits

# Développer la fonctionnalité
git add .
git commit -m "feat(produits): ajouter le formulaire produit"
git push -u origin feat/produits
```

Ensuite, créez une PR `feat/produits` vers `dev` sur GitHub. Une fois fusionnée, la fonctionnalité sera disponible pour toute l'équipe.

## Structure finale du projet

Voici la structure de dossiers recommandée pour le projet **Gestion de stock de matériels informatiques** avec Python, PySide6, Qt Designer et MySQL.

```text
gestion-stock/
├── main.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   ├── schema.sql
│   ├── init.py
│   ├── run.bat
│   ├── seed.py
│   └── seed.bat
│
├── interface/
│   ├── fenetre_principale.ui
│   ├── fenetre_produits.ui
│   ├── fenetre_entrees.ui
│   └── fenetre_sorties.ui
│
├── ui_compiled/
│   ├── __init__.py
│   ├── ui_fenetre_principale.py
│   ├── ui_fenetre_produits.py
│   ├── ui_fenetre_entrees.py
│   └── ui_fenetre_sorties.py
│
└── vues/
    ├── __init__.py
    ├── fenetre_principale.py
    ├── fenetre_produits.py
    ├── fenetre_entrees.py
    └── fenetre_sorties.py
```

### Rôle des dossiers et fichiers

| Élément | Rôle |
|---|---|
| `main.py` | Point d'entrée de l'application. |
| `database.py` | Gère la connexion à la base de données MySQL. |
| `requirements.txt` | Liste les dépendances Python du projet. |
| `database/` | Contient le script SQL, l'initialisation et les données de test. |
| `interface/` | Contient les fichiers `.ui` créés avec Qt Designer. |
| `ui_compiled/` | Contient les fichiers Python générés à partir des fichiers `.ui`. |
| `vues/` | Contient le code Python des fenêtres et la gestion des interactions. |

### Règles à respecter

- Modifier les interfaces graphiques dans `interface/` avec Qt Designer.
- Après une modification d'un fichier `.ui`, régénérer le fichier Python correspondant dans `ui_compiled/`.
- Ne pas modifier manuellement les fichiers générés dans `ui_compiled/`.
- Placer la logique des fenêtres dans `vues/`.
- Centraliser la connexion MySQL dans `database.py`.
- Conserver les scripts de création et de peuplement de la base dans `database/`.
- Ne pas versionner les environnements virtuels, les fichiers `__pycache__/` ni les fichiers Python compilés `.pyc`.

### Dépendances

Le fichier `requirements.txt` doit contenir les bibliothèques nécessaires, par exemple :

```text
PySide6
mysql-connector-python
```

Pour installer les dépendances :

```bash
pip install -r requirements.txt
```

### Compilation des interfaces

Depuis la racine du projet, exécuter les commandes suivantes après avoir créé les dossiers nécessaires :

```powershell
pyside6-uic interface/fenetre_principale.ui -o ui_compiled/ui_fenetre_principale.py
pyside6-uic interface/fenetre_produits.ui -o ui_compiled/ui_fenetre_produits.py
pyside6-uic interface/fenetre_entrees.ui -o ui_compiled/ui_fenetre_entrees.py
pyside6-uic interface/fenetre_sorties.ui -o ui_compiled/ui_fenetre_sorties.py
```

**Important :** cette structure est l'organisation cible. Les noms des classes Python générées par Qt Designer dépendent du type de formulaire utilisé. Vérifier ces noms avant de les importer dans les fichiers de `vues/`.
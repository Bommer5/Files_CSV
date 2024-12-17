# Application de Gestion de Base de Données CSV

## Description
Cette application permet de gérer des données stockées dans des fichiers CSV via une base de données SQLite. Elle propose plusieurs fonctionnalités comme l'affichage des tables, l'exportation des données, et des requêtes spécifiques sur les produits et départements.

## Fonctionnalités
1. **Afficher toutes les entités d'une table**
2. **Afficher toutes les tables de la base de données**
3. **Vérifier si un produit est vendu dans un département**
4. **Calculer la quantité totale pour un produit**
5. **Afficher le nombre de produits dans un département**
6. **Exporter les données dans un fichier CSV**
7. **Recharger la base de données** (avec des fichiers CSV)

## Prérequis
- Python 3.8+
- Bibliothèques Python :
  - `sqlite3` (intégrée)
  - `argparse`
  - `glob`
  - `os`
  - `unittest`

## Installation
1. **Clonez le projet** :
   ```bash
   git clone https://github.com/Bommer5/Files_CSV.git
   cd Files_CSV
   ```


2**Ajoutez vos fichiers CSV** :
   Placez les fichiers CSV dans le répertoire spécifié (par défaut : `info`).

## Utilisation
### Lancer l'application
Pour lancer le programme principal, exécutez la commande suivante :
```bash
python main.py
```

### Recharger la base de données
Si vous souhaitez recharger la base de données avec les fichiers CSV, utilisez l'option `--reload` :
```bash
python main.py --reload
```

### Menu principal
L'application présente un menu interactif avec les options suivantes :
- **1** : Afficher toutes les départements
- **2** : Afficher toutes les catégories
- **3** : Afficher toutes les localisations
- **4** : Afficher tous les fournisseurs
- **5** : Afficher toutes les unités
- **6** : Afficher tous les produits
- **7** : Exporter les données en fichier CSV
- **8** : Afficher toutes les tables de la base de données
- **9** : Vérifier si un produit est en stock dans un département
- **10** : Calculer la quantité totale d'un produit
- **11** : Afficher les produits par département
- **12** : Quitter




```
Le rapport HTML sera généré dans un dossier `htmlcov/`.

## Structure du projet
```plaintext
.
├── info/                 # Répertoire des fichiers CSV
├── main.py               # Fichier principal
├── db.py                 # Fonctions pour gérer la base de données
├── Menu.py               # Menu interactif
├── CSVFileProcessor.py   # Gestion de l'import/export des fichiers CSV
├── Database.py           # Gestion des connexions et requêtes SQLite
├── CrudManager.py        # Gestion des opérations CRUD
└── README.md             # Documentation
```

## Auteurs
- **Nathan** - [GitHub](https://github.com/Bommer5)

## Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

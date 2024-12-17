# Cahier des Charges - Programme de Gestion des Fichiers CSV

## 1. Objectif du Programme

Le programme a pour but de faciliter la gestion, l’importation, l’exportation, ainsi que l’analyse des données stockées dans des fichiers CSV. Il gère différentes entités liées à la gestion d'un inventaire, telles que les départements, catégories, localisations, fournisseurs, unités, et produits. Le programme permet d’afficher, manipuler et exporter ces données à travers une interface utilisateur interactive.

---

## 2. Architecture du Programme

### Classes Principales
- **Menu** : Interface utilisateur pour la gestion des fonctionnalités du programme.
- **CrudManager** : Gère les opérations CRUD (création, lecture, mise à jour, suppression) sur les données.
- **Database** : Gestion de la base de données SQLite, incluant la connexion et les opérations SQL.
- **Exporter** : Exportation des données vers des fichiers CSV.

### Structure des Données
- **Entités** : Les entités principales sont `departments`, `categories`, `locations`, `suppliers`, `units`, et `products`.
- **Relations** : Les entités sont liées par des clés primaires et étrangères dans la base de données, par exemple, chaque produit est lié à un département.

---

## 3. Fonctionnalités

### 3.1. Affichage des Données
L'utilisateur peut visualiser les informations concernant :
- Départements
- Catégories
- Localisations
- Fournisseurs
- Unités
- Produits

Chaque option permet d'afficher toutes les entrées d'une entité particulière.

### 3.2. Exportation des Données
- Le programme peut exporter les données contenues dans la base de données vers un fichier CSV formaté.

### 3.3. Statistiques et Analyses
- **Vérification de produit en stock** : Permet de vérifier si un produit est disponible dans un département.
- **Calcul de quantité totale** : Permet de calculer la quantité totale d'un produit à travers tous les départements.
- **Produits par département** : Affiche le nombre total de produits disponibles dans un département spécifique.

### 3.4. Gestion des Erreurs
Le programme gère les erreurs liées à :
- Fichiers CSV mal formatés ou manquants.
- Conflits d'intégrité des données (ex. : doublons).
- Erreurs d'exécution de requêtes SQL.

### 3.5. Extensibilité
Le programme doit permettre l'ajout facile de nouvelles entités ou de nouvelles fonctionnalités sans modifier l'architecture principale.

---

## 4. Processus Techniques

### 4.1. Importation de Données (CSV)
- Le programme parcourt un répertoire spécifique (CSV_DIRECTORY) et importe automatiquement tous les fichiers CSV présents.
- Chaque fichier CSV est analysé ligne par ligne et les données sont insérées dans la base de données SQLite.

### 4.2. Opérations CRUD
- Les entités de la base de données (produits, départements, etc.) sont créées et gérées via le `CrudManager`, garantissant que les relations entre les entités sont bien respectées.

### 4.3. Exportation CSV
- Le module `Exporter` est responsable de la création de fichiers CSV contenant toutes les données pertinentes dans un format lisible.

### 4.4. Statistiques et Calculs
- Les fonctions comme `produits_par_departements` et `calculer_total_quantite` sont implémentées à l'aide de requêtes SQL pour effectuer des agrégations efficaces.

---

## 5. Exigences SMART

1. **Importation Automatique de Données**
   - Le programme doit importer les fichiers CSV en moins de 5 secondes pour des fichiers de 1000 lignes.

2. **Gestion des Entités et Relations**
   - Les entités et leurs relations doivent être gérées avec une fidélité à 100 % et doivent permettre des requêtes SQL complexes.

3. **Exportation des Données**
   - Le programme doit exporter 100 % des données disponibles en un temps inférieur à 10 secondes pour une table de 10 000 lignes.

4. **Analyse et Requêtes Statistiques**
   - Les requêtes doivent être exécutées en moins de 1 seconde et fournir des résultats précis à 100 %.

5. **Interface Utilisateur Intuitive**
   - Le menu doit permettre l’accès à au moins 10 fonctionnalités différentes avec une réponse immédiate.

6. **Fiabilité et Gestion des Erreurs**
   - Le programme doit loguer toutes les erreurs et les afficher immédiatement (<1 seconde).

7. **Extensibilité**
   - Le programme doit permettre l’ajout de nouvelles entités ou de champs sans modifier l'architecture principale, et ce en moins de 2 heures.

---

## 6. Planning et Délai

1. **Importation des Données** : Mois 1
2. **Création des Entités et Relations** : Mois 1-2
3. **Développement de l'Exportation et des Statistiques** : Mois 3
4. **Tests et Validation** : Mois 4
5. **Mise en Production et Déploiement** : Mois 5

Le programme doit être prêt à intégrer de nouvelles fonctionnalités et à être extensible pour l'année 2024.

---

## 7. Conclusion

Ce cahier des charges définit les fonctionnalités essentielles, les exigences de performance, ainsi que les détails techniques nécessaires au bon développement d'un programme de gestion de fichiers CSV. L'outil ainsi développé permettra de gérer, analyser et exporter des données relatives à des départements, produits, et fournisseurs de manière fluide et fiable.

# Rapport : Fonctionnalités SMART du Programme de Gestion des Fichiers CSV

## 1. Importation Automatique de Données
- **Spécifique** : Le programme parcourt automatiquement un répertoire spécifique (`CSV_DIRECTORY`) pour identifier et importer tous les fichiers CSV présents.
- **Mesurable** : Le programme doit détecter et traiter 100 % des fichiers CSV dans le répertoire spécifié.
- **Atteignable** : Chaque fichier CSV est lu, et les données sont extraites ligne par ligne et insérées dans une base de données SQLite.
- **Pertinent** : Cette fonctionnalité garantit que les données sont disponibles pour les analyses et rapports.
- **Temporellement défini** : Les données doivent être importées en moins de 5 secondes pour un fichier de 1000 lignes.

---

## 2. Gestion des Entités et Relations
- **Spécifique** : Les entités comme `Produits`, `Catégories`, `Départements`, et `Fournisseurs` sont créées dans des tables SQL interconnectées. Les relations clés (exemple : `Produit` et `Département`) sont gérées via des ID uniques.
- **Mesurable** : Chaque entité est ajoutée avec 100 % de fidélité par rapport aux données du CSV.
- **Atteignable** : En utilisant SQLite, les contraintes d’unicité empêchent les doublons et garantissent la qualité des données.
- **Pertinent** : Les relations entre entités permettent des requêtes SQL complexes pour les rapports.
- **Temporellement défini** : Une requête simple ou une insertion dans la base de données doit s'exécuter en moins de 0,5 seconde.

---

## 3. Exportation des Données
- **Spécifique** : Exportation des données enrichies depuis la base de données dans un fichier CSV lisible contenant des colonnes comme `Département`, `Produit`, `Prix`, `Quantité`, etc.
- **Mesurable** : L’export doit inclure 100 % des données disponibles dans la base de données.
- **Atteignable** : Utilisation du module CSV en Python pour écrire les fichiers de manière structurée.
- **Pertinent** : Fournit une vue synthétique des données pour des besoins externes (rapports ou audits).
- **Temporellement défini** : L'exportation d'une table de 10 000 lignes ne doit pas excéder 10 secondes.

---

## 4. Analyse et Requêtes Statistiques
- **Spécifique** : Analyse des ventes par produit, département ou catégorie avec des fonctions dédiées (exemple : `produits_par_departements` ou `calculer_total_quantite`).
- **Mesurable** : Les requêtes doivent retourner les résultats précis avec 100 % de précision.
- **Atteignable** : Utilisation de SQL pour effectuer des agrégations efficaces.
- **Pertinent** : Permet d’extraire des insights comme les produits les plus vendus par département.
- **Temporellement défini** : Chaque requête doit s'exécuter en moins de 1 seconde.

---

## 5. Interface Utilisateur Intuitive
- **Spécifique** : Le programme propose un menu interactif permettant de naviguer entre les différentes fonctionnalités (CRUD, exportation, statistiques).
- **Mesurable** : Le menu doit proposer au moins 10 fonctionnalités différentes.
- **Atteignable** : Utilisation de boucles et conditions pour gérer les entrées utilisateur.
- **Pertinent** : Facilite l’utilisation pour des utilisateurs non techniques.
- **Temporellement défini** : La navigation entre les options doit être fluide, avec une réponse immédiate (<0,5 seconde).

---

## 6. Fiabilité et Gestion des Erreurs
- **Spécifique** : Le programme gère les erreurs comme les fichiers manquants, les colonnes mal formées, ou les conflits de base de données (ex. contrainte d’unicité).
- **Mesurable** : Toutes les erreurs doivent être loguées et affichées à l’utilisateur.
- **Atteignable** : En utilisant des blocs `try-except`, les erreurs sont gérées sans arrêt brutal du programme.
- **Pertinent** : Améliore la robustesse et l’expérience utilisateur.
- **Temporellement défini** : Les erreurs doivent être détectées et signalées immédiatement (<1 seconde).

---

## 7. Extensibilité
- **Spécifique** : Le programme est conçu pour permettre l’ajout futur de nouvelles entités ou colonnes dans la base de données sans modifier l’existant.
- **Mesurable** : Une nouvelle fonctionnalité (ex. : ajout d’un champ "Pays" pour les fournisseurs) peut être implémentée en moins de 2 heures.
- **Atteignable** : Grâce à une structure modulaire avec des classes comme `Database`, `CSVFileProcessor`, et `CrudManager`.
- **Pertinent** : Assure la pérennité du projet.
- **Temporellement défini** : Doit être prêt à intégrer des changements en 2024.

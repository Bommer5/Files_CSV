class CrudManager:
    """
    Classe pour gérer les opérations CRUD avancées sur la base de données.
    Fournit des méthodes pour lister, vérifier et calculer des informations sur les données.
    """

    def __init__(self, database):
        """
        Initialise une instance de CrudManager.

        Args:
            database (Database): Instance de la classe Database pour effectuer des requêtes.
        """
        self.database = database

    def afficher_toutes_entites(self, table_name: str) -> None:
        """
        Affiche toutes les entrées d'une table spécifique.

        Args:
            table_name (str): Nom de la table à afficher.
        """
        query = f"SELECT * FROM {table_name}"
        try:
            results = self.database.fetch_all(query)
            if results:
                print(f"Liste des entrées dans la table '{table_name}':")
                for row in results:
                    print(row)
            else:
                print(f"Aucune entrée trouvée dans la table '{table_name}'.")
        except Exception as e:
            print(f"Erreur lors de l'affichage des entrées : {e}")

    def afficher_toutes_les_tables(self) -> None:
        """
        Affiche le contenu de toutes les tables de la base de données.
        """
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        try:
            tables = self.database.fetch_all(query)
            if tables:
                for table in tables:
                    table_name = table[0]
                    print(f"\n=== Contenu de la table '{table_name}' ===")
                    self.afficher_toutes_entites(table_name)
            else:
                print("Aucune table trouvée dans la base de données.")
        except Exception as e:
            print(f"Erreur lors de la récupération des tables : {e}")

    def verifier_produit_vendu(self, produit: str, departement: str) -> None:
        """
        Vérifie si un produit est vendu dans un département spécifique.

        Args:
            produit (str): Nom du produit à vérifier.
            departement (str): Nom du département.
        """
        query = '''
            SELECT 
                COUNT(*) 
            FROM data
            LEFT JOIN products p ON p.product_id = data.product_id
            LEFT JOIN departments d ON d.department_id = data.department_id
            WHERE p.product_name = ? AND d.department_name = ?
        '''
        try:
            count = self.database.fetch_all(query, (produit, departement))[0][0]
            if count > 0:
                print(f"Le produit '{produit}' est en stock dans le département '{departement}'.")
            else:
                print(f"Le produit '{produit}' n'est pas en stock dans le département '{departement}'.")
        except Exception as e:
            print(f"Erreur lors de la vérification du produit vendu : {e}")

    def calculer_total_quantite(self, produit: str) -> int:
        """
        Calcule le total des quantités pour un produit spécifique.

        Args:
            produit (str): Nom du produit.

        Returns:
            int: Le total des quantités.
        """
        query = """
            SELECT SUM(quantity) 
            FROM data
            LEFT JOIN products p ON p.product_id = data.product_id
            WHERE p.product_name = ?
        """
        try:
            result = self.database.fetch_all(query, (produit,))
            total = result[0][0] if result and result[0][0] else 0
            print(f"Le total des quantités pour le produit '{produit}' est : {total}")
            return total
        except Exception as e:
            print(f"Erreur lors du calcul du total des quantités : {e}")
            return 0

    def produits_par_departements(self, departement: str) -> int:
        """
        Calcule le nombre total de produits dans un département spécifique.

        Args:
            departement (str): Nom du département.

        Returns:
            int: Nombre total de produits.
        """
        query = """
            SELECT DISTINCT COUNT(product_id)
            FROM data
            LEFT JOIN departments d ON d.department_id = data.department_id
            WHERE d.department_name = ?
        """
        try:
            result = self.database.fetch_all(query, (departement,))
            total = result[0][0] if result and result[0][0] else 0
            print(f"Le total des produits pour le département '{departement}' est : {total}")
            return total
        except Exception as e:
            print(f"Erreur lors du calcul du total des produits : {e}")
            return 0

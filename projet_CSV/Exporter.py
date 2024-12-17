import csv
import sqlite3
from variable import OUTPUT_FILE
from CSVFileProcessor import CSVFileProcessor

class Exporter:
    """
    Classe responsable de l'exportation des données depuis la base de données vers un fichier CSV.
    """

    def __init__(self, database):
        """
        Initialise une instance de la classe Exporter.

        Args:
            database (Database): Instance de la classe Database utilisée pour se connecter à la base de données.
        """
        self.database = database

    def exporter_donnees_vers_csv(self):
        """
        Exporte les données depuis la base de données SQLite vers un fichier CSV.

        Crée un fichier CSV contenant les informations des tables liées à `data` et leurs associations :
        département, produit, catégorie, prix, quantité, date d'achat, localisation, fournisseur et unité.

        Raises:
            Exception: En cas d'erreur lors de l'exécution de la requête ou de l'écriture du fichier.
        """
        conn = sqlite3.connect(self.database.db_name)
        cursor = conn.cursor()

        try:
            # Requête SQL pour récupérer les données
            query = '''
                SELECT 
                    d.department_name AS "Départment",
                    p.product_name AS "Produit",
                    c.category_name AS "Catégorie",
                    data.price AS "Prix",
                    data.quantity AS "Quantité",
                    data.purchase_date AS "Date d'achat",
                    l.location_name AS "Localisation",
                    s.supplier_name AS "Fournisseur",
                    u.unit_name AS "Unité"
                FROM data
                LEFT JOIN departments d ON d.department_id = data.department_id
                LEFT JOIN products p ON p.product_id = data.product_id
                LEFT JOIN categories c ON c.category_id = data.category_id
                LEFT JOIN locations l ON l.location_id = data.location_id
                LEFT JOIN suppliers s ON s.supplier_id = data.supplier_id
                LEFT JOIN units u ON u.unit_id = data.unit_id
            '''
            cursor.execute(query)

            # Récupérer les données et les en-têtes
            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description]

            # Écriture des données dans le fichier CSV
            with open(OUTPUT_FILE, mode="w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(headers)  # Écrire les en-têtes
                writer.writerows(rows)  # Écrire les lignes

            print(f"✅ Données exportées avec succès dans le fichier : {OUTPUT_FILE}")

        except Exception as e:
            print(f"❌ Une erreur est survenue lors de l'exportation du fichier CSV : {e}")

        finally:
            # Fermer la connexion à la base de données
            conn.close()

import glob
import os
import sqlite3
import csv
from projet_CSV import variable
from variable import *
import db

COLUMN_PRODUCT_NAME = 0
COLUMN_CATEGORY = 1
COLUMN_DEPARTMENT = 2
COLUMN_QUANTITY = 3
COLUMN_PURCHASE_DATE = 4
COLUMN_PRICE = 5
COLUMN_SUPPLIER = 6
COLUMN_UNIT = 7
COLUMN_LOCATION = 8
class CSVFileProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.header = None
        self.data = []
    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                self.header = next(reader, None)  # Fetch header, or None if empty
                self.data = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    def get_header(self):
        return self.header
    def get_data(self):
        return self.data
def process_csv_file(file_path):
    csv_processor = CSVFileProcessor(file_path)
    csv_processor.read_file()
    print(f"The file {csv_processor.filename} has the header: {csv_processor.get_header()}")
    for row in csv_processor.get_data():
        # Extract values from the row
        department = row[COLUMN_DEPARTMENT]
        product = row[COLUMN_PRODUCT_NAME]
        quantity = int(row[COLUMN_QUANTITY])
        price = row[COLUMN_PRICE][1:]
        category = row[COLUMN_CATEGORY]
        supplier = row[COLUMN_SUPPLIER]
        purchase_date = row[COLUMN_PURCHASE_DATE]
        unit = row[COLUMN_UNIT]
        location = row[COLUMN_LOCATION]
        print(
            f"Processing data for Department: {department}, Product: {product}, Quantity: {quantity}, Price: {price}, Category: {category}, Purchase Date: {purchase_date}, Supplier: {supplier}, Unit: {unit}, Location: {location}"
        )
        # Insert or fetch IDs and add data to the database
        department_id = db.ajouter_departement(department)
        product_id = db.ajouter_produit(product)
        category_id = db.ajouter_catégories(category)
        supplier_id = db.ajouter_supplier(supplier)
        unit_id = db.ajouter_unit(unit)
        location_id = db.ajouter_location(location)
        data_id = db.ajouter_data(department_id, product_id, category_id, price, quantity, purchase_date,supplier_id,unit_id,location_id)
        print(
            f"Added Data: Department({department_id}), Product({product_id}), Category({category_id}), Data({data_id})"
        )

class Database:
    """Gestion de la connexion et des opérations CRUD simples."""

    def __init__(self, db_name="CSV.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def execute_query(self, query, params=None):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
        finally:
            conn.close()

    def fetch_all(self, query, params=None):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
        finally:
            conn.close()


class Exporter:
    """Classe dédiée à l'exportation des données vers un fichier CSV."""

    def __init__(self, database: Database):
        self.database = database

    def exporter_donnees_vers_csv(self):
        conn = sqlite3.connect(self.database.db_name)
        cursor = conn.cursor()

        try:
            cursor.execute('''
                SELECT 
                    d.departement_nom AS "Département",
                    p.produit_nom AS "Produit",
                    c.catégorie_nom AS "Catégorie",
                    data.prix AS "Prix",
                    data.quantité AS "Quantité",
                    data.purchase_date AS "Date d'achat",
                    l.location_nom AS "Localisation",
                    s.supplier_nom AS "Fournisseur",
                    u.unit_nom AS "Unité"
                FROM data
                LEFT JOIN departements d ON d.departement_id = data.departement_id
                LEFT JOIN produits p ON p.produit_id = data.produit_id
                LEFT JOIN catégories c ON c.catégorie_id = data.catégorie_id
                LEFT JOIN locations l ON l.location_id = data.location_id
                LEFT JOIN suppliers s ON s.supplier_id = data.supplier_id
                LEFT JOIN units u ON u.unit_id = data.unit_id
            ''')

            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description]

            with open(OUTPUT_FILE, mode="w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(headers)  # Écriture des en-têtes
                writer.writerows(rows)  # Écriture des données

            print(f"✅ Données exportées avec succès dans le fichier : {OUTPUT_FILE}")

        except Exception as e:
            print(f"❌ Une erreur est survenue lors de l'exportation du fichier CSV : {e}")
        finally:
            conn.close()


class CrudManager:
    """Classe pour gérer les opérations CRUD liées aux entités."""

    def __init__(self, database: Database):
        self.database = database

    def afficher_toutes_entites(self, table_name):
        query = f"SELECT * FROM {table_name}"
        results = self.database.fetch_all(query)
        if results:
            print(f"Liste des entrées dans la table '{table_name}':")
            for row in results:
                print(row)
        else:
            print(f"Aucune entrée trouvée dans la table '{table_name}'.")

    def afficher_toutes_les_tables(self):
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

    def verifier_produit_vendu(self, produit, departement):
        query = '''
            SELECT 
                COUNT(*) 
            FROM data
            LEFT JOIN produits p ON p.produit_id = data.produit_id
            LEFT JOIN departements d ON d.departement_id = data.departement_id
            WHERE p.produit_nom = ? AND d.departement_nom = ?
        '''
        count = self.database.fetch_all(query, (produit, departement))[0][0]
        if count > 0:
            print(f"Le produit '{produit}' a été vendu dans le département '{departement}'.")
        else:
            print(f"Le produit '{produit}' n'a pas été vendu dans le département '{departement}'.")

    def calculer_total_quantite(self, produit):
        query = """
        SELECT sum(quantité) 
        FROM data
        LEFT JOIN produits p ON p.produit_id = data.produit_id
        WHERE p.produit_nom = ?
        """
        try:
            result = self.database.fetch_all(query, (produit,))
            total = result[0][0] if result and result[0][0] else 0
            print(f"Le total des quantités pour le produit '{produit}' est : {total}")
            return total
        except Exception as e:
            print(f"Erreur lors du calcul du total des quantités : {e}")
            return 0

    def produits_par_departements(self,departement):


        query = """
        SELECT DISTINCT count(produit_id)
        FROM data
        /*LEFT JOIN produits p ON p.produit_id = data.produit_id*/
        LEFT JOIN departements d ON d.departement_id = data.departement_id
        WHERE departement_nom = ?
        """
        try :
            result = self.database.fetch_all(query, (departement,))
            tot = result[0][0] if result and result[0][0] else 0
            print(f"le total des produits pour le departement {departement} est : {tot}")
            return tot
        except Exception as e:
            print(f"Erreur lors du calcul du total des produits : {e}")
            return 0
    
    



class Menu:
    """Classe pour gérer le menu principal."""

    def __init__(self):
        self.database = Database()
        self.crud_manager = CrudManager(self.database)
        self.exporter = Exporter(self.database)

    def afficher_menu(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Afficher tous les départements")
            print("2. Afficher toutes les catégories")
            print("3. Afficher toutes les localisations")
            print("4. Afficher tous les suppliers")
            print("5. Afficher tous les units")
            print("6. Afficher tous les produits")
            print("7. Exporter les données dans un fichier CSV")
            print("8. Afficher toutes les tables")
            print("9. verifier produit vendu dans un département")
            print("10. calculer total quantite pour un produit")
            print("11. produits par departements")
            print("12. Quitter")

            choix = input("Entrez votre choix : ")
            if choix == "1":
                self.crud_manager.afficher_toutes_entites('departements')
            elif choix == "2":
                self.crud_manager.afficher_toutes_entites('catégories')
            elif choix == "3":
                self.crud_manager.afficher_toutes_entites('locations')
            elif choix == "4" :
                self.crud_manager.afficher_toutes_entites('suppliers')
            elif choix == "5":
                self.crud_manager.afficher_toutes_entites('units')
            elif choix == "6":
                self.crud_manager.afficher_toutes_entites('produits')
            elif choix == "7":
                self.exporter.exporter_donnees_vers_csv()
            elif choix == "8":
                self.crud_manager.afficher_toutes_les_tables()
            elif choix == "9":
                self.crud_manager.afficher_toutes_entites('departements')
                dep = input("nom du departement :")
                self.crud_manager.afficher_toutes_entites('produits')
                pro = input("nom du produit :")
                self.crud_manager.verifier_produit_vendu(pro, dep)
            elif choix == "10":
                self.crud_manager.afficher_toutes_entites('produits')
                pro = input("nom du produit :")
                self.crud_manager.calculer_total_quantite(pro)
            elif choix == "11":
                self.crud_manager.afficher_toutes_entites('departements')
                dep1 = input("nom du departement :")
                self.crud_manager.produits_par_departements(dep1)
            elif choix == "12":
                print("Merci d'avoir utilisé le programme. À bientôt !")
                break

            else:
                print("Choix invalide. Veuillez réessayer.")





if __name__ == "__main__":
    db.creer_base_de_donnees()
    csv_files = glob.glob(os.path.join(variable.CSV_DIRECTORY, "*.csv"))
    for file_path in csv_files:
        process_csv_file(file_path)
    menu = Menu()
    menu.afficher_menu()
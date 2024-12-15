import sqlite3
import csv
from variable import *


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

    def ajouter_entite(self, table_name, column_name, value):
        query = f"INSERT INTO {table_name} ({column_name}) VALUES (?)"
        self.database.execute_query(query, (value,))
        print(f"✅ {column_name} '{value}' ajouté avec succès dans la table '{table_name}'.")

    def afficher_toutes_entites(self, table_name):
        query = f"SELECT * FROM {table_name}"
        results = self.database.fetch_all(query)
        if results:
            print(f"Liste des entrées dans la table '{table_name}':")
            for row in results:
                print(row)
        else:
            print(f"Aucune entrée trouvée dans la table '{table_name}'.")

    def modifier_nom_entite(self, table_name, column_name, entity_id, nouveau_nom):
        query = f"UPDATE {table_name} SET {column_name} = ? WHERE {table_name[:-1]}_id = ?"
        self.database.execute_query(query, (nouveau_nom, entity_id))
        print(f"✅ Nom mis à jour dans la table '{table_name}'. ID : {entity_id}, Nouveau nom : {nouveau_nom}")

    def supprimer_entite(self, table_name, entity_id):
        query = f"DELETE FROM {table_name} WHERE {table_name[:-1]}_id = ?"
        self.database.execute_query(query, (entity_id,))
        print(f"✅ Entrée avec ID {entity_id} supprimée dans la table '{table_name}'.")


class Menu:
    """Classe pour gérer le menu principal."""

    def __init__(self):
        self.database = Database()
        self.crud_manager = CrudManager(self.database)
        self.exporter = Exporter(self.database)

    def afficher_menu(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Ajouter un département")
            print("2. Ajouter un produit")
            print("3. Ajouter une catégorie")
            print("4. Ajouter une localisation")
            print("5. Afficher tous les départements")
            print("6. Afficher toutes les catégories")
            print("7. Afficher toutes les localisations")
            print("8. Modifier un produit (nom)")
            print("9. Supprimer une catégorie")
            print("10. Exporter les données dans un fichier CSV")
            print("11. Quitter")

            choix = input("Entrez votre choix : ")

            if choix == "1":
                nom = input("Entrez le nom du département : ")
                self.crud_manager.ajouter_entite('departements', 'departement_nom', nom)
            elif choix == "2":
                nom = input("Entrez le nom du produit : ")
                self.crud_manager.ajouter_entite('produits', 'produit_nom', nom)
            elif choix == "3":
                nom = input("Entrez le nom de la catégorie : ")
                self.crud_manager.ajouter_entite('catégories', 'catégorie_nom', nom)
            elif choix == "4":
                nom = input("Entrez le nom de la localisation : ")
                self.crud_manager.ajouter_entite('locations', 'location_nom', nom)
            elif choix == "5":
                self.crud_manager.afficher_toutes_entites('departements')
            elif choix == "6":
                self.crud_manager.afficher_toutes_entites('catégories')
            elif choix == "7":
                self.crud_manager.afficher_toutes_entites('locations')
            elif choix == "8":
                produit_id = input("Entrez l'ID du produit à modifier : ")
                nouveau_nom = input("Entrez le nouveau nom du produit : ")
                self.crud_manager.modifier_nom_entite('produits', 'produit_nom', produit_id, nouveau_nom)
            elif choix == "9":
                categorie_id = input("Entrez l'ID de la catégorie à supprimer : ")
                self.crud_manager.supprimer_entite('catégories', categorie_id)
            elif choix == "10":
                self.exporter.exporter_donnees_vers_csv()
            elif choix == "11":
                print("Merci d'avoir utilisé le programme. À bientôt !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    menu = Menu()
    menu.afficher_menu()

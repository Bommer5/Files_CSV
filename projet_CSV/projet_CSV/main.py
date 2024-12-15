import csv
import variable
import db


class file_CSV:
    def __init__(self, filename):
        self.filename = filename
        self.header = None
        self.data = []

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                self.header = next(reader, None)  # Récupère l'entête, ou None si vide
                self.data = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_header(self):
        return self.header

    def get_data(self):
        return self.data

# Effectuer la lecture des fichiers CSV et remplir les tables dans la base de données
if __name__ == "__main__":
    db.creer_base_de_donnees()
    for file in variable.CSV_DIRECTORY:
        content = file_CSV(file)
        content.read_file()  # Lire les données du fichier CSV
        print(f"The file {content.filename} has the header: {content.get_header()}")

        # Insérer les données ligne par ligne
        for row in content.get_data():
            # Lire les valeurs depuis la ligne
            departement = row[0]  # Colonne "departement_nom"
            produit = row[1]  # Colonne "product_name"
            quantité = int(row[2])  # Colonne "quantity"
            prix = float(row[3])  # Colonne "unit_price"
            catégorie = row[4]  # Colonne "category"

            # Étape 1 : Ajouter ou récupérer l'ID du département
            departement_id = db.ajouter_departement(departement)

            # Étape 2 : Ajouter ou récupérer l'ID du produit
            produit_id = db.ajouter_produit(produit, prix, quantité)

            # Étape 3 : Ajouter ou récupérer l'ID de la catégorie
            catégorie_id = db.ajouter_catégories(catégorie)

            # Étape 4 : Ajouter les informations dans la table `data`
            data_id = db.ajouter_data(departement_id, produit_id, catégorie_id)

            print(
                f"Ajout des données : Département({departement_id}), Produit({produit_id}), Catégorie({catégorie_id}), Data({data_id})")



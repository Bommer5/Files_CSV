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

    def close(self):
        # Rien à fermer ici car 'with open()' gère déjà la fermeture du fichier
        pass


for i in variable.CSV_DIRECTORY :
    test = file_CSV(i)
    test.read_file()  # Lire les données du fichier CSV
    print(f"The file {test.filename} has the header: {test.get_header()}")
    for row in test.get_data():
            print(row)  # Afficher chaque ligne de données
    test.close()

import glob
import os
import argparse

from db import *
from variable import *
from Menu import *
from CSVFileProcessor import CSVFileProcessor
from Database import Database

def recharger_base_de_donnees():
    create_database()
    # Réimportation des fichiers CSV
    csv_files = glob.glob(os.path.join(CSV_DIRECTORY, "*.csv"))
    for file_path in csv_files:
        CSVFileProcessor.process_csv_file(file_path)

if __name__ == "__main__":
    # Initialisation d'argparse pour gérer les options en ligne de commande
    parser = argparse.ArgumentParser(description="Application de gestion de base de données CSV.")
    parser.add_argument('--reload', action='store_true', help="Recharger la base de données avant d'exécuter le programme")
    parser.add_argument('--help', action='store_true', help="Help")
    args = parser.parse_args()

    # Si l'option --reload est passée, on recharge la base de données
    if args.help :
        print("voir le fichier feature")
    if args.reload:
        recharger_base_de_donnees()
    print(args.reload)
    # Démarrage du menu

    menu = Menu()
    menu.afficher_menu()

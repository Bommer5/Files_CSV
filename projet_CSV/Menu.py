from CrudManager import *
from Database import *
from Exporter import *

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
            print("9. Vérifier produit stocké dans un département")
            print("10. Calculer total quantité pour un produit")
            print("11. Produits par départements")
            print("12. Quitter")

            choix = input("Entrez votre choix : ")
            if choix == "1":
                self.crud_manager.afficher_toutes_entites('departments')
            elif choix == "2":
                self.crud_manager.afficher_toutes_entites('categories')
            elif choix == "3":
                self.crud_manager.afficher_toutes_entites('locations')
            elif choix == "4":
                self.crud_manager.afficher_toutes_entites('suppliers')
            elif choix == "5":
                self.crud_manager.afficher_toutes_entites('units')
            elif choix == "6":
                self.crud_manager.afficher_toutes_entites('products')
            elif choix == "7":
                self.exporter.exporter_donnees_vers_csv()
            elif choix == "8":
                self.crud_manager.afficher_toutes_les_tables()
            elif choix == "9":
                # Demande de nom de département et produit, avec validation
                self._verifier_produit_vendu()
            elif choix == "10":
                # Demande du produit et calcul de la quantité, avec validation
                self._calculer_total_quantite()
            elif choix == "11":
                # Demande du département et calcul du nombre de produits, avec validation
                self._produits_par_departements()
            elif choix == "12":
                print("Merci d'avoir utilisé le programme. À bientôt !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    def _verifier_produit_vendu(self):
        """
        Demande un département et un produit à l'utilisateur et vérifie si le produit est en stock dans le département.
        """
        self.crud_manager.afficher_toutes_entites('departments')
        dep = input("Entrez le nom du département : ").strip()
        self.crud_manager.afficher_toutes_entites('products')
        pro = input("Entrez le nom du produit : ").strip()

        if not dep or not pro:
            print("Le nom du département ou du produit est invalide.")
            return

        # Vérification si le produit est stocké dans le département
        self.crud_manager.verifier_produit_vendu(pro, dep)

    def _calculer_total_quantite(self):
        """
        Demande le nom d'un produit à l'utilisateur et calcule la quantité totale disponible.
        """
        self.crud_manager.afficher_toutes_entites('products')
        pro = input("Entrez le nom du produit : ").strip()

        if not pro:
            print("Le nom du produit est invalide.")
            return

        # Calculer le total des quantités pour ce produit
        self.crud_manager.calculer_total_quantite(pro)

    def _produits_par_departements(self):
        """
        Demande un département à l'utilisateur et calcule le nombre de produits dans ce département.
        """
        self.crud_manager.afficher_toutes_entites('departements')
        dep1 = input("Entrez le nom du département : ").strip()

        if not dep1:
            print("Le nom du département est invalide.")
            return

        # Calculer le nombre de produits dans ce département
        self.crud_manager.produits_par_departements(dep1)

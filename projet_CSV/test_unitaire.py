import unittest
from unittest.mock import patch, MagicMock
from Menu import Menu
from CrudManager import CrudManager
from Exporter import Exporter
from Database import Database
from main import recharger_base_de_donnees
import os

class TestMenu(unittest.TestCase):

    def setUp(self):
        # On crée un mock pour Database, CrudManager, et Exporter
        self.mock_database = MagicMock(Database)
        self.mock_crud_manager = MagicMock(CrudManager)
        self.mock_exporter = MagicMock(Exporter)
        # On crée une instance de Menu
        self.menu = Menu()

    @patch('builtins.input', side_effect=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
    def test_afficher_menu(self, mock_input):
        # On simule la méthode afficher_menu qui gère les choix de menu
        with patch.object(self.menu, 'crud_manager', self.mock_crud_manager):
            self.menu.afficher_menu()

        # Vérification des appels à afficher_toutes_entites
        self.mock_crud_manager.afficher_toutes_entites.assert_any_call('departments')
        self.mock_crud_manager.afficher_toutes_entites.assert_any_call('categories')
        self.mock_crud_manager.afficher_toutes_entites.assert_any_call('locations')
        self.mock_crud_manager.afficher_toutes_entites.assert_any_call('suppliers')
        self.mock_crud_manager.afficher_toutes_entites.assert_any_call('units')
        self.mock_crud_manager.afficher_toutes_entites.assert_any_call('product')
        self.mock_crud_manager.afficher_toutes_entites.assert_any_call('departments')
        self.mock_crud_manager.afficher_toutes_entites.assert_any_call('products')

        # Vérification du passage des méthodes comme 'afficher_toutes_entites', 'exporter_donnees_vers_csv', etc.
        self.mock_crud_manager.afficher_toutes_les_tables.assert_called_once()
        self.mock_exporter.exporter_donnees_vers_csv.assert_called_once()

    @patch('builtins.input', side_effect=["1", "Département A", "Produit X"])
    def test_verifier_produit_vendu(self, mock_input):
        self.menu._verifier_produit_vendu()
        self.mock_crud_manager.verifier_produit_vendu.assert_called_once_with("Produit X", "Département A")

    @patch('builtins.input', side_effect=["Produit Y"])
    def test_calculer_total_quantite(self, mock_input):
        self.menu._calculer_total_quantite()
        self.mock_crud_manager.calculer_total_quantite.assert_called_once_with("Produit Y")

    @patch('builtins.input', side_effect=["Département A"])
    def test_produits_par_departements(self, mock_input):
        self.menu._produits_par_departements()
        self.mock_crud_manager.produits_par_departements.assert_called_once_with("Département A")
class TestCrudManager(unittest.TestCase):

    def setUp(self):
        self.mock_database = MagicMock(Database)
        self.crud_manager = CrudManager(self.mock_database)

    def test_afficher_toutes_entites(self):
        # Simuler le résultat de la méthode fetch_all
        self.mock_database.fetch_all.return_value = [("Test1",), ("Test2",)]
        with patch('builtins.print') as mock_print:
            self.crud_manager.afficher_toutes_entites('departements')
            mock_print.assert_any_call("Liste des entrées dans la table 'departements':")
            mock_print.assert_any_call(('Test1',))
            mock_print.assert_any_call(('Test2',))

    def test_afficher_toutes_les_tables(self):
        # Simuler le résultat de la méthode fetch_all
        self.mock_database.fetch_all.return_value = [("departements",), ("produits",)]
        with patch('builtins.print') as mock_print:
            self.crud_manager.afficher_toutes_les_tables()
            mock_print.assert_any_call("\n=== Contenu de la table 'departements' ===")
            mock_print.assert_any_call("\n=== Contenu de la table 'produits' ===")

    def test_verifier_produit_vendu(self):
        self.mock_database.fetch_all.return_value = [(1,)]
        with patch('builtins.print') as mock_print:
            self.crud_manager.verifier_produit_vendu('Produit X', 'Département A')
            mock_print.assert_called_once_with("Le produit 'Produit X' est en stock dans le département 'Département A'.")

    def test_calculer_total_quantite(self):
        self.mock_database.fetch_all.return_value = [(10,)]
        with patch('builtins.print') as mock_print:
            total = self.crud_manager.calculer_total_quantite('Produit Y')
            mock_print.assert_called_once_with("Le total des quantités pour le produit 'Produit Y' est : 10")
            self.assertEqual(total, 10)

    def test_produits_par_departements(self):
        self.mock_database.fetch_all.return_value = [(5,)]
        with patch('builtins.print') as mock_print:
            total = self.crud_manager.produits_par_departements('Département A')
            mock_print.assert_called_once_with("Le total des produits pour le département 'Département A' est : 5")
            self.assertEqual(total, 5)
class TestExporter(unittest.TestCase):

    def setUp(self):
        self.mock_database = MagicMock(Database)
        self.exporter = Exporter(self.mock_database)

    def test_exporter_donnees_vers_csv(self):
        # Simuler la méthode fetch_all pour récupérer des données
        self.mock_database.fetch_all.return_value = [("Test1",), ("Test2",)]
        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            self.exporter.exporter_donnees_vers_csv()
            mock_file.assert_called_once_with('data.csv', 'w', newline='')
            handle = mock_file()
            handle.write.assert_any_call("Test1,Test2\n")
            handle.write.assert_any_call("Test2,Test2\n")
class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database = MagicMock(Database)

    def test_fetch_all(self):
        # Simuler le retour de fetch_all
        self.database.fetch_all.return_value = [("Test1",), ("Test2",)]
        result = self.database.fetch_all("SELECT * FROM departements")
        self.assertEqual(result, [("Test1",), ("Test2",)])

    def test_execute_query(self):
        # Simuler l'exécution d'une requête
        self.database.execute_query.return_value = None
        self.database.execute_query("INSERT INTO departements (name) VALUES (?)", ("Test",))
        self.database.execute_query.assert_called_once_with("INSERT INTO departements (name) VALUES (?)", ("Test",))


class TestRechargerBaseDeDonnees(unittest.TestCase):

    @patch('votre_module.create_database')  # Mock pour create_database
    @patch('glob.glob')  # Mock pour glob.glob qui récupère les fichiers CSV
    @patch('votre_module.CSVFileProcessor.process_csv_file')  # Mock pour le traitement des fichiers CSV
    def test_recharger_base_de_donnees(self, mock_process_csv_file, mock_glob, mock_create_database):
        # Simuler que glob retourne une liste de fichiers CSV
        mock_glob.return_value = ['file1.csv', 'file2.csv']

        # Appel de la fonction recharger_base_de_donnees
        recharger_base_de_donnees()

        # Vérifier que create_database a été appelé une fois
        mock_create_database.assert_called_once()

        # Vérifier que glob.glob a récupéré les fichiers CSV
        mock_glob.assert_called_once_with(os.path.join('CSV_DIRECTORY', "*.csv"))

        # Vérifier que process_csv_file a été appelé pour chaque fichier CSV
        mock_process_csv_file.assert_any_call('file1.csv')
        mock_process_csv_file.assert_any_call('file2.csv')


if __name__ == '__main__':
    unittest.main()

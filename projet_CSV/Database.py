import sqlite3
from typing import Any, List, Optional, Tuple

class Database:
    """
    Gestion de la connexion et des opérations CRUD simples sur une base SQLite.

    Attributes:
        db_name (str): Nom du fichier de la base de données SQLite.
    """

    def __init__(self, db_name: str = "CSV.db"):
        """
        Initialise une instance de la classe Database.

        Args:
            db_name (str): Nom du fichier de la base de données SQLite. Par défaut, "CSV.db".
        """
        self.db_name = db_name

    def connect(self) -> sqlite3.Connection:
        """
        Établit une connexion à la base de données SQLite.

        Returns:
            sqlite3.Connection: L'objet de connexion à la base de données.

        Raises:
            sqlite3.Error: En cas d'échec de la connexion à la base de données.
        """
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            raise sqlite3.Error(f"Erreur lors de la connexion à la base de données : {e}")

    def execute_query(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> Optional[int]:
        """
        Exécute une requête SQL (INSERT, UPDATE, DELETE) et valide les changements.

        Args:
            query (str): La requête SQL à exécuter.
            params (Optional[Tuple[Any, ...]]): Les paramètres pour la requête (si nécessaire).

        Returns:
            Optional[int]: L'ID de la dernière ligne insérée (si applicable), sinon None.

        Raises:
            sqlite3.Error: En cas d'échec de l'exécution de la requête.
        """
        try:
            conn = self.connect()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            last_row_id = cursor.lastrowid
            return last_row_id
        except sqlite3.Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
        finally:
            conn.close()

    def fetch_all(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Tuple[Any, ...]]:
        """
        Exécute une requête SELECT et retourne les résultats.

        Args:
            query (str): La requête SQL à exécuter.
            params (Optional[Tuple[Any, ...]]): Les paramètres pour la requête (si nécessaire).

        Returns:
            List[Tuple[Any, ...]]: Une liste des résultats sous forme de tuples.

        Raises:
            sqlite3.Error: En cas d'échec de l'exécution de la requête.
        """
        try:
            conn = self.connect()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
            return []
        finally:
            conn.close()

    def create_table(self, table_name: str, schema: str) -> None:
        """
        Crée une table dans la base de données si elle n'existe pas.

        Args:
            table_name (str): Le nom de la table à créer.
            schema (str): La définition du schéma SQL de la table.

        Raises:
            sqlite3.Error: En cas d'échec de la création de la table.
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
        try:
            self.execute_query(query)
            print(f"Table '{table_name}' créée ou déjà existante.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la création de la table '{table_name}' : {e}")

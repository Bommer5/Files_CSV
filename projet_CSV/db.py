import sqlite3


def creer_base_de_donnees():

    # Connexion à la base de données (la créera si elle n'existe pas)
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()


    curseur.execute('''
    CREATE TABLE IF NOT EXISTS departements (
        departement_id INTEGER PRIMARY KEY AUTOINCREMENT,
        departement_nom TEXT NOT NULL UNIQUE
    )
    ''')

    curseur.execute('''
    CREATE TABLE IF NOT EXISTS produits (
        produit_id INTEGER PRIMARY KEY AUTOINCREMENT,
        produit_nom TEXT NOT NULL UNIQUE
    )
    ''')
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS catégories (
            catégorie_id INTEGER PRIMARY KEY AUTOINCREMENT,
            catégorie_nom TEXT NOT NULL UNIQUE
        )
        ''')

    curseur.execute('''
            CREATE TABLE IF NOT EXISTS suppliers  (
                supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_nom TEXT NOT NULL UNIQUE
            )
            ''')
    curseur.execute('''
                CREATE TABLE IF NOT EXISTS units  (
                    unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    unit_nom TEXT NOT NULL UNIQUE
                )
                ''')
    curseur.execute('''
                CREATE TABLE IF NOT EXISTS locations  (
                    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    location_nom TEXT NOT NULL UNIQUE
                )
                ''')
    curseur.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,       
        departement_id INTEGER not null,
        produit_id INTEGER not null,
        catégorie_id INTEGER not null,
        prix float NOT NULL,
        quantité INTEGER NOT NULL,        
        purchase_date TEXT NOT NULL,
        location_id INTEGER,
        supplier_id INTEGER,
        unit_id INTEGER,
        
        FOREIGN KEY(location_id) REFERENCES locations(location_id) ON DELETE CASCADE
        FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE
        FOREIGN KEY(unit_id) REFERENCES units(unit_id) ON DELETE CASCADE
        FOREIGN KEY(departement_id) REFERENCES departements(departement_id) ON DELETE CASCADE
        FOREIGN KEY(produit_id) REFERENCES produits(produit_id) ON DELETE CASCADE
        FOREIGN KEY(catégorie_id) REFERENCES catégories(catégorie_id) ON DELETE CASCADE

    )
    ''')



    # Commit des changements et fermeture de la connexion
    conn.commit()
    conn.close()
def ajouter_departement(departement):
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()

    try :
        curseur.execute('INSERT INTO departements (departement_nom) VALUES (?)', (departement,))
        departement_id = curseur.lastrowid
        conn.commit()
        return departement_id
    except sqlite3.IntegrityError:
        curseur.execute('select departement_id from departements where departement_nom = ?', (departement,))
        departement_id = curseur.fetchone()[0]
        return departement_id
    finally:
        conn.close()
def ajouter_produit(produit):
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()
    try:
        curseur.execute('INSERT INTO produits (produit_nom) VALUES (?)', (produit,))
        produit_id = curseur.lastrowid
        conn.commit()
        return produit_id
    except sqlite3.IntegrityError:
        curseur.execute('SELECT produit_id FROM produits WHERE produit_nom = ?', (produit,))
        produit_id = curseur.fetchone()[0]
        return produit_id
    finally:
        conn.close()

def ajouter_catégories(catégorie):
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()
    try:
        curseur.execute('INSERT INTO catégories (catégorie_nom) VALUES (?)', (catégorie,))
        catégorie_id = curseur.lastrowid
        conn.commit()
        return catégorie_id
    except sqlite3.IntegrityError:
        curseur.execute('SELECT catégorie_id FROM catégories WHERE catégorie_nom = ?', (catégorie,))
        catégorie_id = curseur.fetchone()[0]
        return catégorie_id
    finally:
        conn.close()

def ajouter_data(departement_id, produit_id, catégorie_id, prix, quantité, purchase_date):
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()
    try:
        curseur.execute('''
            INSERT INTO data (departement_id, produit_id, catégorie_id, prix, quantité,purchase_date) 
            VALUES (?, ?, ?,?,?,?)
        ''', (departement_id, produit_id, catégorie_id, prix, quantité,purchase_date))
        data_id = curseur.lastrowid
        conn.commit()
        return data_id
    except sqlite3.IntegrityError as e:
        print(f"Erreur lors de l'ajout dans data : {e}")
        return None
    finally:
        conn.close()
def ajouter_supplier(supplier_nom):
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()
    try:
        curseur.execute('INSERT INTO suppliers (supplier_nom) VALUES (?)', (supplier_nom,))
        supplier_id = curseur.lastrowid
        conn.commit()
        return supplier_id
    except sqlite3.IntegrityError:
        curseur.execute('SELECT supplier_id FROM suppliers WHERE supplier_nom = ?', (supplier_nom,))
        supplier_id = curseur.fetchone()[0]
        return supplier_id
    finally:
        conn.close()
def ajouter_unit(unit_nom):
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()
    try:
        curseur.execute('INSERT INTO units (unit_nom) VALUES (?)', (unit_nom,))
        unit_id = curseur.lastrowid
        conn.commit()
        return unit_id
    except sqlite3.IntegrityError:
        curseur.execute('SELECT unit_id FROM units WHERE unit_nom = ?', (unit_nom,))
        unit_id = curseur.fetchone()[0]
        return unit_id
    finally:
        conn.close()
def ajouter_location(location_nom):
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()
    try:
        curseur.execute('INSERT INTO locations (location_nom) VALUES (?)', (location_nom,))
        location_id = curseur.lastrowid
        conn.commit()
        return location_id
    except sqlite3.IntegrityError:
        curseur.execute('SELECT location_id FROM locations WHERE location_nom = ?', (location_nom,))
        location_id = curseur.fetchone()[0]
        return location_id
    finally:
        conn.close()


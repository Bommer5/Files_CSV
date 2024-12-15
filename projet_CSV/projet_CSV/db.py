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
        produit_nom TEXT NOT NULL UNIQUE,
        prix REAL NOT NULL,
        quantité INTEGER NOT NULL
    )
    ''')
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS catégories (
            catégorie_id INTEGER PRIMARY KEY AUTOINCREMENT,
            catégorie_nom TEXT NOT NULL UNIQUE
        )
        ''')


    curseur.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,       
        departement_id INTEGER not null,
        produit_id INTEGER not null,
        catégorie_id INTEGER not null,        
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
def ajouter_produit(produit, prix, quantité):
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()
    try:
        curseur.execute('INSERT INTO produits (produit_nom, prix, quantité) VALUES (?, ?, ?)', (produit, prix, quantité))
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

def ajouter_data(departement_id, produit_id, catégorie_id):
    conn = sqlite3.connect('CSV.db')
    curseur = conn.cursor()
    try:
        curseur.execute('''
            INSERT INTO data (departement_id, produit_id, catégorie_id) 
            VALUES (?, ?, ?)
        ''', (departement_id, produit_id, catégorie_id))
        data_id = curseur.lastrowid
        conn.commit()
        return data_id
    except sqlite3.IntegrityError as e:
        print(f"Erreur lors de l'ajout dans data : {e}")
        return None
    finally:
        conn.close()


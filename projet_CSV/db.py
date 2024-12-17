import sqlite3
import os

def create_database():
    """
    Creates a new database and tables if they do not exist. If the database already exists, it will be deleted first.
    """
    database_filename = "CSV.db"

    # Check and remove the old database if it exists
    if os.path.exists(database_filename):
        print(f"Removing the old database: {database_filename}")
        os.remove(database_filename)

    # Connect to the database (it will be created if it does not exist)
    conn = sqlite3.connect(database_filename)
    cursor = conn.cursor()

    # Create the tables in the database
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        department_id INTEGER PRIMARY KEY AUTOINCREMENT,
        department_name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suppliers  (
        supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
        supplier_name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS units  (
        unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
        unit_name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS locations  (
        location_id INTEGER PRIMARY KEY AUTOINCREMENT,
        location_name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,       
        department_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL,        
        purchase_date TEXT NOT NULL,
        location_id INTEGER,
        supplier_id INTEGER,
        unit_id INTEGER,

        FOREIGN KEY(location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
        FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
        FOREIGN KEY(unit_id) REFERENCES units(unit_id) ON DELETE CASCADE,
        FOREIGN KEY(department_id) REFERENCES departments(department_id) ON DELETE CASCADE,
        FOREIGN KEY(product_id) REFERENCES products(product_id) ON DELETE CASCADE,
        FOREIGN KEY(category_id) REFERENCES categories(category_id) ON DELETE CASCADE
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def add_department(department):
    """
    Adds a department to the database. If the department already exists, it returns the existing department's ID.

    Args:
    department (str): The name of the department.

    Returns:
    int: The department's ID.
    """
    conn = sqlite3.connect('CSV.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO departments (department_name) VALUES (?)', (department,))
        department_id = cursor.lastrowid
        conn.commit()
        return department_id
    except sqlite3.IntegrityError:
        cursor.execute('SELECT department_id FROM departments WHERE department_name = ?', (department,))
        department_id = cursor.fetchone()[0]
        return department_id
    finally:
        conn.close()

def add_product(product):
    """
    Adds a product to the database. If the product already exists, it returns the existing product's ID.

    Args:
    product (str): The name of the product.

    Returns:
    int: The product's ID.
    """
    conn = sqlite3.connect('CSV.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO products (product_name) VALUES (?)', (product,))
        product_id = cursor.lastrowid
        conn.commit()
        return product_id
    except sqlite3.IntegrityError:
        cursor.execute('SELECT product_id FROM products WHERE product_name = ?', (product,))
        product_id = cursor.fetchone()[0]
        return product_id
    finally:
        conn.close()

def add_category(category):
    """
    Adds a category to the database. If the category already exists, it returns the existing category's ID.

    Args:
    category (str): The name of the category.

    Returns:
    int: The category's ID.
    """
    conn = sqlite3.connect('CSV.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO categories (category_name) VALUES (?)', (category,))
        category_id = cursor.lastrowid
        conn.commit()
        return category_id
    except sqlite3.IntegrityError:
        cursor.execute('SELECT category_id FROM categories WHERE category_name = ?', (category,))
        category_id = cursor.fetchone()[0]
        return category_id
    finally:
        conn.close()

def add_data(department_id, product_id, category_id, price, quantity, purchase_date, unit_id, location_id, supplier_id):
    """
    Adds a record to the 'data' table.

    Args:
    department_id (int): ID of the department.
    product_id (int): ID of the product.
    category_id (int): ID of the category.
    price (float): Price of the product.
    quantity (int): Quantity of the product.
    purchase_date (str): Date of purchase.
    unit_id (int): ID of the unit.
    location_id (int): ID of the location.
    supplier_id (int): ID of the supplier.

    Returns:
    int: The ID of the inserted data record.
    """
    conn = sqlite3.connect('CSV.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO data (department_id, product_id, category_id, price, quantity, purchase_date, unit_id, location_id, supplier_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (department_id, product_id, category_id, price, quantity, purchase_date, unit_id, location_id, supplier_id))
        data_id = cursor.lastrowid
        conn.commit()
        return data_id
    except sqlite3.IntegrityError as e:
        print(f"Error when adding to data: {e}")
        return None
    finally:
        conn.close()

def add_supplier(supplier_name):
    """
    Adds a supplier to the database. If the supplier already exists, it returns the existing supplier's ID.

    Args:
    supplier_name (str): The name of the supplier.

    Returns:
    int: The supplier's ID.
    """
    conn = sqlite3.connect('CSV.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO suppliers (supplier_name) VALUES (?)', (supplier_name,))
        supplier_id = cursor.lastrowid
        conn.commit()
        return supplier_id
    except sqlite3.IntegrityError:
        cursor.execute('SELECT supplier_id FROM suppliers WHERE supplier_name = ?', (supplier_name,))
        supplier_id = cursor.fetchone()[0]
        return supplier_id
    finally:
        conn.close()

def add_unit(unit_name):
    """
    Adds a unit to the database. If the unit already exists, it returns the existing unit's ID.

    Args:
    unit_name (str): The name of the unit.

    Returns:
    int: The unit's ID.
    """
    conn = sqlite3.connect('CSV.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO units (unit_name) VALUES (?)', (unit_name,))
        unit_id = cursor.lastrowid
        conn.commit()
        return unit_id
    except sqlite3.IntegrityError:
        cursor.execute('SELECT unit_id FROM units WHERE unit_name = ?', (unit_name,))
        unit_id = cursor.fetchone()[0]
        return unit_id
    finally:
        conn.close()

def add_location(location_name):
    """
    Adds a location to the database. If the location already exists, it returns the existing location's ID.

    Args:
    location_name (str): The name of the location.

    Returns:
    int: The location's ID.
    """
    conn = sqlite3.connect('CSV.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO locations (location_name) VALUES (?)', (location_name,))
        location_id = cursor.lastrowid
        conn.commit()
        return location_id
    except sqlite3.IntegrityError:
        cursor.execute('SELECT location_id FROM locations WHERE location_name = ?', (location_name,))
        location_id = cursor.fetchone()[0]
        return location_id
    finally:
        conn.close()

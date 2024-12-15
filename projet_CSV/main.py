import csv
import os
import glob
import db
import variable

# Constants to represent column indices for better readability
COLUMN_PRODUCT_NAME = 0
COLUMN_CATEGORY = 1
COLUMN_DEPARTMENT = 2
COLUMN_QUANTITY = 3
COLUMN_PURCHASE_DATE = 4
COLUMN_PRICE = 5
COLUMN_SUPPLIER = 6
COLUMN_UNIT = 7
COLUMN_LOCATION = 8


class CSVFileProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.header = None
        self.data = []

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                self.header = next(reader, None)  # Fetch header, or None if empty
                self.data = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_header(self):
        return self.header

    def get_data(self):
        return self.data


def process_csv_file(file_path):
    csv_processor = CSVFileProcessor(file_path)
    csv_processor.read_file()
    print(f"The file {csv_processor.filename} has the header: {csv_processor.get_header()}")

    for row in csv_processor.get_data():
        # Extract values from the row
        department = row[COLUMN_DEPARTMENT]
        product = row[COLUMN_PRODUCT_NAME]
        quantity = int(row[COLUMN_QUANTITY])
        price = row[COLUMN_PRICE][1:]
        category = row[COLUMN_CATEGORY]

        supplier = row[COLUMN_SUPPLIER]
        purchase_date = row[COLUMN_PURCHASE_DATE]

        unit = row[COLUMN_UNIT]
        location = row[COLUMN_LOCATION]

        print(
            f"Processing data for Department: {department}, Product: {product}, Quantity: {quantity}, Price: {price}, Category: {category}, Purchase Date: {purchase_date}, Supplier: {supplier}, Unit: {unit}, Location: {location}"
        )
        # Insert or fetch IDs and add data to the database
        department_id = db.ajouter_departement(department)
        product_id = db.ajouter_produit(product)
        category_id = db.ajouter_catégories(category)
        supplier_id = db.ajouter_supplier(supplier)
        unit_id = db.ajouter_unit(unit)
        location_id = db.ajouter_location(location)
        data_id = db.ajouter_data(department_id, product_id, category_id, price, quantity, purchase_date)


        print(
            f"Added Data: Department({department_id}), Product({product_id}), Category({category_id}), Data({data_id})"
        )


# Main script
if __name__ == "__main__":
    db.creer_base_de_donnees()
    csv_files = glob.glob(os.path.join(variable.CSV_DIRECTORY, "*.csv"))

    for file_path in csv_files:
        process_csv_file(file_path)

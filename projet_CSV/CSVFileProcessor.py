import csv
import db

class CSVFileProcessor:
    """
    A class for processing CSV files and extracting data for database insertion.

    Attributes:
        filename (str): The path to the CSV file.
        header (list[str]): The header row of the CSV file.
        data (list[list[str]]): The content rows of the CSV file.
    """

    def __init__(self, filename: str):
        """
        Initialize a CSVFileProcessor instance.

        Args:
            filename (str): The path to the CSV file.
        """
        self.filename = filename
        self.header = None
        self.data = []

    def read_file(self) -> None:
        """
        Read the CSV file and populate the header and data attributes.

        Raises:
            FileNotFoundError: If the file does not exist.
            Exception: For any other errors during file reading.
        """
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                self.header = next(reader, None)  # Fetch header, or None if empty
                self.data = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: The file {self.filename} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_header(self) -> list[str]:
        """
        Retrieve the header of the CSV file.

        Returns:
            list[str]: The header row of the file.
        """
        return self.header

    def get_data(self) -> list[list[str]]:
        """
        Retrieve the data rows of the CSV file.

        Returns:
            list[list[str]]: The content rows of the file.
        """
        return self.data

    @staticmethod
    def process_csv_file(file_path: str) -> None:
        """
        Process a CSV file and insert its data into the database.

        Args:
            file_path (str): The path to the CSV file.

        Raises:
            ValueError: If the file data is not properly formatted.
        """
        csv_processor = CSVFileProcessor(file_path)
        csv_processor.read_file()

        if not csv_processor.header:
            raise ValueError("The CSV file is empty or does not contain a header.")

        print(f"The file {csv_processor.filename} has the header: {csv_processor.get_header()}")

        for row in csv_processor.get_data():
            try:
                # Column indices
                COLUMN_PRODUCT_NAME = 0
                COLUMN_CATEGORY = 1
                COLUMN_DEPARTMENT = 2
                COLUMN_QUANTITY = 3
                COLUMN_PURCHASE_DATE = 4
                COLUMN_PRICE = 5
                COLUMN_SUPPLIER = 6
                COLUMN_UNIT = 7
                COLUMN_LOCATION = 8

                # Extract values from the row
                department = row[COLUMN_DEPARTMENT]
                product = row[COLUMN_PRODUCT_NAME]
                quantity = int(row[COLUMN_QUANTITY])
                price = float(row[COLUMN_PRICE][1:])  # Assuming price starts with a currency symbol
                category = row[COLUMN_CATEGORY]
                supplier = row[COLUMN_SUPPLIER]
                purchase_date = row[COLUMN_PURCHASE_DATE]
                unit = row[COLUMN_UNIT]
                location = row[COLUMN_LOCATION]

                print(
                    f"Processing data for Department: {department}, Product: {product}, "
                    f"Quantity: {quantity}, Price: {price}, Category: {category}, "
                    f"Purchase Date: {purchase_date}, Supplier: {supplier}, "
                    f"Unit: {unit}, Location: {location}"
                )

                # Insert or fetch IDs and add data to the database
                department_id = db.add_department(department)
                product_id = db.add_product(product)
                category_id = db.add_category(category)
                supplier_id = db.add_supplier(supplier)
                unit_id = db.add_unit(unit)
                location_id = db.add_location(location)

                data_id = db.add_data(
                    department_id=department_id,
                    product_id=product_id,
                    category_id=category_id,
                    price=price,
                    quantity=quantity,
                    purchase_date=purchase_date,
                    supplier_id=supplier_id,
                    unit_id=unit_id,
                    location_id=location_id
                )

                print(
                    f"Added Data: Department({department_id}), Product({product_id}), "
                    f"Category({category_id}), Data({data_id})"
                )

            except IndexError:
                print(f"Error: Missing data in row {row}")
            except ValueError as e:
                print(f"Error in processing row {row}: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

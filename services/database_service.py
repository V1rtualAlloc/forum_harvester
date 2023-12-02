import json
import mysql.connector

'''
Manages MariaDB database connection safely

# Example usage:
    # Using the context manager to ensure the connection is properly closed
    with DatabaseService() as db_service:
        result = db_service.execute_query("SELECT * FROM your_table")
        print(result)
    # Connection is automatically closed when exiting the 'with' block
'''


class DatabaseService:
    def __init__(self, config_path='configuration.json'):
        self.config_path = config_path
        self.connection = None

    def load_config(self):
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        return config

    def __enter__(self):
        config = self.load_config()

        # Open a database connection when entering the context
        self.connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the database connection when exiting the context
        if self.connection:
            self.connection.close()

    # Additional methods for database operations can be added here
    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

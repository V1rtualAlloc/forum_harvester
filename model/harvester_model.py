import json
import os
import mysql.connector
import requests
from bs4 import BeautifulSoup
import time
from model.base_model import BaseModel


class HarvesterModel(BaseModel):
    def download_html(self, url):
        response = requests.get(url)
        return response.content
    
    def parse_html(self, html_content):
        # Your parsing logic here using BeautifulSoup or any other library
        # Example:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract data from the parsed HTML
        data = {'example': 'data'}
        return data
    
    def insert_into_mariadb(data, cursor):
        # Your MariaDB insertion logic here
        # Example (replace this with your actual MariaDB insertion code):
        query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
        values = (data['example'], 'some_value')
        cursor.execute(query, values)

    def serialize_progress(self, current_page, output_directory):
        progress = {'current_page': current_page}
        with open(os.path.join(output_directory, 'progress.json'), 'w') as f:
            json.dump(progress, f, indent=2)

    def start(self, database_name, ):
        # Your main processing loop
        output_directory = "output_data"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # MariaDB connection details
        database_config = {
            'host': 'your_host',
            'user': 'your_user',
            'password': 'your_password',
            'database': 'your_database',
        }

        connection = mysql.connector.connect(**database_config)
        cursor = connection.cursor()

        # Create your MariaDB table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS your_table (column1 VARCHAR(255), column2 VARCHAR(255))")

        # Load progress if it exists
        progress_file = os.path.join(output_directory, 'progress.json')
        if os.path.exists(progress_file):
            with open(progress_file, 'r') as f:
                progress = json.load(f)
            start_page = progress['current_page'] + 1
        else:
            start_page = 1

        for current_page in range(start_page, 10001):
            # Download HTML
            url = f"your_base_url/page{current_page}.html"
            html_content = self.download_html(url)

            # Parse HTML
            parsed_data = self.parse_html(html_content)

            # Insert into MariaDB
            self.insert_into_mariadb(parsed_data, cursor)
            connection.commit()

            # Serialize progress
            self.serialize_progress(current_page, output_directory)

            print(f"Processed and saved page {current_page}.")

            # Add a 5-second delay between processing pages
            time.sleep(5)

        # Close the MariaDB connection
        connection.close()


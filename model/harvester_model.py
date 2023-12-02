from services.data_serializer_service import DataSerializerService
from services.download_service import DownloadService
from services.parse_service import ParseService
from services.database_service import DatabaseService

from model.base_model import BaseModel


class HarvesterModel(BaseModel):
    def __init__(self, pages, name, template, output_directory='output_data'):
        self.pages = pages
        self.name = name
        self.template = template
        self.output_directory = output_directory

    def process_pages(self):
        # Initialize DataSerializerService
        serializer = DataSerializerService(self.pages, self.name)

        # Iterate through pages
        for current_page, page_url in enumerate(self.pages, start=1):
            with DownloadService() as download_service:
                # Download page
                html_content, response = download_service.download_page(page_url)

            if response.ok and html_content is not None:
                with ParseService(html_content, self.template) as parse_service:
                    # Parse HTML
                    parsed_data = parse_service.parse_html()

                with DatabaseService() as db_service:
                    # Add parsed data to database
                    query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
                    params = (parsed_data.get('key1', ''), parsed_data.get('key2', ''))
                    db_service.execute_query(query, params)

                # Update progress and serialize
                serializer.processed_pages.append(current_page)
                serializer.serialize_progress(current_page, self.output_directory)



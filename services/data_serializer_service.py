import os
import json


'''
Data serialize/deserializer class for current progress

# Example usage:
    output_directory = "output_data"
    name = "example"

    # Create an instance of DataSerializerService
    serializer = DataSerializerService(pages=[1, 2, 3], name=name)

    # Serialize progress
    serializer.serialize_progress(current_page=2, output_directory=output_directory)

    # Deserialize progress
    progress_file_path = os.path.join(output_directory, f'progress_{name}.json')
    deserialize_info = serializer.deserialize_progress(progress_file_path)

    if deserialize_info:
        print("Deserialized progress:")
        print(f"Current Page: {deserialize_info['current_page']}")
        print(f"Total Pages: {deserialize_info['total_pages']}")
        print(f"Processed Pages: {deserialize_info['processed_pages']}")
    else:
        print("Progress file does not exist.")
'''


class DataSerializerService:
    def __init__(self, pages, name):
        self.serialize_info = None
        self.pages = pages
        self.name = name
        self.total_pages = len(pages) if isinstance(pages, list) else pages
        self.processed_pages = list()

    def serialize_progress(self, current_page, output_directory):
        serialize_info = {'current_page': current_page, 'total_pages': self.total_pages, 'processed_pages': self.processed_pages}
        file_path = os.path.join(output_directory, f'progress_{self.name}.json')
        
        with open(file_path, 'w') as f:
            json.dump(serialize_info, f, indent=2)

    def deserialize_progress(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                deserialize_info = json.load(f)

            # Update the object's state with the deserialized information
            self.total_pages = deserialize_info['total_pages']
            self.processed_pages = deserialize_info['processed_pages']
            return deserialize_info
        else:
            print(f"Progress file {file_path} does not exist.")
            return None

    def get_current_progress(self):
        progress = (len(self.processed_pages) / self.total_pages) * 100
        return round(progress, 2)

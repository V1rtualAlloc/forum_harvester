import requests


'''
Downloads page and its context from the provided url

# Example usage:
    url = "https://example.com"

    with DownloadService() as download_service:
        html_content, response = download_service.download_page(url)

        if html_content is not None:
            print(f"Downloaded content from {url}:\n{html_content}")
        else:
            print(f"Failed to download content from {url}")
    # The __exit__ method is automatically called when exiting the 'with' block
'''


class DownloadService:
    def __enter__(self):
        self.session = requests.Session()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_session()

    def download_page(self, url):
        try:
            # Send an HTTP request to the specified URL
            response = self.session.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Return both the HTML content and the response object
                return response.text, response

            # If the request was not successful, print an error message
            print(f"Error: {response.status_code}")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Return None if the request was unsuccessful
        return None, None

    def close_session(self):
        # Close the requests session
        if hasattr(self, 'session'):
            self.session.close()
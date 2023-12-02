from bs4 import BeautifulSoup

'''
Parse given HTML text based upon loaded template

# Example usage:
    html_content = "<html><body><div class='title'>Title</div><p class='content'>Content</p></body></html>"
    template = [
        {"selector": "div.title", "key": "title"},
        {"selector": "p.content", "key": "content"}
    ]

    parse_service = ParseService(html_content, template)
    parsed_data = parse_service.parse_html()

    print("Parsed Data:")
    print(parsed_data)
'''

class ParseService:
    def __init__(self, html_content, template):
        self.html_content = html_content
        self.template = template

    def parse_html(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')

        parsed_data = {}
        for element in self.template:
            selector = element.get('selector')
            key = element.get('key')

            if selector and key:
                selected_elements = soup.select(selector)
                parsed_data[key] = [element.text.strip() for element in selected_elements]

        return parsed_data

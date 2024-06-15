import requests


class Interactor():
    def __init__(self, url):
        self.url = url


    def get_data(self):
        response = requests.get(f"{self.url}/getall")
        return response.json()
    

    def get_positions_by_category(self, category: str):
        response = requests.get(f"{self.url}/{category}")
        return response.json()
    
    
    def get_categories(self):
        response = requests.get(f"{self.url}/categories")
        return response.json()


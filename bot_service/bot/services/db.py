import requests
import logging

logger = logging.getLogger(__name__)

class Interactor():
    def __init__(self, url):
        self.url = url


    def get_categories(self):
        response = requests.get(f"{self.url}/categories")
        return response.json()
    

    def get_description_by_category(self, category: str):
        response = requests.get(f"{self.url}/category/{category}")
        return response.json()


    def get_data_by_category(self, category: str):
        response = requests.get(f"{self.url}/category_data/{category}") # to be refactored
        return response.json()
    

    def get_position_by_its_name(self, pos: str):
        response = requests.get(f"{self.url}/position/{pos}")
        return response.json()

    
    def get_position_photos(self, pos: str):
        response = requests.get(f"{self.url}/position_data/{pos}")
        return response.json()


    def get_category_by_id(self, category: str):
        response = requests.get(f"{self.url}/category_by_id/{category}") # to be refactored
        return response.json()

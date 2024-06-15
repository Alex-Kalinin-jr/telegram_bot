import requests


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
        
        response = requests.get(f"{self.url}/category_data/{category}")
        return response.json()
    



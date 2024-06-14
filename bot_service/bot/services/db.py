import requests


class Interactor():
    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(f"{self.url}/getall")
        return response.json()


import requests

class JeuxDeMotsAPI:
    def __init__(self):
        self.base_url = "https://jdm-api.demo.lirmm.fr"

    def get_node_by_name(self, node_name):
        url = f"{self.base_url}/v0/node_by_name/{node_name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erreur API pour le token : {node_name}, Status Code: {response.status_code}")
            return None

    def get_morphological_data(self, token):
        # Exemple : récupérez les données morphologiques via une API ou localement
        return [{"type": "GN", "weight": 10}, {"type": "GV", "weight": 5}]

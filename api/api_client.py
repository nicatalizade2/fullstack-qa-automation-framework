import requests
import yaml

class APIClient:
    def __init__(self):
        config = yaml.safe_load(open('config.yaml'))
        self.base_url = config['api_base_url']

    def get(self,endpoint,params=None):
        return requests.get(f"{self.base_url}{endpoint}",params=params)

    def post(self,endpoint, data=None):
        return requests.post(f"{self.base_url}{endpoint}", json=data)

    def put(self,endpoint, data=None):
        return requests.put(f"{self.base_url}{endpoint}", json=data)

    def delete(self,endpoint):
        return requests.delete(f'{self.base_url}{endpoint}')
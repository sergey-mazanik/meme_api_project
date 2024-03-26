import requests
from endpoints.endpoint import Endpoint


class GetAliveAuthToken(Endpoint):

    def get_alive_token(self):
        self.response = requests.get(f'{self.url}/authorize/{self.token}')
        return self.response.status_code

    def get_alive_incorrect_token(self):
        self.response = requests.get(f'{self.url}/authorize/incorrectToken')
        return self.response

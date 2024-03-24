import requests
from endpoints.endpoint import Endpoint


class GetAliveAuthToken(Endpoint):

    def get_alive_token(self):
        self.response = requests.get(f'{self.url}/authorize/{self.token}')
        if self.response.status_code == 200:
            return True
        else:
            return False

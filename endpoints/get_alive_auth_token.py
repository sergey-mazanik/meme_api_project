import requests
from endpoints.endpoint import Endpoint


class GetAliveAuthToken(Endpoint):

    def get_alive_token(self):
        self.response = requests.get(f'{self.url}/authorize/{self.token}')
        return self.response.status_code

    def check_that_token_alive(self):
        assert self.get_alive_token() == 200, f'Status code is not 200 - {self.response.status_code}'

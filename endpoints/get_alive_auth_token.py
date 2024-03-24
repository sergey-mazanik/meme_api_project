import requests
from endpoints.endpoint import Endpoint


class GetAliveAuthToken(Endpoint):

    def get_alive_token(self):
        self.response = requests.get(f'{self.url}/authorize/{self.token}')
        return self.response.status_code
        # print(self.response.status_code)
        # if self.response.status_code == 200:
        #     return True
        # else:
        #     return False

    def check_that_token_alive(self):
        assert self.get_alive_token() == 200, 'Status code is not 200'

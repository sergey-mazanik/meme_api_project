import requests
import dotenv
from endpoints.endpoint import Endpoint

dotenv.load_dotenv(dotenv.find_dotenv())


class CreateNewAuthToken(Endpoint):

    def create_new_auth_token_and_rewrite(self, body=None):
        body = body if body else self.body
        self.response = requests.post(f'{self.url}/authorize', json=body)
        self.json = self.response.json()
        dotenv.set_key(dotenv.find_dotenv(), 'TOKEN', self.json['token'])
        dotenv.set_key(dotenv.find_dotenv(), 'USER_NAME', self.json['user'])
        return self.response

    def create_new_auth_token_positive(self, body=None):
        body = body if body else self.body
        self.response = requests.post(f'{self.url}/authorize', json=body)
        return self.response

    def create_new_auth_token_negative(self, body=None):
        self.response = requests.post(f'{self.url}/authorize', json=body)
        return self.response

    def check_that_token_is_new(self):
        assert self.response.json()['token'] != self.token, 'Token is not new'

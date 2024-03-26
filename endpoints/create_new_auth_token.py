import requests
import os
from endpoints.endpoint import Endpoint
from faker import Faker


class CreateNewAuthToken(Endpoint):

    def create_new_auth_token_and_rewrite(self, body=None):
        body = body if body else self.body
        self.response = requests.post(f'{self.url}/authorize', json=body)
        self.json = self.response.json()
        self.token = self.json['token']
        with open(f'{os.path.abspath(os.curdir)}/cred.py', 'w') as f:
            f.write(f'TOKEN = "{self.json['token']}"\n'
                    f'USER_NAME = "{self.json['user']}"\n'
                    f'API_URL = "{self.url}"\n')
        return self.response

    def create_new_auth_token_positive(self, body=None):
        body = body if body else self.body
        self.response = requests.post(f'{self.url}/authorize', json=body)
        return self.response

    def create_new_auth_token_negative(self, body=None):
        self.response = requests.post(f'{self.url}/authorize', json=body)
        return self.response

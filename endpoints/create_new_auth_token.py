import requests
import os
from endpoints.endpoint import Endpoint
from faker import Faker


class CreateNewAuthToken(Endpoint):

    def create_new_auth_token(self):
        body = {'name': Faker().name()}
        self.response = requests.post(f'{self.url}/authorize', json=body)
        self.json = self.response.json()
        with open(f'{os.path.abspath(os.curdir)}/cred.py', 'w') as f:
            f.write(f'TOKEN = "{self.json['token']}"\n'
                    f'USER_NAME = "{self.json['user']}"\n'
                    f'API_URL = "{self.url}"\n')
        return self.response

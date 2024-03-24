import requests
import cred
from faker import Faker
import os


class Endpoint:
    url = cred.API_URL
    response = None
    json = None
    headers = {'Authorization': cred.TOKEN}
    fake = Faker()

    def get_authorize_token(self):
        body = {'name': self.fake.name()}
        self.response = requests.post(f'{self.url}/authorize', json=body)
        self.json = self.response.json()
        with open(f'{os.path.abspath(os.curdir)}/cred.py', 'w') as f:
            f.write(f'TOKEN = "{self.json['token']}"\n'
                    f'USER_NAME = "{self.json['user']}"\n'
                    f'API_URL = "{self.url}"\n')
        return self.response

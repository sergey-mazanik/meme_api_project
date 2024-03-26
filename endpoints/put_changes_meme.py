import requests
from endpoints.endpoint import Endpoint


class PutChangesMeme(Endpoint):

    def make_changes_in_meme(self, meme_id, body=None, headers=None):
        headers = headers if headers else self.headers
        body['id'] = meme_id
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=body, headers=headers)
        try:
            self.json = self.response.json()
            return self.response
        except requests.exceptions.JSONDecodeError:
            return self.response

    def make_changes_in_meme_without_id(self, meme_id, body=None, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=body, headers=headers)
        return self.response

    def make_changes_in_meme_without_auth_token(self, meme_id, body=None):
        body['id'] = meme_id
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=body, headers={'Authorization': ''})
        return self.response

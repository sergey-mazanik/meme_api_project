import requests
from endpoints.endpoint import Endpoint


class PutChangesMeme(Endpoint):

    def make_changes_in_meme(self, meme_id, body=None, headers=None):
        headers = headers if headers else self.headers
        body = body if body else self.body
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response

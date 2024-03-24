import requests
from endpoints.endpoint import Endpoint


class PostNewMeme(Endpoint):

    def post_new_meme(self, body=None, headers=None):
        headers = headers if headers else self.headers
        body = body if body else self.body
        self.response = requests.post(f'{self.url}/meme', json=body, headers=headers)
        self.json = self.response.json()
        self.creating_meme_list.append(self.json['id'])
        return self.json['id']

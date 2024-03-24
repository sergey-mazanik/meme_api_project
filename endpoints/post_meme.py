import requests
from endpoints.endpoint import Endpoint


class PostNewMeme(Endpoint):

    def post_new_meme(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/meme', json=body, headers=headers)
        self.json = self.response.json()
        print(self.json['id'])
        return self.response

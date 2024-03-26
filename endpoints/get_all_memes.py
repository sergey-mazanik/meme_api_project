import requests
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):

    def get_all_memes_list(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        try:
            self.json = self.response.json()
            return self.response
        except requests.exceptions.JSONDecodeError:
            return self.response

    def get_all_memes_without_auth_token(self):
        self.response = requests.get(f'{self.url}/meme', headers={'Authorization': ''})
        return self.response

import requests
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):

    def get_all_memes_list(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        self.json = self.response.json()
        print(len(self.json['data']))
        return self.response

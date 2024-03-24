import requests
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):

    def get_all_memes_list(self):
        self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        self.json = self.response.json()
        print(len(self.json['data']))
        return self.response

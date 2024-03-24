import requests
from endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):

    def get_one_meme(self, meme_id):
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=self.headers)
        self.json = self.response.json()
        print(self.json)
        return self.response

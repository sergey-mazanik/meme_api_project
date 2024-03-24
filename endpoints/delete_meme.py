import requests
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    def delete_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/meme/{meme_id}', headers=headers)
        return self.response

    def clear_data_after_testing(self, headers=None):
        headers = headers if headers else self.headers
        for meme_id in self.creating_meme_list:
            requests.delete(f'{self.url}/meme/{meme_id}', headers=headers)

import requests
from endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):

    def get_one_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=headers)
        try:
            self.json = self.response.json()
            return self.response
        except requests.exceptions.JSONDecodeError:
            return self.response

    def get_one_meme_without_auth_token(self, meme_id):
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers={'Authorization': ''})
        return self.response

    def check_that_response_meme_id_is_correct(self, meme_id):
        assert self.json['id'] == meme_id, 'meme_id is not correct'

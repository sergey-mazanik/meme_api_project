import allure
import requests
from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):

    @allure.step('Get all memes')
    def get_all_memes_list(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        try:
            self.json = self.response.json()
            return self.response
        except requests.exceptions.JSONDecodeError:
            return self.response

    @allure.step('Get all memes without authorization')
    def get_all_memes_without_auth_token(self):
        self.response = requests.get(f'{self.url}/meme', headers={'Authorization': ''})
        return self.response

    @allure.step('Check that meme list is not empty')
    def check_that_meme_list_is_not_empty(self):
        assert len(self.json['data']) > 0, 'Meme list is empty'

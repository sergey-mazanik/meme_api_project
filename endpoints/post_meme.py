import allure
import requests
from endpoints.endpoint import Endpoint


class PostNewMeme(Endpoint):

    @allure.step('Post new meme')
    def post_new_meme(self, body=None, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/meme', json=body, headers=headers)
        try:
            self.json = self.response.json()
            self.creating_meme_list.append(self.json['id'])
            return self.json['id']
        except requests.exceptions.JSONDecodeError:
            return self.response

    @allure.step('Post new meme without authorization')
    def post_new_meme_without_auth_token(self, body=None):
        self.response = requests.post(f'{self.url}/meme', json=body, headers={'Authorization': ''})
        return self.response

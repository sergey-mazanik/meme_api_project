import allure
import requests
import dotenv
from endpoints.endpoint import Endpoint

dotenv.load_dotenv(dotenv.find_dotenv())


class CreateNewAuthToken(Endpoint):

    @allure.step('Create new auth token and override')
    def create_new_auth_token_and_rewrite(self, body=None):
        body = body if body else self.body
        self.response = requests.post(f'{self.url}/authorize', json=body)
        self.json = self.response.json()
        dotenv.set_key(dotenv.find_dotenv(), 'TOKEN', self.json['token'])
        dotenv.set_key(dotenv.find_dotenv(), 'USER_NAME', self.json['user'])
        return self.response

    @allure.step('Create new auth token')
    def create_new_auth_token_positive(self, body=None):
        body = body if body else self.body
        self.response = requests.post(f'{self.url}/authorize', json=body)
        return self.response

    @allure.step('Create new auth token (negative case)')
    def create_new_auth_token_negative(self, body=None):
        self.response = requests.post(f'{self.url}/authorize', json=body)
        return self.response

    @allure.step('Check that token is new')
    def check_that_token_is_new(self):
        assert self.response.json()['token'] != self.token, 'Token is not new'

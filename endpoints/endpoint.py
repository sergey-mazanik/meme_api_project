import os
import dotenv
from faker import Faker

dotenv.load_dotenv(dotenv.find_dotenv())


class Endpoint:
    url = os.getenv('API_URL')
    body = {'name': Faker().name()}
    response = None
    json = None
    token = os.getenv('TOKEN')
    user = os.getenv('USER_NAME')
    headers = {'Authorization': os.getenv('TOKEN')}
    creating_meme_list = []

    def check_that_status_is_200(self):
        assert self.response.status_code == 200, f'Status code is {self.response.status_code}'

    def check_that_status_is_400(self):
        assert self.response.status_code == 400, f'Status code is {self.response.status_code}'

    def check_that_status_is_401(self):
        assert self.response.status_code == 401, f'Status code is {self.response.status_code}'

    def check_that_status_is_403(self):
        assert self.response.status_code == 403, f'Status code is {self.response.status_code}'

    def check_that_status_is_404(self):
        assert self.response.status_code == 404, f'Status code is {self.response.status_code}'

    def check_that_author_is_correct(self):
        assert self.json['updated_by'] == os.getenv('USER_NAME'), f"{self.json['updated_by']} is not correct author"

    def check_that_response_text_is_correct(self, data):
        assert self.json['text'] == data['text'], 'Response text is not correct'

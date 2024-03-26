import cred
from faker import Faker


class Endpoint:
    url = cred.API_URL
    body = {'name': Faker().name()}
    response = None
    json = None
    token = cred.TOKEN
    headers = {'Authorization': cred.TOKEN}
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


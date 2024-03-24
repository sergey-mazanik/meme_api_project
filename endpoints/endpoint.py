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
        assert self.response.status_code == 200, 'Status code is not 200'

import cred


class Endpoint:
    url = cred.API_URL
    response = None
    json = None
    token = cred.TOKEN
    headers = {'Authorization': cred.TOKEN}

    def check_that_status_is_200(self):
        assert self.response.status_code == 200, 'Status code is not 200'

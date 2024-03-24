import pytest
import requests
import cred
from endpoints.create_new_auth_token import CreateNewAuthToken
from endpoints.get_alive_auth_token import GetAliveAuthToken
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_one_meme import GetOneMeme
from endpoints.post_meme import PostNewMeme
from endpoints.put_changes_meme import PutChangesMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture()
def create_new_auth_token_endpoint():
    return CreateNewAuthToken()


@pytest.fixture()
def get_alive_token_endpoint():
    return GetAliveAuthToken()


@pytest.fixture()
def use_or_create_new_auth_token(get_alive_token_endpoint, create_new_auth_token_endpoint):
    if get_alive_token_endpoint.get_alive_token() == 200:
        return None
    else:
        create_new_auth_token_endpoint.create_new_auth_token()


@pytest.fixture()
def get_all_memes_endpoint():
    return GetAllMemes()


@pytest.fixture()
def get_one_meme_endpoint():
    return GetOneMeme()


@pytest.fixture()
def post_meme_endpoint():
    return PostNewMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def new_meme_id():
    body = {
        'text': 'Text',
        'url': '',
        'tags': [],
        'info': {
            'colors': ['', ''],
            'objects': ['', '']
        }
    }
    headers = {'Authorization': cred.TOKEN}
    response = requests.post(f'{cred.API_URL}/meme', json=body, headers=headers)
    meme_id = response.json()['id']
    yield meme_id
    requests.delete(f'{cred.API_URL}/meme/{meme_id}', headers=headers)


@pytest.fixture()
def make_changes_in_meme_endpoint():
    return PutChangesMeme()


@pytest.fixture(scope='session')
def start_end_testing():
    print('\nStart testing')
    yield

    print('\nTesting completed')
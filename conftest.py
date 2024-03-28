import pytest
import requests
import os
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
        create_new_auth_token_endpoint.create_new_auth_token_and_rewrite()
        return None


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
        'text': 'Python logo reveals',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    }
    headers = {'Authorization': os.getenv('TOKEN')}
    response = requests.post(f'{os.getenv('API_URL')}/meme', json=body, headers=headers)
    meme_id = response.json()['id']
    yield meme_id
    requests.delete(f'{os.getenv('API_URL')}/meme/{meme_id}', headers=headers)


@pytest.fixture()
def make_changes_in_meme_endpoint():
    return PutChangesMeme()

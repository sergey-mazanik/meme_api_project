import pytest
import requests
from endpoints.create_new_auth_token import CreateNewAuthToken
from endpoints.get_alive_auth_token import GetAliveAuthToken
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_one_meme import GetOneMeme
from endpoints.post_meme import PostNewMeme


@pytest.fixture()
def create_new_auth_token_endpoint():
    return CreateNewAuthToken()


@pytest.fixture()
def get_alive_token_endpoint():
    return GetAliveAuthToken()


@pytest.fixture()
def use_or_create_new_auth_token(get_alive_token_endpoint, create_new_auth_token_endpoint):
    if get_alive_token_endpoint.get_alive_token():
        return True
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
def create_meme():
    ...
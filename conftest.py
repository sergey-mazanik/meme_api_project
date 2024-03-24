import pytest
import requests
from endpoints.create_new_auth_token import CreateNewAuthToken
from endpoints.get_alive_auth_token import GetAliveAuthToken
from endpoints.get_all_memes import GetAllMemes


@pytest.fixture()
def create_new_auth_token():
    return CreateNewAuthToken()


@pytest.fixture()
def get_alive_token():
    return GetAliveAuthToken()


@pytest.fixture()
def use_or_create_new_auth_token(get_alive_token, create_new_auth_token):
    if get_alive_token.get_alive_token():
        return True
    else:
        create_new_auth_token.create_new_auth_token()


@pytest.fixture()
def get_all_memes():
    return GetAllMemes()



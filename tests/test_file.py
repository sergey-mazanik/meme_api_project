import pytest
from endpoints.endpoint import Endpoint


def test_create_token():
    endpoint = Endpoint()
    endpoint.get_authorize_token()

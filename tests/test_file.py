import pytest
from test_data import TEST_BODY_FOR_NEW_MEME_POSITIVE, TEST_BODY_FOR_NEW_MEME_NEGATIVE, TEST_BODY_FOR_UPDATE_MEME


def test_get_memes(use_or_create_new_auth_token, get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes_list()
    get_all_memes_endpoint.check_that_status_is_200()


def test_get_one_meme(use_or_create_new_auth_token, get_one_meme_endpoint, new_meme_id):
    get_one_meme_endpoint.get_one_meme(new_meme_id)
    get_one_meme_endpoint.check_that_status_is_200()


@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_positive(use_or_create_new_auth_token, post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(body=data)
    post_meme_endpoint.check_that_status_is_200()
    delete_meme_endpoint.clear_data_after_testing()


@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_with_empty_auth_token(post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(body=data)
    post_meme_endpoint.check_that_status_is_401()
    delete_meme_endpoint.clear_data_after_testing()


@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_with_incorrect_auth_token(post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(body=data, headers={'Authorization': 'incorrectToken'})
    post_meme_endpoint.check_that_status_is_401()
    delete_meme_endpoint.clear_data_after_testing()


@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_with_empty_auth_token(post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme_without_auth_token(body=data)
    post_meme_endpoint.check_that_status_is_401()
    delete_meme_endpoint.clear_data_after_testing()


@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_NEGATIVE)
def test_post_meme_negative(use_or_create_new_auth_token, post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(body=data)
    post_meme_endpoint.check_that_status_is_400()
    delete_meme_endpoint.clear_data_after_testing()


def test_post_meme_without_body(use_or_create_new_auth_token, post_meme_endpoint, delete_meme_endpoint):
    post_meme_endpoint.post_new_meme()
    post_meme_endpoint.check_that_status_is_400()
    delete_meme_endpoint.clear_data_after_testing()


@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME)
def test_update_meme_positive(use_or_create_new_auth_token, make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_200()


def test_delete_meme(use_or_create_new_auth_token, new_meme_id, delete_meme_endpoint, get_one_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.get_one_meme(new_meme_id)
    get_one_meme_endpoint.check_that_status_is_404()


def test_delete_meme_with_incorrect_auth_token(new_meme_id, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id, headers={'Authorization': 'incorrectToken'})
    delete_meme_endpoint.check_that_status_is_401()


def test_delete_meme_with_empty_auth_token(new_meme_id, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme_without_auth_token(new_meme_id)
    delete_meme_endpoint.check_that_status_is_401()


def authorize_without_body():
    ...

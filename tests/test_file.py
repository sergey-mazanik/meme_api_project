import pytest
from test_data import (TEST_BODY_FOR_NEW_MEME_POSITIVE, TEST_BODY_FOR_NEW_MEME_NEGATIVE,
                       TEST_BODY_FOR_UPDATE_MEME_POSITIVE, TEST_BODY_FOR_UPDATE_MEME_NEGATIVE_WITHOUT_ID,
                       TEST_BODY_FOR_UPDATE_MEME_NEGATIVE, TEST_BODY_FOR_CREATING_AUTH_TOKEN,
                       TEST_BODY_FOR_UPDATE_MEME_WITHOUT_PERMISSION)


def test_get_alive_auth_token(use_or_create_new_auth_token, get_alive_token_endpoint):
    get_alive_token_endpoint.get_alive_token()
    get_alive_token_endpoint.check_that_status_is_200()


def test_get_alive_incorrect_token(use_or_create_new_auth_token, get_alive_token_endpoint):
    get_alive_token_endpoint.get_alive_incorrect_token()
    get_alive_token_endpoint.check_that_status_is_404()


def test_create_auth_token_positive(create_new_auth_token_endpoint):
    create_new_auth_token_endpoint.create_new_auth_token_positive()
    create_new_auth_token_endpoint.check_that_status_is_200()


@pytest.mark.parametrize('data', TEST_BODY_FOR_CREATING_AUTH_TOKEN)
def test_create_auth_token_negative(create_new_auth_token_endpoint, data):
    create_new_auth_token_endpoint.create_new_auth_token_negative(body=data)
    create_new_auth_token_endpoint.check_that_status_is_400()


def test_create_auth_token_without_body(create_new_auth_token_endpoint):
    create_new_auth_token_endpoint.create_new_auth_token_negative()
    create_new_auth_token_endpoint.check_that_status_is_400()


def test_get_memes(use_or_create_new_auth_token, get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes_list()
    get_all_memes_endpoint.check_that_status_is_200()


def test_get_memes_with_empty_auth_token(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes_without_auth_token()
    get_all_memes_endpoint.check_that_status_is_401()


def test_get_memes_with_incorrect_auth_token(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes_list(headers={'Authorization': 'incorrectToken'})
    get_all_memes_endpoint.check_that_status_is_401()


def test_get_one_meme(use_or_create_new_auth_token, get_one_meme_endpoint, new_meme_id):
    get_one_meme_endpoint.get_one_meme(new_meme_id)
    get_one_meme_endpoint.check_that_status_is_200()


def test_get_one_meme_with_empty_auth_token(get_one_meme_endpoint, new_meme_id):
    get_one_meme_endpoint.get_one_meme_without_auth_token(new_meme_id)
    get_one_meme_endpoint.check_that_status_is_401()


def test_get_one_meme_with_incorrect_auth_token(get_one_meme_endpoint, new_meme_id):
    get_one_meme_endpoint.get_one_meme(new_meme_id, headers={'Authorization': 'incorrectToken'})
    get_one_meme_endpoint.check_that_status_is_401()


@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_positive(use_or_create_new_auth_token, post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(body=data)
    post_meme_endpoint.check_that_status_is_200()
    delete_meme_endpoint.clear_data_after_testing()


@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_with_incorrect_auth_token(post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(body=data, headers={'Authorization': 'incorrectToken'})
    post_meme_endpoint.check_that_status_is_401()
    delete_meme_endpoint.clear_data_after_testing()


@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_without_auth_token(post_meme_endpoint, delete_meme_endpoint, data):
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


@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_POSITIVE)
def test_update_meme_positive(use_or_create_new_auth_token, make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_200()


@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_WITHOUT_PERMISSION)
def test_update_meme_positive_without_permission(use_or_create_new_auth_token, make_changes_in_meme_endpoint, data,
                                                 new_meme_id=1):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_403()


@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_POSITIVE)
def test_update_meme_with_incorrect_auth_token(make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data,
                                                       headers={'Authorization': 'incorrectToken'})
    make_changes_in_meme_endpoint.check_that_status_is_401()


@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_POSITIVE)
def test_update_meme_without_auth_token(make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme_without_auth_token(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_401()


@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_NEGATIVE)
def test_update_meme_negative(use_or_create_new_auth_token, make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_400()


def test_update_meme_without_body(use_or_create_new_auth_token, make_changes_in_meme_endpoint, new_meme_id):
    make_changes_in_meme_endpoint.make_changes_in_meme_without_id(new_meme_id)
    make_changes_in_meme_endpoint.check_that_status_is_400()


@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_NEGATIVE_WITHOUT_ID)
def test_update_meme_without_id(use_or_create_new_auth_token, make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme_without_id(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_400()


def test_delete_meme(use_or_create_new_auth_token, new_meme_id, delete_meme_endpoint, get_one_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.get_one_meme(new_meme_id)
    get_one_meme_endpoint.check_that_status_is_404()


def test_delete_meme(use_or_create_new_auth_token, delete_meme_endpoint, get_one_meme_endpoint, new_meme_id=1):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_that_status_is_403()


def test_delete_meme_with_incorrect_auth_token(new_meme_id, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id, headers={'Authorization': 'incorrectToken'})
    delete_meme_endpoint.check_that_status_is_401()


def test_delete_meme_with_empty_auth_token(new_meme_id, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme_without_auth_token(new_meme_id)
    delete_meme_endpoint.check_that_status_is_401()

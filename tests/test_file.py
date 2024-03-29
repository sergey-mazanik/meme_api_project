import pytest
import allure
from test_data import (TEST_BODY_FOR_NEW_MEME_POSITIVE, TEST_BODY_FOR_NEW_MEME_NEGATIVE,
                       TEST_BODY_FOR_UPDATE_MEME_POSITIVE, TEST_BODY_FOR_UPDATE_MEME_NEGATIVE_WITHOUT_ID,
                       TEST_BODY_FOR_UPDATE_MEME_NEGATIVE, TEST_BODY_FOR_CREATING_AUTH_TOKEN,
                       TEST_BODY_FOR_UPDATE_MEME_WITHOUT_PERMISSION)


@allure.epic('Token')
@pytest.mark.before_testing
def test_check_alive_or_override_auth_token(get_alive_token_endpoint, create_new_auth_token_endpoint):
    if get_alive_token_endpoint.get_alive_token() == 200:
        return None
    else:
        create_new_auth_token_endpoint.create_new_auth_token_and_rewrite()
        return None


@allure.epic('Token')
@pytest.mark.positive
def test_get_alive_auth_token(get_alive_token_endpoint):
    get_alive_token_endpoint.get_alive_token()
    get_alive_token_endpoint.check_that_status_is_200()


@allure.epic('Token')
@pytest.mark.negative
def test_get_alive_incorrect_token(get_alive_token_endpoint):
    get_alive_token_endpoint.get_alive_incorrect_token()
    get_alive_token_endpoint.check_that_status_is_404()


@allure.epic('Token')
@pytest.mark.positive
def test_create_auth_token_positive(create_new_auth_token_endpoint):
    create_new_auth_token_endpoint.create_new_auth_token_positive()
    create_new_auth_token_endpoint.check_that_status_is_200()
    create_new_auth_token_endpoint.check_that_token_is_new()


@allure.epic('Token')
@pytest.mark.negative
@pytest.mark.parametrize('data', TEST_BODY_FOR_CREATING_AUTH_TOKEN)
def test_create_auth_token_negative(create_new_auth_token_endpoint, data):
    create_new_auth_token_endpoint.create_new_auth_token_negative(body=data)
    create_new_auth_token_endpoint.check_that_status_is_400()


@allure.epic('Token')
@pytest.mark.negative
def test_create_auth_token_without_body(create_new_auth_token_endpoint):
    create_new_auth_token_endpoint.create_new_auth_token_negative()
    create_new_auth_token_endpoint.check_that_status_is_400()


@allure.story('Get meme')
@allure.epic('Memes')
@pytest.mark.positive
def test_get_memes(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes_list()
    get_all_memes_endpoint.check_that_status_is_200()
    get_all_memes_endpoint.check_that_meme_list_is_not_empty()


@allure.story('Get meme')
@allure.epic('Memes')
@pytest.mark.negative
def test_get_memes_with_empty_auth_token(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes_without_auth_token()
    get_all_memes_endpoint.check_that_status_is_401()


@allure.story('Get meme')
@allure.epic('Memes')
@pytest.mark.negative
def test_get_memes_with_incorrect_auth_token(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes_list(headers={'Authorization': 'incorrectToken'})
    get_all_memes_endpoint.check_that_status_is_401()


@allure.story('Get meme')
@allure.epic('Memes')
@pytest.mark.positive
def test_get_one_meme(get_one_meme_endpoint, new_meme_id):
    get_one_meme_endpoint.get_one_meme(new_meme_id)
    get_one_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.check_that_response_meme_id_is_correct(new_meme_id)


@allure.story('Get meme')
@allure.epic('Memes')
@pytest.mark.negative
def test_get_one_meme_with_empty_auth_token(get_one_meme_endpoint, new_meme_id):
    get_one_meme_endpoint.get_one_meme_without_auth_token(new_meme_id)
    get_one_meme_endpoint.check_that_status_is_401()


@allure.story('Get meme')
@allure.epic('Memes')
@pytest.mark.negative
def test_get_one_meme_with_incorrect_auth_token(get_one_meme_endpoint, new_meme_id):
    get_one_meme_endpoint.get_one_meme(new_meme_id, headers={'Authorization': 'incorrectToken'})
    get_one_meme_endpoint.check_that_status_is_401()


@allure.story('Create meme')
@allure.epic('Memes')
@pytest.mark.positive
@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_positive(post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(body=data)
    post_meme_endpoint.check_that_status_is_200()
    post_meme_endpoint.check_that_author_is_correct()
    post_meme_endpoint.check_that_response_text_is_correct(data)
    delete_meme_endpoint.clear_data_after_testing()


@allure.story('Create meme')
@allure.epic('Memes')
@pytest.mark.negative
@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_with_incorrect_auth_token(post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(body=data, headers={'Authorization': 'incorrectToken'})
    post_meme_endpoint.check_that_status_is_401()
    delete_meme_endpoint.clear_data_after_testing()


@allure.story('Create meme')
@allure.epic('Memes')
@pytest.mark.negative
@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_POSITIVE)
def test_post_meme_without_auth_token(post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme_without_auth_token(body=data)
    post_meme_endpoint.check_that_status_is_401()
    delete_meme_endpoint.clear_data_after_testing()


@allure.story('Create meme')
@allure.epic('Memes')
@pytest.mark.negative
@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME_NEGATIVE)
def test_post_meme_negative(post_meme_endpoint, delete_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(body=data)
    post_meme_endpoint.check_that_status_is_400()
    delete_meme_endpoint.clear_data_after_testing()


@allure.story('Create meme')
@allure.epic('Memes')
@pytest.mark.negative
def test_post_meme_without_body(post_meme_endpoint, delete_meme_endpoint):
    post_meme_endpoint.post_new_meme()
    post_meme_endpoint.check_that_status_is_400()
    delete_meme_endpoint.clear_data_after_testing()


@allure.story('Update meme')
@allure.epic('Memes')
@pytest.mark.positive
@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_POSITIVE)
def test_update_meme_positive(make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_200()
    make_changes_in_meme_endpoint.check_that_author_is_correct()
    make_changes_in_meme_endpoint.check_that_response_text_is_correct(data)


@allure.story('Update meme')
@allure.epic('Memes')
@pytest.mark.negative
@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_WITHOUT_PERMISSION)
def test_update_meme_positive_without_permission(make_changes_in_meme_endpoint, data, new_meme_id=1):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_403()


@allure.story('Update meme')
@allure.epic('Memes')
@pytest.mark.negative
@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_POSITIVE)
def test_update_meme_with_incorrect_auth_token(make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data,
                                                       headers={'Authorization': 'incorrectToken'})
    make_changes_in_meme_endpoint.check_that_status_is_401()


@allure.story('Update meme')
@allure.epic('Memes')
@pytest.mark.negative
@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_POSITIVE)
def test_update_meme_without_auth_token(make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme_without_auth_token(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_401()


@allure.story('Update meme')
@allure.epic('Memes')
@pytest.mark.negative
@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_NEGATIVE)
def test_update_meme_negative(make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_400()


@allure.story('Update meme')
@allure.epic('Memes')
@pytest.mark.negative
def test_update_meme_without_body(make_changes_in_meme_endpoint, new_meme_id):
    make_changes_in_meme_endpoint.make_changes_in_meme_without_id(new_meme_id)
    make_changes_in_meme_endpoint.check_that_status_is_400()


@allure.story('Update meme')
@allure.epic('Memes')
@pytest.mark.negative
@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME_NEGATIVE_WITHOUT_ID)
def test_update_meme_without_id(make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme_without_id(new_meme_id, body=data)
    make_changes_in_meme_endpoint.check_that_status_is_400()


@allure.story('Delete meme')
@allure.epic('Memes')
@pytest.mark.positive
def test_delete_meme(new_meme_id, delete_meme_endpoint, get_one_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.get_one_meme(new_meme_id)
    get_one_meme_endpoint.check_that_status_is_404()


@allure.story('Delete meme')
@allure.epic('Memes')
@pytest.mark.negative
def test_delete_foreign_meme(delete_meme_endpoint, get_one_meme_endpoint, new_meme_id=1):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_that_status_is_403()


@allure.story('Delete meme')
@allure.epic('Memes')
@pytest.mark.negative
def test_delete_meme_with_incorrect_auth_token(new_meme_id, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(new_meme_id, headers={'Authorization': 'incorrectToken'})
    delete_meme_endpoint.check_that_status_is_401()


@allure.story('Delete meme')
@allure.epic('Memes')
@pytest.mark.negative
def test_delete_meme_with_empty_auth_token(new_meme_id, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme_without_auth_token(new_meme_id)
    delete_meme_endpoint.check_that_status_is_401()

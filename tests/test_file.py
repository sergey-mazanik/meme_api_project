import pytest

TEST_BODY_FOR_NEW_MEME = [
    {
        'text': '',
        'url': '',
        'tags': [],
        'info': {
            'colors': ['', ''],
            'objects': ['', '']
        }
    }
]

TEST_BODY_FOR_UPDATE_MEME = [
    {
        'id': 155,
        'text': '',
        'url': '',
        'tags': [],
        'info': {
            'colors': ['', ''],
            'objects': ['', '']
        }
    }
]


# def test_get_memes(use_or_create_new_auth_token, get_all_memes_endpoint):
#     get_all_memes_endpoint.get_all_memes_list()
#
#
# def test_get_one_meme(use_or_create_new_auth_token, get_one_meme_endpoint, new_meme_id):
#     get_one_meme_endpoint.get_one_meme(new_meme_id)
#
#
# @pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME)
# def test_post_meme(use_or_create_new_auth_token, post_meme_endpoint, delete_meme_endpoint, data):
#     post_meme_endpoint.post_new_meme(body=data)
#     delete_meme_endpoint.clear_data_after_testing()


@pytest.mark.parametrize('data', TEST_BODY_FOR_UPDATE_MEME)
def test_update_meme(use_or_create_new_auth_token, make_changes_in_meme_endpoint, new_meme_id, data):
    make_changes_in_meme_endpoint.make_changes_in_meme(new_meme_id, body=data)

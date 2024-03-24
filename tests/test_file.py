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

def test_get_memes(use_or_create_new_auth_token, get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes_list()


def test_get_one_meme(use_or_create_new_auth_token, get_one_meme_endpoint):
    get_one_meme_endpoint.get_one_meme(48)


@pytest.mark.parametrize('data', TEST_BODY_FOR_NEW_MEME)
def test_post_meme(use_or_create_new_auth_token, post_meme_endpoint, data):
    post_meme_endpoint.post_new_meme(data)

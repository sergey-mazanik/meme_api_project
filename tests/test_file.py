import pytest


def test_get_memes(use_or_create_new_auth_token, get_all_memes):
    get_all_memes.get_all_memes_list()

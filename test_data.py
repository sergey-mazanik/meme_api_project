TEST_BODY_FOR_CREATING_AUTH_TOKEN = [
    {'name': None},
    {'name': 1},
    {'name': ''},
    {}
]

TEST_BODY_FOR_NEW_MEME_POSITIVE = [
    {
        'text': 'Python logo reveals',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    }
]

TEST_BODY_FOR_NEW_MEME_NEGATIVE = [
    {
        'text': None,
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    },
    {
        'text': 'Python logo reveals',
        'url': None,
        'tags': ['IT'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    },
    {
        'text': 'Python logo reveals',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': 'IT',
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    },
    {
        'text': 'Python logo reveals',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': None,
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    },
    {
        'text': 'Python logo reveals',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT'],
        'info': ['colors', ['blue', 'yellow'], 'objects', ['python', 'chair']]
    },
    {
        'text': 'Python logo reveals',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT'],
        'info': None
    },
    {
        'text': 'Python logo reveals',
        'url': 1,
        'tags': ['IT'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    },
    {
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    },
    {
        'text': 'Python logo reveals',
        'tags': ['IT'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    },
    {
        'text': 'Python logo reveals',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair']
        }
    },
    {
        'text': 'Python logo reveals',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT'],
    },
    {},
    []
]

TEST_BODY_FOR_UPDATE_MEME_POSITIVE = [
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    }
]

TEST_BODY_FOR_UPDATE_MEME_WITHOUT_PERMISSION = [
    {
        'id': '1',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    }
]

TEST_BODY_FOR_UPDATE_MEME_NEGATIVE = [
    {
        'id': '',
        'text': None,
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': '',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': None,
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 1,
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': {'IT': ['memes', 'python']},
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': None,
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': [
            'colors', ['blue', 'yellow'],
            'objects', ['python', 'chair', 'laptop']
        ]
    },
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': None
    },
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
    },
    {}
]

TEST_BODY_FOR_UPDATE_MEME_NEGATIVE_WITHOUT_ID = [
    {
        'id': '',
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': None,
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'id': 1,
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    },
    {
        'text': 'Python logo reveals how to sit whole coding',
        'url': 'https://preview.redd.it/44aw5j979ve61.png?auto=webp&s=a0285d3a6e42e88b15bd738bc483412bb3efb019',
        'tags': ['IT', 'memes', 'python'],
        'info': {
            'colors': ['blue', 'yellow'],
            'objects': ['python', 'chair', 'laptop']
        }
    }
]

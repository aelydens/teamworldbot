from app.cody import add_two
from app.emoji_class import emoji_it


def test_add_two():
    assert 5 == add_two(3)

def test_encryption_1():
    emojifier = emoji_it()
    assert 5 == emojifier.encrypt("hello")

from app.emoji_class import emoji_it


def test_encryption_1():
    emojifier = emoji_it()
    assert emojifier.encrypt("hello") == '📍🐓😥😥🥪'

#test for handling spaces and punctuation
def test_encryption_2():
    emojifier = emoji_it()
    assert emojifier.encrypt("um ! ?") == '🏫⛵ ! ?'

#test to ensure unidentified characters are not encoded
def test_chinese_korean():
    emojifier = emoji_it()
    assert emojifier.encrypt("漢字ㄲ, ㄸ, ㅃ, ㅆ, ㅉ") == '漢字ㄲ, ㄸ, ㅃ, ㅆ, ㅉ'

#test encrypting numbers
def test_numbers():
    emojifier = emoji_it()
    assert emojifier.encrypt("806-672-3455") == '⛷🤘🕡-🕡🕕🤘🏻-🤘🏾🤘🏼🤘🏽🤘🏽'
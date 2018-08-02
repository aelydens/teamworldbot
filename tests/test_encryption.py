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

#testing empty input
def test_empty_input():
    emojifier = emoji_it()
    assert emojifier.encrypt('') == ''

#testing multiline input
def test_multiline_input():
    emojifier = emoji_it()
    input = "You work that you may keep pace\nwith the earth\nand the soul of the earth."
    expected_output ="🔀🥪🏫 ✂🥪🦕👟 🧣📍🚀🧣 📜🥪🏫 ⛵🚀📜 👟🐓🐓🛰 🛰🚀🎢🐓\n✂🏉🧣📍 🧣📍🐓 🐓🚀🦕🧣📍\n🚀🍶🤣 🧣📍🐓 🎷🥪🏫😥 🥪🌹 🧣📍🐓 🐓🚀🦕🧣📍."

    assert emojifier.encrypt(input) == expected_output

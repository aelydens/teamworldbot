from app.emoji_class import emoji_it

def test_decryption_1():
    emojifier = emoji_it()
    assert emojifier.decrypt('📍🐓😥😥🥪') == 'hello'

#test for handling spaces and punctuation
def test_decryption_2():
    emojifier = emoji_it()
    assert emojifier.decrypt('🏫⛵ ! ?') == "um ! ?"

#test to ensure unidentified characters are not encoded
def test_de_chinese_korean():
    emojifier = emoji_it()
    assert emojifier.decrypt("漢字ㄲ, ㄸ, ㅃ, ㅆ, ㅉ") == '漢字ㄲ, ㄸ, ㅃ, ㅆ, ㅉ'

#test decrypting numbers
def test_de_numbers():
    emojifier = emoji_it()
    assert emojifier.decrypt('🛩💀🙂-🙂🎰🛷-😴😪🙁🙁') == "806-672-3455"

#testing Cody's parsing ':'
def test_dreaded_colon():
    emojifier = emoji_it()
    assert emojifier.decrypt(':hey::') == ":hey::"

#testing empty input
def test_empty_input():
    emojifier = emoji_it()
    assert emojifier.decrypt('') == ''

#testing multiline input
def test_multiline_input():
    emojifier = emoji_it()
    expected = "And if you sing\nthough as angels"
    assert emojifier.decrypt('🙈🍶🤣 🏉🌹 📜🥪🏫 🎷🏉🍶🏵\n🧣📍🥪🏫🏵📍 🚀🎷 🚀🍶🏵🐓😥🎷') == expected

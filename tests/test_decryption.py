from app.emoji_class import emoji_it

def test_decryption_1():
    emojifier = emoji_it()
    assert emojifier.decrypt('📍🐓😥😥🥪') == 'hello'

#test for handling spaces and punctuation
def test_decryption_2():
    emojifier = emoji_it()
    assert emojifier.decrypt('🏫⛵ ! ?') == "um ! ?"

#test to ensure only alphabet and numbers are encoded #besides : which is used in to mark spaces in decryption
def test_de_nonAlphabet_or_numbers():
    emojifier = emoji_it()
    assert emojifier.decrypt("!!!, @, #, $, % ^ & * () _ + - ` ; ' . , / ? | [ ] { } ") == "!!!, @, #, $, % ^ & * () _ + - ` ; ' . , / ? | [ ] { } "

#test decrypting numbers
def test_de_numbers():
    emojifier = emoji_it()
    assert emojifier.decrypt('⛷🤘🕡-🕡🕕🤘🏻-🤘🏾🤘🏼🤘🏽🤘🏽') == "806-672-3455"

#testing empty input
def test_empty_input():
    emojifier = emoji_it()
    assert emojifier.decrypt('') == ''

#testing multiline input
def test_multiline_input():
    emojifier = emoji_it()
    expected = ["And if you sing","though as angels"]
    input_lines =['🙈🍶🤣 🏉🌹 📜🥪🏫 🎷🏉🍶🏵', '🧣📍🥪🏫🏵📍 🚀🎷 🚀🍶🏵🐓😥🎷' ]
    
    for i in range (len(expected)):
        assert emojifier.decrypt(input_lines[i])  == expected[i]

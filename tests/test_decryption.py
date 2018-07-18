from app.emoji_class import emoji_it


def test_decryption_1():
    emojifier = emoji_it()
    assert emojifier.decrypt('📍🐓😥😥🥪') == 'hello'

# #test for handling spaces and punctuation
# def test_decryption_2():
#     emojifier = emoji_it()
#     assert emojifier.decrypt(u':school::sailboat: ! ?') == "um ! ?"

# #test to ensure unidentified characters are not encoded
# def test_de_chinese_korean():
#     emojifier = emoji_it()
#     assert emojifier.decrypt("漢字ㄲ, ㄸ, ㅃ, ㅆ, ㅉ") == '漢字ㄲ, ㄸ, ㅃ, ㅆ, ㅉ'

# #test decrypting numbers
# def test_de_numbers():
#     emojifier = emoji_it()
#     assert emojifier.decrypt(':skier::sign_of_the_horns::six-thirty:-:six-thirty::six_o’clock::sign_of_the_horns_light_skin_tone:-:sign_of_the_horns_medium-dark_skin_tone::sign_of_the_horns_medium-light_skin_tone::sign_of_the_horns_medium_skin_tone::sign_of_the_horns_medium_skin_tone:') == "806-672-3455"

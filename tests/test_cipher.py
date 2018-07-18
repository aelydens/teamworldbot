from app.emoji_class import emoji_it


#simple sanity check
def test_default_sanity():
    cipher = emoji_it()

    assert cipher.emoji_key == ':rocket:'
    assert cipher.multiplier == 1

#Test that each character gets mapped to a different emoji.
def test_cipher_duplicate():
    cipher = emoji_it()
    cipher.multiplier = 2623 #number of emojis

    #create cipher dictionary
    cipher_dict = cipher.define_cipher()
    
    for value in cipher_dict.values():
        counter = 0

        for value2 in cipher_dict.values():
            if value == value2:
                counter += 1
        
        assert counter == 1 #value should only match value2 once per iteration
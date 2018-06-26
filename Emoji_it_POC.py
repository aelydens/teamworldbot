__author__ = 'jcovino'
# !/usr/bin/env python
# Python 2.7

from sys import argv
import emoji
import string


def define_cipher(emoji_key, emoji_list):
    #define the alphabet to emoji symboles dictionary for caesar cipher

    cipher_dict = {}
    start_alphabet = emoji_list.index(emoji_key)
    alphabet = string.ascii_lowercase

    count = 0
    for letter in alphabet:
        emoji_index = (start_alphabet + count) % len(emoji_list)
        cipher_dict[letter] = emoji_list[emoji_index]
        count += 1
    cipher_dict[' '] = ' '

    return cipher_dict


def encrypt(message, emoji_key, emoji_list):
    # Simple Ceasar Cypher, the emoji-key index position marks 'a', the rest of the alphabet is defined from starting index 'a'

    print 'Encrpyting----> ', message

    cipher = define_cipher(emoji_key, emoji_list)
    encrypt_message_list=[]
    for letter in list(message.lower()):
        encrypt_message_list.append(cipher[letter])

    for emoj in encrypt_message_list:
        print (emoji.emojize(emoj, use_aliases=True)),

    return encrypt_message_list


def decrypt (message, emoji_key, emoji_list):
    # Simple Ceasar Cypher, the emoji-key index position marks 'a', the rest of the alphabet is defined from starting index 'a'
    # cipher dict is regenerated as in Encrpyt, but then key value pairs are reversed

    print
    print
    print 'Decrypting----> '
    cipher = define_cipher(emoji_key, emoji_list)

    #reverse the cipher
    rev_cipher = {v: k for k, v in cipher.iteritems()}

    decrypted = []
    for symbol in message:
        decrypted.append(rev_cipher[symbol])

    print ''.join(decrypted)

def main(argv):

    test_string = 'shine on you crazy diamond Syd '

    #3415 emoji's in EmojiList
    emoji_list = list(emoji.EMOJI_ALIAS_UNICODE)
    emoji_key = ':bee:'

    encrypted_message = encrypt(test_string, emoji_key, emoji_list)

    decrypt(encrypted_message,emoji_key, emoji_list)


if __name__ == "__main__":
    main(argv)

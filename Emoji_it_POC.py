__author__ = 'jcovino'
# !/usr/bin/env python
# Python 2.7

from sys import argv
import emoji
import string

class emoji_it:
    def __init__(self, input_string, input_key, multiplier=1):
        self.alphabet = string.ascii_lowercase
        self.emoji_list = list(emoji.EMOJI_ALIAS_UNICODE)
        self.multiplier = multiplier
        self.emoji_key = input_key
        self.message = input_string.lower()
        self.encrypted_message = 'na, does not exist yet'


    def define_cipher(self):
        #define the alphabet to emoji symbols dictionary for caesar cipher
        # multiplier allows for offseting alphabet, i.e. A=index 1, b=index 3, c = index 5, instead of ABC= index 1,2,3

        cipher_dict = {}
        start_alphabet = self.emoji_list.index(self.emoji_key)


        count = 0
        for letter in self.alphabet:
            emoji_index = ((start_alphabet + count) * self.multiplier) % len(self.emoji_list)
            cipher_dict[letter] = self.emoji_list[emoji_index]
            count += 1

        return cipher_dict


    def encrypt(self):
        # Simple Ceasar Cypher, the emoji-key index position marks 'a',
        # the rest of the alphabet is defined from starting index 'a'

        print 'Encrpyting----> ', self.message

        # Define the cipher dictionary, assign letter -> emoji
        cipher = self.define_cipher()

        encrypted_message=[]
        for letter in list(self.message):
            if letter in cipher:
                encrypted_message.append(cipher[letter])
            else:
                encrypted_message.append(letter)

        for emoj in encrypted_message:
            print (emoji.emojize(emoj, use_aliases=True)),

        self.encrypted_message = encrypted_message


    def decrypt(self):
        # Simple Ceasar Cypher, the emoji-key index position marks 'a', the rest of the alphabet is defined from starting index 'a'
        # cipher dict is regenerated as in Encrpyt, but then key value pairs are reversed

        print
        print
        print 'Decrypting----> '
        cipher = self.define_cipher()

        #reverse the cipher
        rev_cipher = {v: k for k, v in cipher.iteritems()}

        decrypted = []
        for symbol in self.encrypted_message:
            if symbol in rev_cipher:
                decrypted.append(rev_cipher[symbol])
            else:
                decrypted.append(symbol)

        print ''.join(decrypted)

def main(argv):

    input_text = 'Kambucha refill time'
    input_key = ':rocket:'
    multiplier = 2

    translate = emoji_it(input_text, input_key, multiplier)

    translate.encrypt()

    translate.decrypt()


if __name__ == "__main__":
    main(argv)

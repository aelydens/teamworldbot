# !/usr/local/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'jcovino'

import emoji
import string


class emoji_it:
    def __init__(self):
        self.alphabet_lower = string.ascii_lowercase
        self.aphabet_upper = string.ascii_uppercase
        self.numbers = [0,1,2,3,4,5,6,7,8,9]
        self.emoji_list = list(emoji.EMOJI_UNICODE)
        self.unicode_emoji = {v: k for k, v in iter(emoji.EMOJI_UNICODE.items())}

        self.cipher = None 
        # default multiplier
        self.multiplier = 1
        # default key
        self.emoji_key = ':rocket:'

    def define_cipher(self):
        #define the alphabet to emoji symbols dictionary for caesar cipher
        # multiplier allows for offseting alphabet, i.e. A=index 1, b=index 3, c = index 5, instead of ABC= index 1,2,3

        cipher_dict = {}
        start_alphabet = self.emoji_list.index(self.emoji_key)

        count = 0
        ## assign mapping for lower case
        for letter in self.alphabet_lower:
            emoji_index = ((start_alphabet + count) * int(self.multiplier)) % len(self.emoji_list)
            emoji_mapping = self.emoji_list[emoji_index]

            # check to see if emoji already exists in dictionary, if it does increment index by 1
            while emoji_mapping in cipher_dict.values():
                emoji_index += 1
                emoji_mapping = self.emoji_list[emoji_index]
            cipher_dict[letter] = emoji_mapping
            count += 1

        ## assign mapping for upper case
        for letter in self.aphabet_upper:
            emoji_index = ((start_alphabet + count) * int(self.multiplier)) % len(self.emoji_list)
            emoji_mapping = self.emoji_list[emoji_index]

            # check to see if emoji already exists in dictionary, if it does increment index by 1
            while emoji_mapping in cipher_dict.values():
                emoji_index += 1
                emoji_mapping = self.emoji_list[emoji_index]

            cipher_dict[letter] = emoji_mapping
            count += 1

        ## assign mapping for numbers
        for number in self.numbers:
            emoji_index = ((start_alphabet + count) * int(self.multiplier)) % len(self.emoji_list)
            emoji_mapping = self.emoji_list[emoji_index]

            # check to see if emoji already exists in dictionary, if it does increment index by 1
            while emoji_mapping in cipher_dict.values():
                emoji_index += 1
                emoji_mapping = self.emoji_list[emoji_index]

            cipher_dict[str(number)] = emoji_mapping
            count += 1

        return cipher_dict

    def encrypt(self, message):
        # Simple Ceasar Cypher, the emoji-key index position marks 'a',
        # the rest of the alphabet is defined from starting index 'a'
        # Define the cipher dictionary, assign letter -> emoji

        if self.cipher == None:
            self.cipher = self.define_cipher()
        encrypted_message=[]
        for letter in message:
            if letter in self.cipher:
                encrypted_message.append(self.cipher[letter])
            else:
                encrypted_message.append(letter)

        return encrypted_message

    def decrypt(self, encrypted_message):
        # Simple Ceasar Cypher, the emoji-key index position marks 'a', the rest of the alphabet is defined from starting index 'a'
        # cipher dict is regenerated as in Encrpyt, but then key value pairs are reversed
        if self.cipher == None:
            self.cipher = self.define_cipher()
        #reverse the cipher
        # rev_cipher = {v: k for k, v in cipher.iteritems()}
        # Python 3
        rev_cipher= {v: k for k, v in self.cipher.items()}
        decrypted = []

        for symbol in encrypted_message:
            if symbol == u'':
                symbol = ' '
            if symbol in rev_cipher:
                decrypted.append(rev_cipher[symbol])
            else:
                decrypted.append(symbol)

        return ''.join(decrypted)
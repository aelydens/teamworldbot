# !/usr/local/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'jcovino'

import emoji
import string
import re

class emoji_it:
    def __init__(self):
        self.alphabet_lower = string.ascii_lowercase
        self.aphabet_upper = string.ascii_uppercase
        self.numbers = list(range(0, 10, 1))

        self.unicode_emoji = {}  #******
        for key in emoji.EMOJI_UNICODE:
            val = emoji.EMOJI_UNICODE[key]
            emoji_string =''
            for item in val:
                emoji_string = emoji_string + item
            #if len(emoji.EMOJI_UNICODE[key]) == 1:
            self.unicode_emoji[key] = emoji_string

        #for item in self.unicode_emoji:
            #print (item, list(self.unicode_emoji[item]))
        
        #print (list(self.unicode_emoji[':sign_of_the_horns_dark_skin_tone:']))    

        self.emoji_list = list(self.unicode_emoji)
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

        #for item in cipher_dict:
            #print (item, cipher_dict[item]), list (cipher_dict[item])        
        return cipher_dict

    def encrypt(self, message):
        # Simple Ceasar Cypher, the emoji-key index position marks 'a',
        # the rest of the alphabet is defined from starting index 'a'
        # Define the cipher dictionary, assign letter -> emoji
        # returns encyrpted message in Emoji

        if self.cipher == None:
            self.cipher = self.define_cipher()             

        encrypted_message = ""
        for letter in message:
            if letter in self.cipher:
                encrypted_message += self.cipher[letter]
            else:
                encrypted_message += letter

        return emoji.emojize(encrypted_message, use_aliases=False)


    def decrypt(self, encrypted_message):
        # Simple Ceasar Cypher, the emoji-key index position marks 'a', the rest of the alphabet is defined from starting index 'a'
        # cipher dict is regenerated as in Encrpyt, but then key value pairs are reversed
        # returns decrypted message in text

        if self.cipher == None:
            self.cipher = self.define_cipher()

        # for item in self.cipher:
        #     print (item, self.cipher[item]), list(self.cipher[item])       

        #reverse the cipher
        rev_cipher= {v: k for k, v in self.cipher.items()}

  
        decrypted = []
        encrypted_message = (emoji.demojize(encrypted_message))

        # this handles the combination character emojis- like sign_of_the_horns_light_skin_tone
        # a space is designated with a ~
        # then lines are split based on :
        line = re.sub(' ', '~', encrypted_message)
        line = re.sub(':', ' ', line)
        line_list = (line.split())
        
        for symbol in line_list:
            mod_symbol = ':'+symbol+':'
            #print (mod_symbol)   
            if mod_symbol in rev_cipher:
                decrypted.append(rev_cipher[mod_symbol])
            elif mod_symbol == ':~:':
                decrypted.append(' ')
            elif mod_symbol == ':,~:':
                decrypted.append(', ')
            elif mod_symbol == ':~,:':
                 decrypted.append(' ,')    
            else:
                decrypted.append(symbol)

        return ''.join(decrypted)

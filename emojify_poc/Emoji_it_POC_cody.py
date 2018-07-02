__author__ = 'jcovino'
# !/usr/bin/env python
# Python 2.7
''' Run on the command line. Text file input is required. Encryption is only supported for one-line, so no newlines
encryption example: python Emoji_it_POC.py  -e 'test.txt'    (put text in file)
decryption example: python Emoji_it_POC.py  -d -i test.txt   (put emojis in file)
encryption key, and multiplier are optional-- if you want to pass messages in secret. There is a default
encryption key and multiplier'''


from sys import argv
import emoji
import string
import argparse
import sys



def parse_cmdline_params(arg_list = None):
    """Parses commandline arguments.
    :param arg_list: arguments from the command line
    :type arg_list: list
    :return: dictionary of options
    """
    description = "Description here"
    #Create instance of ArgumentParser
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-e",
                        "--encrypt_message",
                        dest='e',
                        action='store_true',
                        default=False,
                        required=False,
                        help="Encrpyt input text")

    parser.add_argument("-d",
                        "--decrypt_message",
                        dest='d',
                        action='store_true',
                        default=False,
                        required=False,
                        help="Decrpyt input text")

    parser.add_argument("-k",
                        "--encryption_key",
                        action='store',
                        dest='k',
                        default=False,
                        required=False,
                        type=str,
                        help="encryption key")

    parser.add_argument("-m",
                        "--encryption_multiplier",
                        action='store',
                        dest='m',
                        default=False,
                        required=False,
                        type=int,
                        help="encryption multiplier")

    parser.add_argument("-i",
                        "--input_file",
                        type=argparse.FileType('r'),
                        help="text file",
                        required=True,
                        default=False)


    # Parse options
    opts = parser.parse_args(args=arg_list)

    return opts


class emoji_it:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.emoji_list = list(emoji.EMOJI_UNICODE)
        self.unicode_emoji = {v: k for k, v in emoji.EMOJI_UNICODE.iteritems()}
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
        for letter in self.alphabet:
            emoji_index = ((start_alphabet + count) * int(self.multiplier)) % len(self.emoji_list)
            cipher_dict[letter] = self.emoji_list[emoji_index]
            count += 1
            #print(letter, cipher_dict[letter].encode("utf-8"))

        return cipher_dict


    def encrypt(self, message):
        # Simple Ceasar Cypher, the emoji-key index position marks 'a',
        # the rest of the alphabet is defined from starting index 'a'

        print
        print

        # Define the cipher dictionary, assign letter -> emoji
        cipher = self.define_cipher()

        encrypted_message=[]
        for letter in message:
            if letter in cipher:
                encrypted_message.append(cipher[letter])
            else:
                encrypted_message.append(letter)

        for emoj in encrypted_message:
            print emoji.emojize(emoj),

     


    def decrypt(self, encrypted_message):
        # Simple Ceasar Cypher, the emoji-key index position marks 'a', the rest of the alphabet is defined from starting index 'a'
        # cipher dict is regenerated as in Encrpyt, but then key value pairs are reversed

        print
        print
        cipher = self.define_cipher()
        #reverse the cipher
        rev_cipher = {v: k for k, v in cipher.iteritems()}
        decrypted = []

        for symbol in encrypted_message:

            '''  
            CODY : forcing u'' to be a literal space.
            '''
            if symbol == u'':
                symbol = ' '
            #print("hello:", symbol)
            if symbol in rev_cipher:
                decrypted.append(rev_cipher[symbol])
                
            else:
                decrypted.append(symbol)

        print(''.join(decrypted))

      

def main(argv):

    translate = emoji_it()

    opts = parse_cmdline_params(sys.argv[1:])
    
    with open(opts.input_file.name,"r") as fstream:
            input_text = fstream.readline()
  
    # If key provided: assign it
    if opts.k:
        translate.emoji_key = opts.k

    # If multiplier provided: assign it    
    if opts.m:
        translate.multiplier= opts.m  

    # If encryption selected: do it    
    if opts.e:
        translate.encrypt(input_text)
          

    #If decryption selected: do it 
    if opts.d:
        unicode_it = unicode(input_text, 'utf-8')
        '''  
        CODY : just added ' ' to split()
        '''
        escaped_unicode_list = unicode_it.split(' ')
        #escaped_unicode_list = list(input_text.decode("utf-8"))
        #print(escaped_unicode_list)
        decode_message=[]
        for code in escaped_unicode_list:
            if code in translate.unicode_emoji:
                decode_message.append(translate.unicode_emoji[code])
            else:
                decode_message.append(code)

        translate.decrypt(decode_message)
       
      




if __name__ == "__main__":
    main(argv)

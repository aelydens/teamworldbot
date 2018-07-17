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
import Emoji_class_commandline as emoji_class
import emoji

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

def main(argv):
    # create object of class
    translate = emoji_class.emoji_it()

    opts = parse_cmdline_params(sys.argv[1:])
    file_lines = []
    with open(opts.input_file.name,"r") as fstream:
        for line in fstream:
            file_lines.append(line.strip())
   
    # If key provided: assign it
    if opts.k:
        translate.emoji_key = opts.k

    # If multiplier provided: assign it    
    if opts.m:
        translate.multiplier= opts.m  

    # If encryption selected: do it    
    if opts.e:
        encrypted =[]
        for input_line in file_lines:
            encrypted.append(translate.encrypt(input_line))

        for encrypted_line in encrypted:
            #print ''.join(encrypted_line)
            for emoj in encrypted_line:
                print emoji.emojize(emoj),

    #If decryption selected: do it 
    if opts.d:
        for input_line in file_lines:
            unicode_it = unicode(input_line, 'utf-8')
            escaped_unicode_list = unicode_it.split(' ')
            decode_message=[]
            for code in escaped_unicode_list:
                if code in translate.unicode_emoji:
                    decode_message.append(translate.unicode_emoji[code])
                else:
                 decode_message.append(code)

            decrypted = translate.decrypt(decode_message)
            print decrypted

if __name__ == "__main__":
    main(argv)

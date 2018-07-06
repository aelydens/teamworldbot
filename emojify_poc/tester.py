#!/usr/bin/env python2
import Emoji_it_POC_cody

def test1():
    teststring = "hello world"
    print "encrypting: " + teststring 
    thing = Emoji_it_POC_cody.emoji_it()
    encrypted_version = thing.encrypt(teststring)
    print "Did it work?" 

test1()

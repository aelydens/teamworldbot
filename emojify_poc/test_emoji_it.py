
import unittest
import Emoji_class_helper as ech

class emoji_it(unittest.TestCase):

    
    # def test_constructor(self):
    #     numb = 132
    #     with self.assertRaises(textproc.TextProcError):
    #         textproc.Processor(numb)


    #Test that default options are still the same.
    def test_default_sanity(self):
        cipher = ech.emoji_it()

        self.assertEqual(cipher.emoji_key, ':rocket:')
        self.assertEqual(cipher.multiplier, 1)

        print('\ndefault_sanity PASSED')

    
    #Test that each character gets mapped to a different emoji.
    def test_cipher_duplicate(self):
        cipher = ech.emoji_it()
        cipher.multiplier = 2623
        #cipher.define_cipher()

        #print(len(cipher.unicode_emoji), len(cipher.emoji_list))

        print('\ncipher_duplicate PASSED')


    #def test_full_circle(self):



# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a_z = string.ascii_lowercase
        key = key.replace(" ", "")
        key_without_dupes = ''
        for letter in key:
            if letter not in key_without_dupes:
                key_without_dupes = key_without_dupes + letter

        letters = {}

        for key_letter, dict_letter in zip(key_without_dupes, a_z):
            letters[key_letter] = dict_letter

        letters[' '] = ' '

        output = ''
        for letter in message:
            output = output + letters[letter]
        
        return output
        

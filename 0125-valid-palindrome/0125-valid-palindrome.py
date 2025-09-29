class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for letter in s:
            if letter.isalnum():
                new_s += letter
        new_s = new_s.lower()
        new_s_reversed_list = reversed([letter for letter in new_s])
        new_s_reversed = ''
        for letter in new_s_reversed_list:
            new_s_reversed += letter
        if new_s == new_s_reversed:
            return True
        else:
            return False
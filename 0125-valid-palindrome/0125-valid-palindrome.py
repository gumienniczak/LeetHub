class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sentence = ""
        for char in s:
            if char.isalnum():
                sentence += char.lower()

        N = len(sentence)
        left = 0
        right = N - 1

        while left < right:
            if sentence[left] != sentence[right]:
                return False
            left += 1
            right -= 1
        
        return True
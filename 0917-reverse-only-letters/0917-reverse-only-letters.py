class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        beg = 0
        end = len(s) - 1
        output = ""
        for i in range(len(s)):
            if s[i].isalpha():
                while not s[end].isalpha():
                    end -=1
                output += s[end]
                end -= 1
            else:
                output += s[i]
        
        return output
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pars = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in pars:
                stack.append(char)
            else:
                if not stack or char != pars[stack.pop()]:
                    return False
                else:
                    continue
        
        return not stack
                   
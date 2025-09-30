class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for bracket in s:
            if bracket in mapping:
                stack.append(bracket)
            else:
                if not stack or mapping[stack.pop()] != bracket:
                    return False
                else:
                    continue
        return not stack
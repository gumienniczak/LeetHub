class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        S = len(s)
        T = len(t)

        if not s:
            return True
        
        if S > T:
            return False
        
        pointer = 0
        for i in range(T):
            if s[pointer] == t[i]:
                if pointer == S - 1:
                    return True
                pointer += 1
        
        return False
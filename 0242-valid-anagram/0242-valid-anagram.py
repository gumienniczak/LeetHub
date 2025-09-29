from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter_s = defaultdict(int)
        counter_t = defaultdict(int)

        for el in s:
            counter_s[el] += 1
        
        for el in t:
            counter_t[el] += 1
        
        return counter_s == counter_t
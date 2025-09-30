from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_counter = defaultdict(int)
        for char in s1:
            s1_counter[char] += 1
        
        left = 0
        cur_counter = defaultdict(int)
        N1 = len(s1)
        N2 = len(s2)
        for right in range(N2):
            cur_counter[s2[right]] += 1
            while right - left + 1 > N1:
                cur_counter[s2[left]] -= 1
                if cur_counter[s2[left]] == 0:
                    del cur_counter[s2[left]]
                left += 1
            if s1_counter == cur_counter:
                return True
        
        return False
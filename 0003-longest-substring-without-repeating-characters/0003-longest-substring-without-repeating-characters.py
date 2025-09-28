class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        ans = 0
        S = len(s)
        cur_chars = set()
        for right in range(S):
            while s[right] in cur_chars:
                cur_chars.remove(s[left])
                left += 1
            cur_chars.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans
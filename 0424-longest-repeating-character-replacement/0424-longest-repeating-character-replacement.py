class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        left = 0
        ans = 0
        counter = [0] * 26
        for right in range(N):
            counter[ord(s[right]) - 65] += 1
            while right - left + 1 - max(counter) > k:
                counter[ord(s[left]) - 65] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans

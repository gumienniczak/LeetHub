from collections import defaultdict
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
        counter = defaultdict(int)
        for right in range(N):
            counter[s[right]] += 1
            while right - left + 1 - max(counter.values()) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

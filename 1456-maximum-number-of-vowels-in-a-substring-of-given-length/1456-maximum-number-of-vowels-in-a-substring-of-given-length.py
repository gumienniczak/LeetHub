class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        ans = 0
        curr = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for right in range(len(s)):
            if s[right] in vowels:
                curr += 1
            while right - left + 1 == k:
                ans = max(ans, curr)
                if s[left] in vowels:
                    curr -= 1
                left += 1
        
        return ans
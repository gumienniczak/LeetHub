from collections import defaultdict
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        max_freq = max(counter.values())

        res = 0

        for key, val in counter.items():
            if val == max_freq:
                res += 1
        
        return res * max_freq
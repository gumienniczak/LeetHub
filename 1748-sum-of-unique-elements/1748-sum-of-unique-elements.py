from collections import defaultdict
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        res = 0
        
        for key, value in counter.items():
            if value == 1:
                res += key
        
        return res
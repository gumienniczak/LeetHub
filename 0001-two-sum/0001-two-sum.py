class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if num in seen:
                return (seen[num], idx)
            seen[diff] = idx
        
        print(seen)
        return None

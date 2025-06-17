class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_result = 0
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                diff = nums[i] - nums[j]
                if diff > max_result:
                    max_result = diff
        
        if not max_result:
            return -1
        else:
            return max_result
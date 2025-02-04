class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total_sum = 0

        for start_i in range(len(nums)):
            current_sum = nums[start_i]

            end_i = start_i + 1
            while end_i < len(nums) and nums[end_i] > nums[end_i - 1]:
                current_sum += nums[end_i]
                end_i += 1
            
            total_sum = max(total_sum, current_sum)
        
        return total_sum

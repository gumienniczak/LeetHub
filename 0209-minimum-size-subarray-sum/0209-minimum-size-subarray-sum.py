class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        ans = float("inf")
        cur_sum = 0
        N = len(nums)
        for right in range(N):
            cur_sum += nums[right]
            while cur_sum >= target:
                ans = min(ans, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
        return ans if ans != float("inf") else 0
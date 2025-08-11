class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = curr = 0
        ans = float('inf')

        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1

        if ans == float('inf'):
            return 0
        return ans
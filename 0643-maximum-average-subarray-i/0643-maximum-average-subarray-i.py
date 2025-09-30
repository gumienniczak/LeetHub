class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        N = len(nums)
        left = 0
        ans = float("-inf")
        cur_sum = 0
        for right in range(N):
            cur_sum += nums[right]
            size = right - left + 1
            if size == k:
                ans = max(ans, float(cur_sum) / float(k))
                cur_sum -= nums[left]
                left += 1
        
        return ans
from collections import defaultdict
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = defaultdict(int)
        left = 0
        ans = 0
        cur = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            while counter[nums[right]] > k:
                counter[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
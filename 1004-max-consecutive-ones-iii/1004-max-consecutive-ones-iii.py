from collections import defaultdict
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        left = 0
        ans = 0
        counter = defaultdict(int)
        for right in range(N):
            counter[nums[right]] += 1
            while counter[0] > k:
                counter[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
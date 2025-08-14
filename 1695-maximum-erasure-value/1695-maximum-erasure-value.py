class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        left = 0
        ans = 0
        last_seen = dict()
        for right in range(n):
            if nums[right] in last_seen:
                left = max(left, last_seen[nums[right]] + 1)

            last_seen[nums[right]] = right

            current_sum = prefix_sum[right + 1] - prefix_sum[left]
            ans = max(ans, current_sum)

        return ans
from collections import defaultdict
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        counter = defaultdict(int)
        counter[0] = 1
        cur_sum = 0
        ans = 0
        for num in nums:
            cur_sum += num
            diff = cur_sum - goal
            ans += counter[diff]
            counter[cur_sum] += 1
        
        return ans
        
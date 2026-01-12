class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                longest = 1
                cur_num = num
                while cur_num + 1 in num_set:
                    cur_num += 1
                    longest += 1
                ans = max(ans, longest)
            else:
                continue
        
        return ans


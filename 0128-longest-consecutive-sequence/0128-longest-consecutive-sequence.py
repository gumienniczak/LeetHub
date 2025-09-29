class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        chars = set(nums)

        output = 0

        for num in chars:
            if num - 1 not in chars:
                next_num = num + 1
                length = 1
                while next_num in chars:
                    length += 1
                    next_num += 1
                output = max(output, length)
        
        return output

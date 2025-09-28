class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = float("inf")
        for num in nums:
            if abs(num) < abs(closest):
                closest = num
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        return closest
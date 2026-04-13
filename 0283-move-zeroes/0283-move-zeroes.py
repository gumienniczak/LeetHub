class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                counter += 1
            else:
                nums[i - counter], nums[i] = nums[i], nums[i - counter]
        
    

        
                
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        l_prod = 1
        r_prod = 1
        
        l_arr = [0] * N
        r_arr = [0] * N

        for i in range(N):
            j = -i - 1
            l_arr[i] = l_prod
            r_arr[j] = r_prod

            l_prod *= nums[i]
            r_prod *= nums[j]
        
        return [l*r for l, r in zip(l_arr, r_arr)]


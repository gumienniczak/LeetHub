class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        left_prod = [0] * n
        right_prod = [0] * n
        l_mult = 1
        r_mult = 1

        for i in range(n):
            j = -i - 1
            left_prod[i] = l_mult
            right_prod[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        
        return [left * right for left, right in zip(left_prod, right_prod)]
        
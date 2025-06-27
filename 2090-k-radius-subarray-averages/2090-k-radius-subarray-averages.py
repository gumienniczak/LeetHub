class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        output = [-1] * n
        prefix_sum = [0]
        
        rg = k * 2 + 1
        
        for i in range(n):
            prefix_sum.append(nums[i] + prefix_sum[-1])
            
        for i in range(rg, n + 1):
            s = prefix_sum[i] - prefix_sum[i - rg]
            res = s // rg
            output[i - (k + 1)] = res
            
        return output
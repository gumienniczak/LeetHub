class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        n = len(nums) - 1
        while i <= n:
            mid = (n + i) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                n = mid - 1
            else:
                i = mid + 1
        
        return -1
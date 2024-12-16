class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            index, num = min(enumerate(nums), key = lambda x: x[1])
            nums[index] = num * multiplier
            k -= 1
        return nums

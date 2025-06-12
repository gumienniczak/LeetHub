class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        first_el = nums[0]
        last_el = nums[-1]
        biggest_dif = abs(first_el - last_el)
        for i in range(len(nums) - 1):
            diff = abs(nums[i] - nums[i + 1])
            if diff > biggest_dif:
                biggest_dif = diff
        return biggest_dif
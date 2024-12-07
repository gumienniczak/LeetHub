class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def ispenaltyvalid(biggest_bag) -> bool:
            number_of_splits = 0
            for bag in nums:
                if bag > biggest_bag:
                    number_of_splits += (bag - 1) // biggest_bag
            return number_of_splits <= maxOperations
        
        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2
            if ispenaltyvalid(mid):
                right = mid
            else:
                left = mid + 1
        return left

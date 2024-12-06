class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        set_ban = set(banned)
        
        valid_numbers = [i for i in range(1, n + 1) if i not in set_ban]

        valid_numbers.sort()

        numsum = 0
        count = 0
        
        for num in valid_numbers:
            if numsum + num > maxSum:
                break
            numsum += num
            count += 1
        
        return count
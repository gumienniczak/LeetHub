class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = []
        for i in range(1,n+1):
            number = str(i)
            nums.append(number)
        nums.sort()
        for i in range(n):
            nums[i] = int(nums[i])
        return nums
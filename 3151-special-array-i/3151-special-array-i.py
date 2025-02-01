class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        result = []
        if len(nums) > 1:
            for num in nums:
                if num % 2 == 0:
                    result.append(1)
                else:
                    result.append(0)
            for i in range(1, len(result)):
                print(result[i - 1])
                print(result[i])
                if result[i - 1] + result[i] == 1:
                    print(True)
                    continue
                else:
                    print(False)
                    return False
                    
            return True
        
        elif len(nums) == 1:
            return True
        else:
            return False
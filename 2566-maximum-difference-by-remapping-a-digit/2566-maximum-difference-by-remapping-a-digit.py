class Solution:
    def minMaxDifference(self, num: int) -> int:
        min_num = num
        max_num = num
        num_str = str(num)
        digits_l = [digit for digit in num_str]
        candidates = set(digits_l)
        for cand in candidates:
            for i in range(10):
                remapped_s = num_str.replace(cand, str(i))
                if min_num > int(remapped_s):
                    min_num = int(remapped_s)
                if max_num < int(remapped_s):
                    max_num = int(remapped_s)        
        return max_num - min_num
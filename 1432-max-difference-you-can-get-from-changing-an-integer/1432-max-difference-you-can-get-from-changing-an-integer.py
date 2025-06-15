class Solution:
    def maxDiff(self, num: int) -> int:
        max_num = num
        min_num = num
        num_s = str(num)
        candidates = [dig for dig in num_s]
        cand_set = set(candidates)
        for i in cand_set:
            for j in range(10):
                if j == 0 and num_s.index(i) == 0:
                    continue
                else:
                    replaced_num = int(num_s.replace(str(i), str(j)))
                if replaced_num > max_num:
                    max_num = replaced_num
                if replaced_num < min_num:
                    min_num = replaced_num
                    
        return max_num - min_num


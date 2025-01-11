class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = defaultdict(int)
        odd_num = 0
        if len(s) < k:
            return False
        counts = len(s) * [k]
        for letter in s:
            counter[letter] += 1
        for value in counter.values():
            if value % 2 != 0:
                odd_num += 1
        
        if odd_num > k:
            return False
        else:
            return True

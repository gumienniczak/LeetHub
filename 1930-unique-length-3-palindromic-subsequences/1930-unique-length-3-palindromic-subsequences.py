class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = Counter(s)
        lr_candidates = set()

        for letter in letters:
            if letters[letter] >= 2:
                lr_candidates.add(letter)
        
        def get_indices(letter, lst):
            return [i for i in range(len(lst)) if lst[i] == letter]
        
        indices = [get_indices(letter, s) for letter in lr_candidates]

        result = 0

        for incs in indices:
            beg, end = incs[0], incs[-1]
            candidates = set(s[beg+1:end])
            result += len(candidates)
        
        return result
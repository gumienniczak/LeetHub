class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        outcome = 0
        n = len(pref)
        for word in words:
            if word[0:n] == pref:
                outcome += 1
        return outcome
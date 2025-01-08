class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        result = 0
        for i in range(n):
            word = words[i]
            word_len = len(word)
            candidates = words[i+1:]
            for candidate in candidates:
                if candidate[0:word_len] == word and candidate[-word_len:] == word:
                    result += 1

        return result

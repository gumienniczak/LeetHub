class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = []
        for rng in queries:
            beg = rng[0]
            end = rng[1]
            counter = 0
            for i in range(beg, end + 1):
                if words[i][0] in vowels and words[i][-1] in vowels:
                    counter += 1
            result.append(counter)
        return result

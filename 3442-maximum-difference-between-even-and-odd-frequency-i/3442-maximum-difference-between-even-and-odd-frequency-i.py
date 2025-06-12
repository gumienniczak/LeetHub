class Solution:
    def maxDifference(self, s: str) -> int:
        counter = dict()
        for char in s:
            if not counter.get(char):
                counter[char] = 1
            else:
                counter[char] += 1
        odds = []
        evens = []
        for el in counter.values():
            if el % 2 == 0:
                evens.append(el)
            else:
                odds.append(el)
        differences = []
        for odd in odds:
            for even in evens:
                diff = odd - even
                differences.append(diff)
        return max(differences)
class Solution:
    def minimumLength(self, s: str) -> int:
        new_string = s
        letters = {}
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = 1
            else:
                letters[s[i]] += 1
        delete_count = 0
        for letter, frequency in letters.items():
            if frequency % 2 == 1:
                delete_count += frequency - 1
            else:
                delete_count += frequency - 2
        return len(s) - delete_count
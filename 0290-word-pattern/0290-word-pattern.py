class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        mapping = {}
        mapped_words = {}

        for letter, word in zip(pattern, words):
            if letter in mapping:
                if mapping[letter] != word:
                    return False
            else:
                if word in mapped_words:
                    return False
                mapping[letter] = word
                mapped_words[word] = letter

        return True
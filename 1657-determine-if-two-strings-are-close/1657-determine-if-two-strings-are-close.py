from collections import defaultdict
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for ch in word1:
            freq1[ch] += 1
        
        for ch in word2:
            freq2[ch] += 1

        if set(freq1.keys()) != set(freq2.keys()):
            return False

        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True
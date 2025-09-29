from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = defaultdict(int)
        for letter in magazine:
            letters[letter] += 1
        
        for letter in ransomNote:
            if letter in letters:
                letters[letter] -= 1
                if letters[letter] == 0:
                    del letters[letter]
            else:
                return False
        
        return True
        
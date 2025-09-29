from collections import defaultdict
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b_counter = defaultdict(int)

        for letter in text:
            if letter in "balloon":
                b_counter[letter] += 1
        
        if any(c not in b_counter for c in "balloon"):
            return 0
        
        return min(b_counter["b"], b_counter["a"], b_counter["n"], b_counter["l"] // 2, b_counter["o"] // 2)

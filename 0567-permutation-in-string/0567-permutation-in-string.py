from collections import defaultdict

class Solution(object):
    def checkInclusion(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        counter1 = defaultdict(int)
        counter2 = defaultdict(int)

        for ch in s1:
            counter1[ch] += 1

        for i in range(n1):
            counter2[s2[i]] += 1

        if counter1 == counter2:
            return True

        # Sliding window
        left = 0
        for right in range(n1, n2):
            counter2[s2[right]] += 1
            char_to_remove = s2[left]
            counter2[char_to_remove] -= 1
            if counter2[char_to_remove] == 0:
                del counter2[char_to_remove]
            left += 1

            if counter1 == counter2:
                return True

        return False
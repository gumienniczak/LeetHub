from collections import defaultdict
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        frequency = defaultdict(int)
        for ch in s:
            frequency[ch] += 1

        result = []
        for ch in order:
            if ch in frequency:
                result.append(ch * frequency[ch])
                del frequency[ch]
        
        for ch, count in frequency.items():
            result.append(ch * count)
        
        return "".join(result)
        
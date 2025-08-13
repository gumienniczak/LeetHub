from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = defaultdict(int)
        output = []

        for char in s:
            counter[char] += 1
        
        cur_freq = 0
        dict_sort = sorted(counter, key = lambda x: counter[x], reverse=True)
        output = ""

        for val in dict_sort:
            output += val * counter[val]

        return output
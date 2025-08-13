from collections import defaultdict
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        counter = defaultdict(int)

        for num in arr:
            counter[num] += 1

        largest_int = -1

        for key, val in counter.items():
            if key == val and key > largest_int:
                largest_int = key
        
        return largest_int

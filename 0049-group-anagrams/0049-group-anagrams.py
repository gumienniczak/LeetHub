from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        outcome = defaultdict(list)
        for s in strs:
            k = sorted(s)
            outcome["".join(k)].append(s)
        
        return [x for x in outcome.values()]
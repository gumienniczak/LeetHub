from collections import defaultdict
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cities = defaultdict(list)
        for ins, outs in paths:
            cities[ins] = outs
        
        for city in list(cities.values()):
            if city not in list(cities.keys()):
                return city
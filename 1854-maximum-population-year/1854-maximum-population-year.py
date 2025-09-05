class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        max_pop = 0
        cur_pop = 0
        result_year = None
        events = []

        for b, d in logs:
            events.append((b, 1))
            events.append((d, -1))
        
        events.sort(key=lambda x: (x[0], x[1]))
        for year, change in events:
            cur_pop += change
            if cur_pop > max_pop:
                max_pop = cur_pop
                result_year = year
        
        return result_year

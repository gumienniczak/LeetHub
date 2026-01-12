class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        intervals.sort(key = lambda interval: interval[0])
        ans.append(intervals[0])
        for interval in intervals[1:]:
            if interval[0] <= ans[-1][1]:
                if ans[-1][1] < interval[1]:
                    ans[-1][1] = interval[1]
                else:
                    continue
            else:
                ans.append(interval) 
        
        return ans

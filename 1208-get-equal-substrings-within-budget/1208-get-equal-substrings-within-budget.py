class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        ans = float('-inf')
        left = 0
        cur = 0
        list1 = []
        list2 = []
        costs = []
        for i in range(len(s)):
            list1.append(ord(s[i]))
            list2.append(ord(t[i]))
        
        for el1, el2 in zip(list1, list2):
            costs.append(abs(el1 - el2))

        for right in range(len(costs)):
            cur += costs[right]
            while cur > maxCost:
                cur -= costs[left]
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
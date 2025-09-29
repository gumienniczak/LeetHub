class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        N = len(temperatures)
        ans = [0] * N
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_idx, stack_tmp = stack.pop()
                time = idx - stack_idx
                ans[stack_idx] = time

            stack.append((idx, temp))

        return ans 

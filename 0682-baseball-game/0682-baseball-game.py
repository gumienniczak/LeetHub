class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for op in operations:
            if op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            elif op == "+":
                new_num = stack[-1] + stack[-2]
                stack.append(new_num)
            else:
                stack.append(int(op))
        
        return sum(stack)
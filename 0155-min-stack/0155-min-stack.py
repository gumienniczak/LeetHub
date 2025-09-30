class MinStack(object):

    def __init__(self):
        self.stack = []
        self.lowest = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.lowest:
            self.lowest.append(val)
        elif self.lowest[-1] < val:
            self.lowest.append(self.lowest[-1])
        else:
            self.lowest.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.lowest.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.lowest[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
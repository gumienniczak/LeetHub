class MyCalendarTwo(object):

    def __init__(self):
        self.events = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """

        self.events.append((startTime, 1))
        self.events.append((endTime, -1))

        self.events.sort()

        cur_events = 0

        for time, change in self.events:
            cur_events += change
            if cur_events >= 3:
                self.events.remove((startTime, 1))
                self.events.remove((endTime, -1))
                return False
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
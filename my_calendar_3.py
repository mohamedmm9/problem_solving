class MyCalendarThree:

    def __init__(self):
        import bisect
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        bisect.insort_left(self.events, (start, 1))
        bisect.insort(self.events, (end, 0))

        res = 0
        booking = 0
        for _, state in self.events:
            booking += 1 if state == 1 else -1
            res = max(res, booking)
        return res

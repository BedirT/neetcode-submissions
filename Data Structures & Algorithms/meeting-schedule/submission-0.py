"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda it: it.start)

        for in1, in2 in zip(intervals, intervals[1:]):
            if in1.end > in2.start:
                return False

        return True



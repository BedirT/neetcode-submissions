"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda it: it.start)

        rooms_last = []
        for interval in intervals:
            # wanna find a suitable room if exists
            if not rooms_last:
                heapq.heappush(rooms_last, interval.end)
                continue
            cur_min_time = heapq.heappop(rooms_last)
            # either way we add
            heapq.heappush(rooms_last, interval.end)
            # we add back the removed one if starting a new room
            if cur_min_time > interval.start:
                heapq.heappush(rooms_last, cur_min_time)

        return len(rooms_last)

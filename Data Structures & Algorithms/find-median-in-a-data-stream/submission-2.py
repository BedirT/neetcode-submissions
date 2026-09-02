from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.med = SortedList([])

    def addNum(self, num: int) -> None:
        self.med.add(num)

    def findMedian(self) -> float:
        n = len(self.med)
        # print(self.med)
        if n % 2 == 0:
            return (self.med[n // 2 - 1] + self.med[n // 2]) / 2
        return self.med[n // 2]
        
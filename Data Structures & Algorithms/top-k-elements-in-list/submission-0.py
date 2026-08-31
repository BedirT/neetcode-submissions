from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        ct_sorted = dict(sorted(counter.items(), key=itemgetter(1), reverse=True))
        # print(ct_sorted)
        return list(ct_sorted.keys())[:k]
        
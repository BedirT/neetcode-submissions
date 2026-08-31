class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            # first stone
            mx = max(stones)
            stones.remove(mx)
            # second stone
            new_mx = max(stones)
            rem = abs(mx - new_mx)
            stones.remove(new_mx)
            mx = None
            stones.append(rem)
        if stones:
            return stones[0]
        else:
            return 0


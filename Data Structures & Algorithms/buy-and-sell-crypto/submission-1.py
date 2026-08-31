class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = max(prices)
        max_p = 0
        for i in range(len(prices)):
            min_so_far = min(prices[i],  min_so_far)
            max_p = max(max_p, prices[i] - min_so_far)
        return max_p

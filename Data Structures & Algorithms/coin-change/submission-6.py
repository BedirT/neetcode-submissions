class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * (amount)

        for value in range(amount + 1):
            # find the min coin for value
            for coin in coins:
                if value - coin >= 0:
                    dp[value] = min(dp[value - coin] + 1, dp[value])

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

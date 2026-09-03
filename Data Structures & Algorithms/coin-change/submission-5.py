class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memoize = {}

        def remove_coin(amount):
            if amount == 0:
                return 0
            if amount in memoize:
                return memoize[amount]

            vals = []
            for coin in coins:
                val = amount - coin
                if val >= 0:
                    steps = remove_coin(val)
                    if steps == -1:
                        continue
                    vals.append(1 + steps)
            if not vals:
                memoize[amount] = -1
                return -1
            res = min(vals)
            memoize[amount] = res
            return res

        return remove_coin(amount)

class Solution:
    def climbStairs(self, n: int) -> int:
        def count_valid_n_bit_numbers(n):
            phi = (1 + 5**0.5) / 2
            return round((phi ** (n + 2)) / (5**0.5))

        return count_valid_n_bit_numbers(n-1)

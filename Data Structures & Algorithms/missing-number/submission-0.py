class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot = sum(nums)
        n = len(nums)

        supposed_tot = int((n * (n + 1)) / 2)

        return supposed_tot - tot
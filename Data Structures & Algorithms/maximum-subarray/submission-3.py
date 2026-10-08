class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = [] 
        last = 0
        res = -float('inf')
        for num in nums:
            prev_max = max_so_far[-1] if max_so_far else -float('inf')
            max_so_far.append(max(num, num + prev_max))
            res = max(max_so_far[-1], res)
        return res
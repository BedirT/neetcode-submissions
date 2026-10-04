class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = {}
        res = 1
        for idx in range(len(nums)-1, -1, -1):
            num = nums[idx]
            LIS[idx] = 1
            for j_idx in range(idx+1, len(nums)):
                if nums[j_idx] > num:
                    LIS[idx] = max(LIS[idx], LIS[j_idx] + 1)
            res = max(LIS[idx], res)
        return res
        

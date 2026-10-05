class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mults = []

        mult_res = 1 # mult value of items on left of the num
        for num in nums: 
            mults.append([mult_res])
            mult_res *= num
        
        mult_res = 1 # now its right side
        for idx in range(len(nums)-1, -1, -1):
            num = nums[idx]
            mults[idx].append(mult_res)
            mult_res *= num

        res = []
        for idx in range(len(nums)):
            res.append(mults[idx][0] * mults[idx][1])

        return res
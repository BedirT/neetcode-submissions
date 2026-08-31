class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(int("1"*len(nums), 2) + 1):
            m_res = []
            bin_val = bin(i)[2:]
            bin_val = (len(nums) - len(bin_val)) * "0" + bin_val
            for j, x in enumerate(bin_val):
                if x == "1":
                    m_res.append(nums[j])
            res.append(m_res)
        return res
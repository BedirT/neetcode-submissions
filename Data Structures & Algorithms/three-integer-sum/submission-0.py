class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        all_s = set()
        for i, num in enumerate(nums):
            target = -num

            j = i + 1
            k = len(nums) - 1
            while j < k:
                tot = nums[j] + nums[k]
                if tot == target:
                    fin = [num, nums[j], nums[k]]
                    if str(fin) not in all_s:
                        res.append(fin)
                        all_s.add(str(fin))
                    j += 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1

        return res
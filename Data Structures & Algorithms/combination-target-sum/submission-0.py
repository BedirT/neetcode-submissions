class Solution:

    def combination_recursive(self, nums: list[int], target: int, current_vals: list[int]) -> list[list[int]]:
        res = []
        for i, num in enumerate(nums):
            # we selected num
            new_vals = current_vals + [num]
            if target - num > 0:
                sub_res = self.combination_recursive(nums[i:], target-num, new_vals)
                res.extend(sub_res)
            elif target - num == 0:
                # reached a res
                res.append(new_vals)
            # passed the target just keep going
        return res

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.combination_recursive(nums, target, [])
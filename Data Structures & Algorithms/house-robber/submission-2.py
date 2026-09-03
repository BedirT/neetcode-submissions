class Solution:
    def rob(self, nums: List[int]) -> int:
        # we never jump 3.
        mem = {}

        def jump(idx):
            # we take 2 after or 3 after always.
            if idx + 2 in mem:
                val_jump_2 = mem[idx + 2]
            else:
                val_jump_2 = jump(idx + 2) if idx + 2 < len(nums) else 0
                mem[idx + 2] = val_jump_2

            if idx + 3 in mem:
                val_jump_3 = mem[idx + 3]
            else:
                val_jump_3 = jump(idx + 3) if idx + 3 < len(nums) else 0
                mem[idx + 3] = val_jump_3
            
            return nums[idx] + max(val_jump_2, val_jump_3)

        if len(nums) < 2:
            return nums[0]
        return max(jump(0), jump(1))
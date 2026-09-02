class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = f"{n:0{32}b}"
        # print(bin_n)
        bin_n_rev = bin_n[::-1]
        # print(bin_n_rev)
        return int(bin_n_rev, 2)
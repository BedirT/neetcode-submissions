class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = {}
        for r in range(n):
            for c in range(n):
                if (r, c) in rotated:
                    val = rotated[(r, c)]
                else:
                    val = matrix[r][c]
                new_loc = c, (n - r - 1) # new r, c
                rotated[new_loc] = matrix[new_loc[0]][new_loc[1]]
                matrix[new_loc[0]][new_loc[1]] = val
                # print((r, c), "->", new_loc)
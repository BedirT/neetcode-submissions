class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]

        def traverse(r, c):
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dir in directions:
                new_r = r + dir[0]
                new_c = c + dir[1]
                if new_r >= 0 and new_c >= 0 and \
                   new_r < len(grid) and new_c < len(grid[0]):
                    traverse(new_r, new_c)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    traverse(r, c)
                    res += 1
                    # print(grid)

        return res
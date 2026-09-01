class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_size = len(board)
        col_size = len(board[0])

        visited = set()

        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

        def is_valid(loc):
            if loc[0] >= len(board) or loc[0] < 0 or \
                loc[1] >= len(board[0]) or loc[1] < 0:
                return False
            return True

        def move_all_around(cur: list[int], target_idx: int) -> bool:
            print(cur)
            if target_idx == len(word):
                # reached
                return True
            target = word[target_idx]
            for dir in directions:
                check_loc = (cur[0] + dir[0], cur[1] + dir[1])
                if not is_valid(check_loc):
                    continue
                new_char = board[check_loc[0]][check_loc[1]]
                if new_char == target and check_loc not in visited:
                    # next in line
                    visited.add(check_loc)
                    if move_all_around(check_loc, target_idx + 1):
                        return True
                    visited.remove(check_loc)
            
            return False

        for r in range(row_size):
            for c in range(col_size):
                if board[r][c] == word[0]:
                    visited.add((r, c))
                    moved = move_all_around((r, c), 1)
                    visited.remove((r, c))
                    if moved:
                        return True

        return False
                
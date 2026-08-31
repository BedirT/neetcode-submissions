class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_checks = [set() for _ in range(9)]
        col_checks = [set() for _ in range(9)]
        subb_checks = [set() for _ in range(9)]
        for row_idx in range(9):
            for col_idx in range(9):
                cell_val = board[row_idx][col_idx]

                if cell_val == ".":
                    continue

                subb_row_idx = row_idx // 3 
                subb_col_idx = col_idx // 3
                subb_idx = subb_row_idx * 3 + subb_col_idx

                if cell_val in row_checks[row_idx]:
                    # print("R", row_checks, row_idx, cell_val)
                    return False
                if cell_val in col_checks[col_idx]:
                    # print("C", col_checks, col_idx)
                    return False
                if cell_val in subb_checks[subb_idx]:
                    # print("S", subb_checks, subb_idx)
                    return False
                
                row_checks[row_idx].add(cell_val)
                col_checks[col_idx].add(cell_val)
                subb_checks[subb_idx].add(cell_val)

        return True

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        placeholder = "x"
        
        done = set()
        def mark_row_col(r, c):
            # row
            if f"R{r}" not in done:
                done.add(f"R{r}")
                for i in range(n_cols):
                    if matrix[r][i] != 0:
                        matrix[r][i] = placeholder

            # column
            if f"C{c}" not in done:
                done.add(f"C{c}")
                for i in range(n_rows):
                    if matrix[i][c] != 0:
                        matrix[i][c] = placeholder

        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] == 0:
                    mark_row_col(r, c)

        # traverse and alter 0s
        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] == placeholder:
                    matrix[r][c] = 0

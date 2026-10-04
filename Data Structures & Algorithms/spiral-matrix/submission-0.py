from math import ceil

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rounds = 0 # to keep track of spiral inward degree
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        def get_row(row_idx, reverse=False):
            selection = matrix[row_idx][::-1] if reverse else matrix[row_idx] 
            return selection[rounds: num_cols-rounds]

        def get_col(col_idx, reverse=False):
            res = []
            # starting +1 since row already gets corners
            for row_idx in range(rounds+1, num_rows-rounds-1): 
                res.append(matrix[row_idx][col_idx])
            if reverse:
                return res[::-1]
            return res

        final_res = []

        num_rounds = min(ceil(num_rows/2), ceil(num_cols/2))
        for idx in range(num_rounds): # idx is same as rounds
            final_res.extend(get_row(idx))
            final_res.extend(get_col(num_cols-idx-1))
            if num_rows-idx-1 != idx:
                final_res.extend(get_row(num_rows-idx-1, True))
            if num_cols-idx-1 != idx:
                final_res.extend(get_col(idx, True))
            rounds += 1

        return final_res

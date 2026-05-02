class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = [[False] * 9 for _ in range(9)]
        columns_seen = [[False] * 9 for _ in range(9)]
        square_seen = [[False] * 9 for _ in range(9)]

        for row_index in range(9):
            for col_index in range(9):
                value = board[row_index][col_index]

                if value == '.':
                    continue

                digit_index = int(value) - 1
                box_index = (row_index//3) *3 + col_index //3


                if (rows_seen[row_index][digit_index] or
                 columns_seen[col_index][digit_index] or
                  square_seen[box_index][digit_index]
                ):
                    return False
                rows_seen[row_index][digit_index] = True
                columns_seen[col_index][digit_index] = True
                square_seen[box_index][digit_index] = True
        
        return True


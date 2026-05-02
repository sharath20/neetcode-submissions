class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat_rows ,mat_cols = len(matrix), len(matrix[0])

        l, r = 0, mat_rows * mat_cols -1

        while l <= r:
            m = (l + r) // 2
            row ,col = m // mat_cols, m % mat_cols
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1 
            else:
                return True
        
        return False
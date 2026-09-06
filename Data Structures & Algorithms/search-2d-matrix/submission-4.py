class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       ROWS = len(matrix)
       COLS = len(matrix[0])

       top = 0
       bottom = ROWS - 1

       while top <= bottom:
        mid = top + (bottom - top) // 2

        if matrix[mid][0] > target:
            # target must be in a row ABOVE mid
            bottom = mid - 1
        elif matrix[mid][COLS - 1] < target:
            # target must be in a row BELOW mid
            top = mid + 1
        else:
            # target is in this row
            row = mid
            break
       if not (top <= bottom):
            return False
        
       left = 0
       right = COLS - 1

       while left <= right:
           mid = left + (right - left) // 2
           if matrix[row][mid] < target:
               left = mid + 1
           elif matrix[row][mid] > target:
               right = mid - 1
           else:
               return True
       return False
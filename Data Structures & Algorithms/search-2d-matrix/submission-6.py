class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       ROWS = len(matrix)
       COLS = len(matrix[0])

       top = 0
       bottom = ROWS - 1

       while top <= bottom:
        mid = top + (bottom - top) // 2

        if matrix[mid][0] > target:
            bottom = mid -  1
        elif matrix[mid][COLS - 1] < target:
            top = mid + 1
        else:
            row = mid
            break
        
       if not (top <= bottom):
        return False

       l = 0
       r = COLS - 1
       while l <= r:
        mid = l + (r - l) // 2

        if matrix[row][mid] > target:
            r = mid - 1
        elif matrix[row][mid] < target:
            l = mid + 1
        else:
            return True
       return False

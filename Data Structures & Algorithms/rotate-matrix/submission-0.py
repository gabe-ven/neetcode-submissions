class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #transpose 
        for row in range(len(matrix)):
            for col in range(row,len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


        #reverse
        for row in matrix:
            row.reverse()

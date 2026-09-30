class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # if the cell is 1, dfs through it keeping track of maxArea
        
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area




        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(area, maxArea)


        return maxArea



        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # if the cell is 1, dfs through it keeping track of maxArea
        
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Start from every treasure chest (0)
        # Explore outward through INF land cells
        # The first time we reach an INF cell, we know we've found
        # its shortest distance to any treasure chest
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visit = set()

        def addCell(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != INF or (r, c) in visit:
                return
            
            visit.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1


        

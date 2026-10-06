class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0
        # put all rotten fruits in queue initially
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                # count all fresh fruits
                elif grid[r][c] == 1:
                    fresh += 1
        
        def addCell(r, c):
            nonlocal fresh

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            fresh -= 1
            q.append((r, c))
        
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            time += 1

        return time if fresh == 0 else -1

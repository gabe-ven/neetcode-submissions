class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Approach (DFS)
        # 1. Start at every O along the four borders.
        # 2. Run DFS to find all connected Os and mark them as safe.
        # 3. Go through the entire board:
        # - If an O wasn't marked safe → change it to X.
        # - If an O was marked safe → leave it alone.
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == "X" or (r, c) in visit:
                return
            
            visit.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Top and bottom borders
        for c in range(COLS):
            dfs(0, c)           # Top row
            dfs(ROWS - 1, c)    # Bottom row

        # Left and right borders
        for r in range(ROWS):
            dfs(r, 0)           # Left column
            dfs(r, COLS - 1)    # Right column

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"



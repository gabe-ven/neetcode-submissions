from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        return components

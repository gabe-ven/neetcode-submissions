class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        connections = 0
        visited = set()
        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
                
        for i in range(n):
            if i in visited:
                continue
            else:
                visited.add(i)
                connections += 1
                dfs(i)
        return connections
        
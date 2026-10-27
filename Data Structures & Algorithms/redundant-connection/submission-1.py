class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(node, target, visited):
            if node == target:
                return True

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False

        adj = {i: [] for i in range(1, len(edges) + 1)}

        for u, v in edges:
            visited = set()

            if dfs(u, v, visited):
                return [u, v]

            adj[u].append(v)
            adj[v].append(u)
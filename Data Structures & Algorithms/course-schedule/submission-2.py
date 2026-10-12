class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c: [] for c in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        print(adj)
            
        visiting = set()

        def dfs(c):
            if c in visiting:
                return False
            if not adj[c]:
                return True

            visiting.add(c)
            for p in adj[c]:
                if not dfs(p): return False
            
            visiting.remove(c)
            adj[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        
        return True
            

    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        visiting = set()  # Current DFS path
        visited = set()   # Fully processed courses
        result = []       # Final course order
        

        def dfs(course):
            # 1. Cycle detected?
            if course in visiting:
                return False

            # 2. Already processed?
            if course in visited:
                return True

            # 3. Mark as currently exploring
            visiting.add(course)

            # 4. Explore prerequisites
            for p in adj[course]:
                if not dfs(p):
                    return False

            # 5. Mark as completed and append to result
            visited.add(course)
            visiting.remove(course)
            result.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return result
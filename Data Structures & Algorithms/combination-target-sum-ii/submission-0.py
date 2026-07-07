class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def dfs(i, cur_sum):
            if cur_sum == target:
                res.append(sol.copy())
                return
            if cur_sum > target or i == n:
                return

            sol.append(candidates[i])
            dfs(i + 1, cur_sum + candidates[i])
            sol.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur_sum)

        dfs(0, 0)
        return res

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        nums.sort()

        def backtrack(i):
            if i == n:
                res.append(sol.copy())
                return

            # Pick at nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            # Dont pick at nums[i]
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res
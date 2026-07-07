class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0

        for n in nums:
            prev, curr = curr, max(n + prev, curr)

        return curr
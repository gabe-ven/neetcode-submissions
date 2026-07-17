class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in num_set:
                length = 0
                current = n
                while current in num_set:
                    length += 1
                    current += 1
                res = max(res, length)
        return res
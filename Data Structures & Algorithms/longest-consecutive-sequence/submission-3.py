class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sett = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in sett:
                count = 0
                current = n
                while current in sett:
                    count += 1
                    current += 1
                longest = max(longest, count)
        return longest
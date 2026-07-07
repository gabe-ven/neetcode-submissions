class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
    # check if num - 1 is in the array
    # [1, 2, 3, 10, 11]
    # only 1 and 10 can be the start of a sequence, since 1 - 1 and 10 - 1 are not in the array

    # make nums array into a set
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        
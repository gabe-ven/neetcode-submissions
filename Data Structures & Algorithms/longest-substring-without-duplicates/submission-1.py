class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set(), set l = 0 and for loop for r ptr, 
        # while s[r] in set, remove s[l] and l += 1. 
        # after loop add s[r] to set, res = max(res, r - l + 1)
        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res

        # set: (, x, y, z )
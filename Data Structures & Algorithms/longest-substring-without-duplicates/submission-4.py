class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window
        # initiate l = 0 and r = 1
        # check if next character is in set, if not add it
        # move right pointer until a same character appears in set
        # keep count of longest substring

        l = 0
        longest = 0
        seen = set()

        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

            seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
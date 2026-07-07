class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       # l and r ptr, keep sliding and subtract count of most frequent char from window size, 
       # as long as max count <= k

       count = {}
       res = 0
       l = 0 

       for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        if (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
       return res
       
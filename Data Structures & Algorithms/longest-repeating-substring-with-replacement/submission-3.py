class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            # inc count of current char
            count[s[r]] = 1 + count.get(s[r], 0)

            # check if window - max count > k
            # if so, we need to slide window UP by l += 1
            # we also have to dec count of that char
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # update result as max of itself and length of the window
            res = max(res, r - l + 1)
        return res
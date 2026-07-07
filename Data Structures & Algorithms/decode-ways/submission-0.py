class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        prev2, prev1 = 1, 1  # dp[0] = 1, dp[1] = 1
        
        for i in range(2, len(s) + 1):
            curr = 0
            one_digit = int(s[i-1:i])
            two_digits = int(s[i-2:i])
            
            if 1 <= one_digit <= 9:
                curr += prev1
            if 10 <= two_digits <= 26:
                curr += prev2
            
            prev2, prev1 = prev1, curr
        
        return prev1

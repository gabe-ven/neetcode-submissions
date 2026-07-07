class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ""
        for ch in s:
            if ch.isalnum():
                letters += ch.lower()
        
        l = 0
        r = len(letters) - 1
        while l < r:
            if letters[l] != letters[r]:
                return False
            l += 1
            r -= 1

        return True
        
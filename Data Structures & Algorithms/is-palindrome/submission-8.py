class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters = ""
        for char in s:
            if char.isalnum():
                letters += char
        
        l = 0
        for r in range(len(letters) - 1, -1, -1):
            if letters[l].lower() != letters[r].lower():
                return False
            l += 1
        
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first combine all letter or number
        # have a left pointer and right pointer
        # check if left == right

        letters = ""
        for char in s:
            if char.isalnum():
                letters += char
        
        left = 0
        right = len(letters) - 1

        while left <= right:
            if letters[left].lower() != letters[right].lower():
                return False
            left += 1
            right -= 1
        return True



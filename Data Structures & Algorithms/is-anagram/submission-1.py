class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a dictionary (map)
        # loop through and count each character
        # if the number of characters in s is the same as t
        # then its an anagram

        if len(s) != len(t):
            return False
    
        countS = {}
        countT = {}
        for letter in s:
            countS[letter] = countS.get(letter, 0) + 1

        for letter in t:
            countT[letter] = countT.get(letter, 0) + 1
        
        return countS == countT
        




class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
       if len(s1) > len(s2):
        return False

       s1Count = {}
       s2Count = {}
       l = 0

       for i in range(len(s1)):
        s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)
        s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)

       if s1Count == s2Count:
        return True

       for r in range(len(s1), len(s2)):
        s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)

        if (r - l + 1) > len(s1):
            char = s2[l]
            s2Count[char] -= 1

            if s2Count[char] == 0:
                del s2Count[char]

            l += 1
        
        if s1Count == s2Count:
            return True

       return False
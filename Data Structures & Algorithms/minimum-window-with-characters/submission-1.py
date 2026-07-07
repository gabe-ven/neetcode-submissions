class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0 
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


        # 1. if t is empty, return empty string
        # 2. init countT hashmap with all leters in t
        # 3. loop through s with right ptr
        # 4. init window hashmap with each iteration 
        # 5. if current letter is in countT and window count and countT count are EQUAL, then inc have
        # 6. loop while have and need are equal
        # 7. check if current window is less than result length
        # 8. update result and result length
        # 9. dec current letter from window hashmap
        # 10. if current letter is in countT and window count < countT count, dec have value
        # 11. simply increase left ptr
        # 12. by the end we should have result, so just return result as long as resLen wasn't default value

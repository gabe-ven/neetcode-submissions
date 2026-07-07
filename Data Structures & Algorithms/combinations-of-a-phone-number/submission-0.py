class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl',
                        '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}

        if digits == '':
            return []
        
        res, sol = [], []

        def dfs(i):
            if i == len(digits):
                res.append(''.join(sol))
                return
            
            for letters in letter_map[digits[i]]:
                sol.append(letters)
                dfs(i+1)
                sol.pop()
            return
        
        dfs(0)
        return res
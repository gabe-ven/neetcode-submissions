class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for ch in s:
            if ch in closedToOpen:
                if stack and stack[-1] == closedToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack
        # push the open in the stack
        # if its a closed one, pop from stack
        # return True if stack is empty else False
        closeToOpen = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
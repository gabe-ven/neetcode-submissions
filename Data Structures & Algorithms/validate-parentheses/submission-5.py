class Solution:
    def isValid(self, s: str) -> bool:
        # add current to stack
        # if right character, pop stack

        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            # if its a closing char
            if c in closeToOpen:
                # if its the open char, pop from stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        # return true if stack is empty
        return True if not stack else False
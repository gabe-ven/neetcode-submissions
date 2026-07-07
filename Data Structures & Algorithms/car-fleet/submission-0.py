class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # list comprehension
        pair = [[p,s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]: # reverse sorted order
            # get the time
            stack.append((target - p) / s)
            # check if there are at least 2 cars in stack
            # make sure the TOP of the stack has lower or equal time
            # as the second car, which means they will become a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
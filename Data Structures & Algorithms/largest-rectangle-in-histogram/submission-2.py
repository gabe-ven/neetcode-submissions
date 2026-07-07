class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair, (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            # check if top height > height we just reached
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        # entrys still in our stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

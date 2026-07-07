class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use left and right pointer
        # start with left at 0 and right at len(heights) - 1
        # do while left < right
        # if left < right move left up
        # if right < left move right down
        # compute area by taking minimum of left or right pointer

        result = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            maxArea = (r - l) * min(heights[l], heights[r])
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            result = max(result, maxArea)

            
        return result
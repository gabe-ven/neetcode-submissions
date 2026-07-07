class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # compute the products of everything to the left and everything to the right
        left = [0] * len(nums)
        right = [0] * len(nums)

        for i in range(len(nums)):
            if i - 1 >= 0:
                left[i] = left[i - 1] * nums[i - 1]
            else:
                left[i] = 1

        for i in range(len(nums) - 1, -1, -1):
            if i + 1 < len(nums):
                right[i] = right[i + 1] * nums[i + 1]
            else:
                right[i] = 1
        
        # left: [1, 1, 2, 8]
        # right: [48, 24, 6, 1]

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = left[i] * right[i]

        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ideally we compute every prefix, all the nums BEFORE the num
        # and a postfix, all the nums AFTER the num


        # result array
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        n = len(nums)
      
        prev, curr = 0, 0
        for n in nums:
            prev, curr = curr, max(n + prev, curr)
        
        return curr
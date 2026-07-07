class Solution:
    def findMin(self, nums: List[int]) -> int:
      # compare m to l, if nums[m] >= nums[l] move left ptr up, 
      # otherwise move right ptr down, get the min of res and nums[m]

      # [3, 4, 5, 6, 1, 2]
      #  l        m      r

      l = 0
      r = len(nums) - 1
      res = nums[0]

      while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
            
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
      return res
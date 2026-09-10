class Solution:
    def findMin(self, nums: List[int]) -> int:
      # compare m to l, if nums[m] >= nums[l] move left ptr up, 
      # otherwise move right ptr down, get the min of res and nums[m]
      # if left is less than right, that means it sorted and just set result to min of res and left val
      

      # [3, 4, 5, 6, 1, 2]
      #  l        m      r

     l = 0
     r = len(nums) - 1

     while l < r:
        m = (l + r) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    
     return nums[r]
        
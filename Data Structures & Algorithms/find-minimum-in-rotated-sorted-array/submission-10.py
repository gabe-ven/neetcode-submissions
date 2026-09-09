class Solution:
    def findMin(self, nums: List[int]) -> int:
      # compare m to l, if nums[m] >= nums[l] move left ptr up, 
      # otherwise move right ptr down, get the min of res and nums[m]
      # if left is less than right, that means it sorted and just set result to min of res and left val
      

      # [3, 4, 5, 6, 1, 2]
      #  l        m      r

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]
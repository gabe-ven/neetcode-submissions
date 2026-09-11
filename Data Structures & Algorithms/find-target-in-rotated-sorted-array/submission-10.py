class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums=[4,5,6,7,0,1,2]
        # target=0
        # Your Output: -1
        # Expected output: 4
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # left side sorted
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # right side sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


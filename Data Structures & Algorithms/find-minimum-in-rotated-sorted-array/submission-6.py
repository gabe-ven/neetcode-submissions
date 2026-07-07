class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # If the array is already sorted, nums[l] is the minimum
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            # Left half is sorted
            if nums[l] <= nums[m]:
                l = m + 1
            else:  # Right half is sorted, rotation is on left
                r = m - 1

        return res

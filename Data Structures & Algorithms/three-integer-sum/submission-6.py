class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue  # skip duplicate pivot

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = a + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res

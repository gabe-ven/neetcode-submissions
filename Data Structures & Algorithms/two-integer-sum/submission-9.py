class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dictt:
                return [dictt[diff], i]
            dictt[nums[i]] = i

        return []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # value: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


        # [3, 4, 5, 6] target = 7
        # diff = 7 - 3 = 4
        # prevMap[3] = 0
        # diff = 7 - 4 = 3
        # is 3 in prevMap? yes
        # return 
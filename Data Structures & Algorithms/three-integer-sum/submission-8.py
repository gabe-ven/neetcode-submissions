class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        arr = sorted(nums)
        res = []
        for i in range(len(arr)):

            if i > 0 and arr[i] == arr[i - 1]:
                continue

            a = arr[i]
            l = i + 1
            r = len(arr) - 1
            while l < r:
                if a + arr[l] + arr[r] > 0:
                    r -= 1
                elif a + arr[l] + arr[r] < 0:
                    l += 1
                else:
                    res.append([a, arr[l], arr[r]])
                    l += 1
                    r -= 1

                    while l < r and arr[l] == arr[l - 1]:
                        l += 1
                    
                    while l < r and arr[r] == arr[r + 1]:
                        r -= 1


        return res
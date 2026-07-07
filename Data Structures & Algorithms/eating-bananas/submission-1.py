class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find the minimum k value to eat all piles within h hours
        # search between 1 and the max in piles
        # start with middle (l + r) // 2 -> this our k
        # divide all the piles by k, and sum each one to hours
        # if hours <= h, set the result to the minimum of result and k. update right pointer down to see for better k
        # otherwise update left pointer 

       l = 1
       r = max(piles)
       res = r

       while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
       return res


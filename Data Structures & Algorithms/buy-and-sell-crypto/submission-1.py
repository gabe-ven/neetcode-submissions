class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l and r ptr, while r < len(prices), 
        # check if left price < right price, 
        # set profit as difference and get max, else set l ptr = r ptr. r += 1 
        l = 0
        r = 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
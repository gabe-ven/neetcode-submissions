import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # list of values that occur particular num of times
        # size of input + 1
        freq = [[] for i in range(len(nums) + 1)] 

        # inc count for each num
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # for every number and count, 
        for n, c in count.items():
            # "this value n occurs c number of times"
            freq[c].append(n)
        
        res = []
        # iterate in descending to get which occurs most frequently
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # res has to be length of k, so return when that occurs
                if len(res) == k:
                    return res




class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) #instead of 0, len(piles)-1
        res = r
        #for i in piles: # to find what's the max -- don't need this, can just do Max
           # Max = max(Max, i)
        
        #arr = []
        #for i in range(1,Max+1): # to fill the array from 1 to Max+1
        #    arr.append(i) don't need this, we already do it in the while loop

        while l <= r:
            k = (l + r)// 2
            Sum = 0
            for i in piles:
                Sum += math.ceil(i/k)
            if Sum <= h:
                res = min(res, k) #not just r= k -1
                r = k -1
            else:
                l = k+1
        return res
    
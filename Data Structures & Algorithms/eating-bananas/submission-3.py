import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Thought Process- for piles = [1,4,3,2]
        try all possible combos- from 1 to h, eg 1,2,3,4,5,6,7,8,9
        use binary search to help reduce this search

        say eating rate is 2, divide each index by two than
        take ceil of it-> ceil(1/2)+ ceil(4/2) + ceil(3/2) + ceil(2/2) = 6

        problems i faced:- Wrong right boundary, Not resetting rate,
        Incorrect min_rate update, Incorrect binary search movement.
        
        '''

        l, r = 1, max(piles) # r is how much koko can eat at any hour
        min_rate = max(piles) 

        while l <= r:
            mid = (l+r)//2
            rate = 0
            for i in piles:
                rate += math.ceil(i / mid)
            
            if rate <=h:
                min_rate = min(min_rate, mid)
                r= mid-1
            else:
                l = mid+1
            
        return min_rate

                



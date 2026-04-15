class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        '''
        diff = 0
        Maxdiff =0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                Maxdiff = max(Maxdiff, diff)
        
        return Maxdiff

        '''

        #optimal- O(n) Time and O(1) space- Sliding window
        
        l, r = 1, len(prices)-1
        currMin = prices[0]
        maxDiff = 0

        while l <= len(prices)-1:
            diff = prices[l] - currMin
            currMin = min(currMin, prices[l])
            maxDiff = max(maxDiff, diff)
            l+=1
        
        return maxDiff

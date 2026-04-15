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
        
        l = 1
        currMin = prices[0]
        maxP = 0

        while l <= len(prices)-1:
            diff = prices[l] - currMin
            currMin = min(currMin, prices[l])
            maxP = max(maxP, diff)
            l+=1
        
        return maxP

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        diff = 0
        Maxdiff =0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                Maxdiff = max(Maxdiff, diff)
        
        return Maxdiff
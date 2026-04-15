class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force approach- utilizes two pointers, one on curr index and other on entire loop
        '''
        finArea= 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = (j-i) * min(heights[i], heights[j])
                finArea = max(finArea, area)
        
        return finArea
        '''
        #optimal approach
        res= 0
        res2 = 0
        l = 0
        r = len(heights) - 1
        while(l < r):
            res2 = (r - l) * min(heights[l], heights[r]) 
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            else:
                l+=1
            res = max(res,res2)
            
        return res
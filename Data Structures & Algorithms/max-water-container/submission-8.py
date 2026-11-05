class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights)-1

        max_arr=0
        while l < r:

            area = min(heights[r], heights[l]) * (r-l)
            max_arr = max(max_arr, area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            
        
        return max_arr
            

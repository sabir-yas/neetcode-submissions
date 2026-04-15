class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        my approach: tried my best
        i = 0
        l, r = 0, 0
        res = 0

        while( i < len(height)):
            if height[i] == 0 and i > 0:
                if i + 1 < len(height) and height[i-1] != height[i+1]:
                    res  +=  min(height[i+1], height[i-1]) * ((i+1)-(i-1))
                else:
                    l, r = i, i 
                    res+=1
                    width=0
                    area = 0
                    while height[l] == height[r]:
                        width+=1
                        l-=1
                        r+=1
                    area = width *(height[i+1])
                    res += area
                    
            i+=1
            
        return res
        '''
        #O(n) time, O(n) space
        
        #O(n) time, O(1) space
        res = 0
        l = 0
        r = len(height) -1
        leftMax= height[l]
        rightMax= height[r]

        while(l < r):
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax- height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax- height[r]
        return res


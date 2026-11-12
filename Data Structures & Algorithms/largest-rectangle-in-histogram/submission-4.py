class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        '''
        #monotically increasing stack, which means that we only 
        really start to care if curr and right are increasing
        
        make sure to get the formula right- stackHeight * (i-index)
        '''

        stack = []
        maxarea = 0

        for i, h in enumerate(heights):

            start =i
            while stack and stack[-1][1] > h: # when it starts to descrease we don't want to count it
                index, stackHeight = stack.pop()
                maxarea = max(maxarea, stackHeight * (i-index))
                start = index
        
            #append to stack by default
            stack.append((start,h))
        
        for i, h in stack:
            maxarea = max(maxarea, h *(len(heights) - i))

        return maxarea
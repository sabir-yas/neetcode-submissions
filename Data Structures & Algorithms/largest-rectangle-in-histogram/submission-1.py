class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #stack approach
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i #this is important
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max( maxArea,height * (i - index)) # remember height * (i-index)
                start = index # here it's start = index, because index is what is the previous element on the stack
            stack.append((start, h)) #here we are appending the current value, not the one already on the top of the stack(not height)

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            

        return maxArea

        '''
        # have a enumerate for loop
        start is the current index
        while stack is not empty and the value of the popped value of stack  is greater 
        than current value,
            then pop the current stack value and index, storing them,
            find the max area between this and curr index,
            start will be popped val's index(remember we are moving back for start)
        then add the (pushed back)index with the current height to stack

        have a separate for loop for unpopped vals in stack
        for enumerate loop in the stack
        maxarea is the max of the maxarea and the area from current h to end of the heights

        '''

    #brute force- for a given value with its index, find it's max right and max left.
    
        















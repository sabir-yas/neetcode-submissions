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
                start = index # remember! here it's start = index, because index is what is the previous element on the stack
            stack.append((start, h)) #here we are appending the current value, not the one already on the top of the stack(not height)

        for i, h in stack: # remember!
            maxArea = max(maxArea, h * (len(heights) - i))
            

        return maxArea

    #brute force- for a given value with its index, find it's max right and max left.
# creating stack , maxarea=0
# for loop- start value, and a while loop to manage decreasing elements, at end of for loop- append to stack
# for loop to traverse elements left in stack- form areas until






































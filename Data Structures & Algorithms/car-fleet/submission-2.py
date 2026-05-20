class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #stack approach

        pair = [[p,s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]: #remember we are checking from the reverse sorted order- O(n log n)
            stack.append((target- p)/ s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


'''
test
    pair = [[p,s] for p,s in zip(position, speed)] #it's [p,s]
    stack = []

    for p, s in sorted(pair)[::-1]:

        time = (target - p)/ s
        stack.append(time)
        if len(stack) >=2 and stack[-1] >= stack[-2]:
            stack.pop()
        ## not here stack.append(time)
    
    return len(stack)

'''
'''
    p,s = [[4,2][[1,2][0,1][7,1]]
    stack=[]
    traverse from the back
        sorted-[[0,1][1,2][4,2][7,1]]
        look at [7,1]
        calculate time- 10-7/1= 3

        add to stack- [3,]

        look at [4,2]
        calculate time- 10-4/2= 3
        add to stack [3,3]

        look at [1,2]
        calculate time- 10-1/2= 4.5
        add to stack[3,3,4.5]

        return the length of stack. this would be 3

    '''





































class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        #brute force- O(n^2)
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):

            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j- i # j - i better than having a count variable
                    break
            
        return res
        #using stack my failed approach
        stack = []
        res = [0]*len(temperatures)
        count = 0
        for i in range(len(temperatures)):
            stack.append(temperatures[i])
            if len(stack) > 0 and stack[i] > stack[i-1]:
                count +=1
            res[i] = count

        return res
        '''
        
        res = [0] * len(temperatures)
        stack = [] # key value: [temp, ind]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #remember t > stack[-1][0]
                stackT, stackInd= stack.pop()
                res[stackInd] = (i - stackInd) # also i - stack T
            stack.append([t,i])
        return res



